Librerías a instalar:
- Django
- Djangorestframework
- django-db-connection-pool
- mysqlclient
- mysql-connector-python
- redis
- django-redis
  
A continuación se desarrollan los 8 puntos del caso, para ello se documenta cada uno de los pasos y se añade el código en general.

## 1. cree una tabla o collection en la base de datos y llenela con 60000 registros ficticios

La base de datos a utilizar corresponde a MySQL. Para la creación de la base de datos e insertar los 60000 datos, se utilizó un archivo .sql, el cual se puede visualizar en el apartado Docker/init.sql 

![alt text](Images/image.png)

En la imagen anterior se muestra la creación de la tabla y la creación de los datos que irán dentro de la base de datos.

## 2. agregue un endpoint a su REST api que dado un query y o parámetros retorne aproximadamente un 35% de los registros

Ya que se optó por el uso de Python, una de las tecnologías disponibles en ese lenguaje para la implementación de un servicio REST que utilizaremos es Django, el cual también es de utilidad para el desarrollo del proyecto. En el apartado Python/Django/api/views.py es donde se puede encontrar la lógica del proceso, en el cual se realiza el retorno del 35% de los datos. En la siguiente imagen se muestra la clase y sus funciones. 

![alt text](Images/EndPoint1.png)

En el caso de la creación del EndPoint este es realizado en el apartado Python/Django/api/urls.py. Se añade una imagen donde se realiza dicho proceso.

![alt text](Images/CreateEndPoint1.png)


## 3. agregue otro endpoint a su REST api que haga exactamente lo mismo del punto #2 y que haga uso de un fixed size connection pool para el acceso de la base de datos

Con el fin de no reiterar en las mismas explicaciones del paso anterior, solo serán añadidas imágenes que sean referentes a la creación de los elementosm, a continuación se añaden dichas imágenes. 

Clase donde se realiza el fixed size connection pool.

![alt text](Images/EndPoint2.png)

Creación del segundo EndPoint

![alt text](Images/CreateEndPoint2.png)

## 4. agregue otro endpoint a su REST api que haga exactamente lo mismo del punto #2 y #3 y agregue una cache por medio de un redis server, de tal forma que los parámetros del endpoint sirvan de llave para la cache, permitiendo que hayan cache hits y fails entre los requests

Clase donde se agrega una cache por medio de un redis server.

![alt text](Images/EndPoint3.png)

Creación del tercer EndPoint

![alt text](Images/CreateEndPoint3.png)

A diferencia de los demás, aquí cabe resaltar que Django es muy flexible y tiene cosas interesantes, por lo que la caché de Redis fue manejada desde el archivo settings.py de Django y accedida por la clase.

![alt text](Images/CacheRedis.png)

## 5. una vez terminado y probados los endpoints dockerice la solución, usando un container para el api, otro para redis y otro para la base de datos. utilice docker compose para dockerización. este paso se pudo haber hecho desde el paso #1.

Desde el primer paso se realizó uso de Docker, en este caso se creó una carpeta llamada Docker, en la cual se ubica el docker-compose.yml. Ya que el documento es algo extenso, no se añadirá imagen, pero este paso ya está realizado y se ubica en la ruta Docker/docker-compose.yml

## 6. utilizando postman o jmeter, proceda a ejecutar un test de stress sobre la solución implementada, atacando a los 3 endpoints, configure la prueba para que se simulen 20 clientes (threads) concurrentes haciendo los requests continuamente con una pausa de 233ms entre cada request de cada thread. la prueba completa corre durante 1 minuto.

En este caso se decidió hacer uso de Jmeter. Como primer paso se definen los 20 clientes (threads).

![alt text](Images/Threads.png)

El tiempo es manejado en segundos, por lo que se ingresa un tiempo de 0.233 segundos.

![alt text](Images/Seconds.png)

Como segundo paso se crearon las pruebas de los 3 endpoints por lo que se realizá una prueba individual para cada endpoint. 

![alt text](Images/Jmeter.png)

A continuación se añaden imágenes de las pruebas de 1 minuto de cada endpoint, aclarando que las siguientes imágenes solo evidencian que fueron ejecutados en el tiempo correspondiente los endpoints correspondientes, los datos arrojados serán abordado más adelante:

1. Prueba EndPoint 1:

![alt text](Images/PruebaEndPoint1.png)

2. Prueba EndPoint 2:

![alt text](Images/PruebaEndPoint2.png)

3. Prueba EndPoint 3:

![alt text](Images/PruebaEndPoint3.png)

## 7. extraiga los resultados obtenidos por el software de pruebas (jmeter o postman), de lo que tenga para monitorear conexiones de base de datos, cpu y memoria del lado de los servidores, tabule toda la información asegurándose de tener medidas de las variables:

Para poder monitorear dichos datos se harán uso de dos medidores de métricas, los cuales corresponden a Prometheus y Docker

### Métricas según Prometheus


### Métricas según Docker


  - cpu, memoria y conexiones de la base de datos para cada endpoint
  - cpu, memoria y conexiones de redis para cada endpoint
  - cpu, memoria y conexiones del backend api para cada endpoint
  - tiempo promedio de respuesta para cada endpoint

## 8. emita las conclusiones cuantitativas basadas en los resultados obtenidos que contrasten los cambios de rendimiento usando el framework seleccionado para REST, la incorporación de pool, y de cache respectivamente

En el punto 6 se realizaron las pruebas, pero sin mostrar los datos arrojados en cada una de las pruebas de los endpoints, a continuación se añadirán imágenes relacionadas a cada endpoint para después realizar las conclusiones correspondientes.

1. Prueba EndPoint 1:



2. Prueba EndPoint 2:



3. Prueba EndPoint 3:



Metricas de Prometheus:

Se accede a prometheus con el localhost:9090

Generales:
- process_cpu_seconds_total: Tiempo total de CPU usado por cada proceso
- process_resident_memory_bytes: Cantidad de memoria residente utilizada por cada proceso
- process_virtual_memory_bytes: Cantidad de memoria virtual utilizada por cada proceso

Mysql:
- mysql_global_status_queries: Número total de consultas ejecutadas.
- mysql_global_status_max_used_connections: El máximo número de conexiones simultáneas utilizadas desde que el servidor se inició.
- mysql_global_status_threads_connected


Redis:
- redis_memory_used_bytes: Cantidad de memoria utilizada por Redis.
- redis_memory_used_peak_bytes: Memoria máxima utilizada por Redis desde que comenzó.
- redis_cpu_sys_seconds_total: Tiempo de CPU usado por Redis en modo de sistema.
- redis_cpu_user_seconds_total: Tiempo de CPU utilizado por Redis en el espacio de usuario.
- redis_total_connections_received: Total de conexiones recibidas.

Django:
- http_requests_total: Total de solicitudes HTTP recibidas por la aplicación Django.
- http_request_duration_seconds: Latencia de las solicitudes HTTP.
- http_request_size_bytes: Tamaño de las solicitudes HTTP entrantes.
- http_response_size_bytes: Tamaño de las respuestas HTTP enviadas.


Metricas de docker:

- Comando: Docker stats 
- Grafico desde containers/redis-1, mysql-1, rest-api-1/stats

