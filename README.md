# Ciw
En este repositorio encontraras programas de simulación de eventos discretos, asi como un ejemplo muy practico con interfaz grafica de usuario (GUI) con n-servidores de lineas de espera con la libreria Ciw.
## Instalación 
Ciw actualmente es compatible y se prueba regularmente en las versiones de Python 3.6, 3.7 y 3.8.

![Image text](https://github.com/OsvaldoYa22/Ciw/blob/main/Captura02.PNG)
```R
$ pip install ciw
```

## Líneas de espera
Suponga que es gerente de un banco y le gustaria saber cuanto tiempo esperan uss clientes en su banco.
* Los clientes llegan al azar aproximadamente 12/hora con una distribución Exponencial
* El tiempo de atención dura aproximadamente 10 minutos con una distribución Exponencial
* Cuenta con 3 servidores
¿En primedio cuanto esperan os clientes?
Solución:
Primero importamos nuestras librerias
```R
import ciw
```
Ahora debemos decirle a Ciw como se ve nuestro sistema
* number of servers = numero de servidores
* arrival distributions = distribucion de llegadas
* service distributions = distribucion de atencion
  
Tomar en cuenta que las unidades se consideran en minutos, por esta razón:
* Exponential(rate=0.2) describe nuestras llegadas (12/hora)
* Exponential(rate=0.1) describe el tiempo de atención del servidor
```R
N = ciw.create_network(arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
	service_distributions=[ciw.dists.Exponential(rate=0.1)],
	number_of_servers=[3])
```
Ahora establecemos una semilla y creamos nuestro banco.
```R
#Establecemos una semilla 
ciw.seed(1)
#ahora creamos la simulacion
Q = ciw.Simulation(N)
```
Simulamos un día (1440 min.).
```R
Q.simulate_until_max_time(1440)
```
### Explorando nuestra simulación
Usando la comprensión de listas, podemos obtener listas de cualquier estadística que nos guste:
```R
#podemos obtener una lista de todos los registros con 
recs = Q.get_all_records()
# Una lista de tiempos del servidor
servicetimes = [r.service_time for r in recs]
# Una lista de espera
waits = [r.waiting_time for r in recs]
```


Puede consultar mas a fondo el funcionamiento de los programas en el siguiente archivo [Ciw.pdf](https://drive.google.com/file/d/1w9887JvFKDoik8pYWmqQjP0H-_FlJ6tP/view?usp=sharing)
