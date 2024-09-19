import redis
import json


# Configuración de Redis
redis_client = redis.StrictRedis(
    host='localhost',  # Cambia esto si tu servidor Redis está en otra máquina
    port=6379,         # El puerto por defecto de Redis
    db=0,              # Base de datos por defecto en Redis
    decode_responses=True
)

def get_cache_key(self, request):
        # Genera una clave única para el cache usando los parámetros de la solicitud
    params = request.query_params.keys()
    return json.dumps(params, sort_keys=True)

def get_cached_response(self, cache_key):
        # Intenta obtener los datos del cache
    return redis_client.get(cache_key)

def set_cache_response(self, cache_key, data):
        # Guarda los datos en el cache con una expiración (por ejemplo, 10 minutos)
    redis_client.setex(cache_key, 600, json.dumps(data))