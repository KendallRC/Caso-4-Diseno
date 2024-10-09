from prometheus_client import Counter, Histogram, start_http_server
import time

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'Request Latency', ['endpoint'])

class PrometheusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        start_http_server(8001)
        print("Prometheus metrics server started on port 8001")  # Agregar print para verificar

    def __call__(self, request):
        method = request.method
        endpoint = request.path
        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
        
        start_time = time.time()
        response = self.get_response(request)
        resp_time = time.time() - start_time
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(resp_time)

        return response
