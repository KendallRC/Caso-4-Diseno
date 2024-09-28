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



## 2. agregue un endpoint a su REST api que dado un query y o parámetros retorne aproximadamente un 35% de los registros



## 3. agregue otro endpoint a su REST api que haga exactamente lo mismo del punto #2 y que haga uso de un fixed size connection pool para el acceso de la base de datos



## 4. agregue otro endpoint a su REST api que haga exactamente lo mismo del punto #2 y #3 y agregue una cache por medio de un redis server, de tal forma que los parámetros del endpoint sirvan de llave para la cache, permitiendo que hayan cache hits y fails entre los requests



## 5. una vez terminado y probados los endpoints dockerice la solución, usando un container para el api, otro para redis y otro para la base de datos. utilice docker compose para dockerización. este paso se pudo haber hecho desde el paso #1.



## 6. utilizando postman o jmeter, proceda a ejecutar un test de stress sobre la solución implementada, atacando a los 3 endpoints, configure la prueba para que se simulen 20 clientes (threads) concurrentes haciendo los requests continuamente con una pausa de 233ms entre cada request de cada thread. la prueba completa corre durante 1 minuto.



## 7. extraiga los resultados obtenidos por el software de pruebas (jmeter o postman), de lo que tenga para monitorear conexiones de base de datos, cpu y memoria del lado de los servidores, tabule toda la información asegurándose de tener medidas de las variables:

  - cpu, memoria y conexiones de la base de datos para cada endpoint
  - cpu, memoria y conexiones de redis para cada endpoint
  - cpu, memoria y conexiones del backend api para cada endpoint
  - tiempo promedio de respuesta para cada endpoint

## 8. emita las conclusiones cuantitativas basadas en los resultados obtenidos que contrasten los cambios de rendimiento usando el framework seleccionado para REST, la incorporación de pool, y de cache respectivamente


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

