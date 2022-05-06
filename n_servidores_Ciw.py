from random import random
from tkinter import ttk
from tkinter import *
import tkinter as tk
import math
import ciw

def N_servidores(n,T,l_l,l_a):
    n_simulaciones = 100 
    T_convertido = T*1440
    N = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(rate=l_l)],
        service_distributions=[ciw.dists.Exponential(rate=l_a)],
        number_of_servers=[n])

    average_waits = []
    lista_colas = []

    for trial in range(n_simulaciones):

        ciw.seed(trial)
        Q = ciw.Simulation(N)
        Q.simulate_until_max_time(T_convertido)
        recs = Q.get_all_records()
        waits = [r.waiting_time for r in recs if r.arrival_date > 100 and r.arrival_date < 1540]
        mean_wait = sum(waits) / len(waits)
        average_waits.append(mean_wait)
        cola = [r.queue_size_at_arrival for r in recs]
        mean_cola = sum(cola)/len(cola)
        lista_colas.append(mean_cola)

    prom=round(sum(average_waits) / len(average_waits),2)
    prom2=round(sum(lista_colas)/ len(lista_colas),2)

    app.title('Resultados')
    app.geometry('350x495')
    tabla=ttk.Treeview(app)
    tabla.pack(ipadx=40,ipady=25)
    tabla.insert("",END,text="Promedio en minutos que los")
    tabla.insert("",END,text=" clientes esperan en la fila :")
    tabla.insert("",END,text=prom)
    tabla.insert("",END,text="Promedio de usuarios que hay")
    tabla.insert("",END,text=" en la cola es de :")
    tabla.insert("",END,text=prom2)
    tabla.place(x=20,y=255)

class SampleApp(tk.Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)

        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        #new_frame.config(bg='blue')
        new_frame.config(width="350",height="350")
        #new_frame.geometry('350x495')
        new_frame.pack(fill='none')
        new_frame.pack(padx=5,pady=5,ipadx=30,ipady=30)
        
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #Label(self, text="Eventos discretos").pack( padx=10,pady=10)
        Label(self, text="Lineas de espera con parametros :\n \n *Primero en llegar primero en ser atendido \n *Las llegadas siguen una distribución Exponencial \n*El tiemo de atención sigue distribución Exponencial ").pack(padx=15,pady=2,ipadx=50,ipady=10)
      
        Button(self, text="Simular ",
                  command=lambda: master.switch_frame(Ingresa_datos)).pack(padx=15,pady=5,ipadx=50,ipady=10)
        
        

class Ingresa_datos(tk.Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        def datos_guardados():

            Ser_data = int(str(Ser.get()))
            T_data = int(str(T.get()))
            lle_data = float(str(lleg.get()))
            ser_ate_data = float(str(serr.get()))
            N_servidores(Ser_data,T_data,lle_data,ser_ate_data)
        app.geometry('350x495')
        numero_ser = Label(text="Ingrese el número de servidores")
        numero_ser.place(x=22,y=20)
        T_sim  =Label(text="Ingrese el tiempo total a simular en días")
        T_sim.place(x=22,y=70)
        lambda_entrada = Label(text="Ingrese el parametro de llegada (usuario/minuto) ")
        lambda_entrada.place(x=22,y=140)
        mu_entrada = Label(text="Ingrese el parametro atención (usuario/minuto)")
        mu_entrada.place(x=22,y=200) 
        Enter = Button(app,text="Enter",command=datos_guardados)
        Enter.place(x=302,y=120)

        Ser = StringVar()
        T = StringVar()
        lleg = StringVar()
        serr = StringVar()

        Ser_entry = Entry(textvariable=Ser,width="40")
        t_entry = Entry(textvariable=T,width="40")
        lleg_entry = Entry(textvariable=lleg,width="40")
        serr_entry = Entry(textvariable=serr,width="40")
        
        Ser_entry.place(x=22,y=40)
        t_entry.place(x=22,y=100)
        lleg_entry.place(x=22,y=170)
        serr_entry.place(x=22,y=230)

if __name__ == "__main__":
    app = SampleApp()

    app.mainloop()