Docker instalado

Desdocumentar la parte de sql del docker-compose.yml
Docker\docker-compose up

Trabajar en sqlworkbench para el local

Trabajar con urls.py 

Trabajar con products y products 2

Librerías a instalar:
- Django
- Djangorestframework
- django-db-connection-pool
- mysqlclient
- mysql-connector-python
- redis
- django-redis
  

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


