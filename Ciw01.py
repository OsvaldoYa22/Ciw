#suponga que es un gerente de banco y le gustaria 
#saber cuanto tiempo esperan los clientes en su banco

#clientes llegan al azar 12 por hora
#tiempo de atencion dura 10 minutos
#cuenta con 3 servidores

####  ¿En promedio cuanto esperan los clientes?  ####

import matplotlib.pyplot as plt
import ciw
#ahora debemos decirle a Ciw como se ve nuestro sistema

#number of servers = numero de servidores
#arrival distributions = distribucion de llegadas
#service distributions = distribucion de atencion

#Tomar en cuenta que se las  unidades se consideran en min.
N = ciw.create_network(arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
	service_distributions=[ciw.dists.Exponential(rate=0.1)],
	number_of_servers=[3])
#Esto define completamente a nuestro banco
#observe que Exponential es la distribucion que siguen nuestros arrival y servers

#Establecemos una semilla 
ciw.seed(1)
#ahora creamos la simulacion
Q = ciw.Simulation(N)
#Simulamos para un día
#como los parametros estan en minutos un día seria 1440
Q.simulate_until_max_time(1440)

#¿como exploramos el objeto de simulacion Q?
#nodo de llegada = Q.nodes[0]
#nodo de servicio = Q.nodes[1]
#nodo de saldida = Q.nodes[-1]

#orden en el que teriminaron el servicio
### Q.nodes[-1].all_individuals
#clientes que se quedaron en la simulacion cuando esta termino
### Q.nodes[1].all_individuals

#pero esta no es una manera muy eficionte de mirar los resultados

#podemos obtener una lista de todos los registros con 
recs = Q.get_all_records()
# Una lista de tiempos del servidor
servicetimes = [r.service_time for r in recs]
# Una lista de espera
waits = [r.waiting_time for r in recs]

#Ahora podemos obtener estadisticas manipulando las listas
mean_service_time = sum(servicetimes)/len(servicetimes)
print("Tiempo medio de atencion del servidor",mean_service_time)
mean_waits = sum(waits)/len(waits)
print("Tiempo medio de espera",mean_waits)
#Ya sabemos el tiempo promedio de espera de los clientes

#que tan ocupados o inactivos han estado nuestros servidores
pro=Q.transitive_nodes[0].server_utilisation
print("En promedio los servidores estuvieron ocupados","%10.2f"%(pro*100),"% de tiempo")
#Asi en nuestro banco, en promedio los servidores 
#estuvieron ocupados el 75.3% del tiempo 


#ahora podemos graficar los timepos de espera
plt.hist(waits,color='grey',edgecolor='black')
plt.show()

