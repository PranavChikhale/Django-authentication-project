import time

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        start_time = time.time()
        print(f"Request: {request.method} {request.path}")

        response = self.get_response(request)
        end_time = time.time()
        duration = end_time - start_time

        print(f"Response: {response.status_code}")
        print(f"Time: {duration:.4f} seconds")
        return response