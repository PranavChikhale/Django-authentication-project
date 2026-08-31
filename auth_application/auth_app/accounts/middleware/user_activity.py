class UserActivityMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            print(f"Logged-in User: {request.user.username}")
        else:
            print("Anonymous User")

        response = self.get_response(request)

        return response