def cookie_logger_middleware(next):
    """
    Middleware to log cookies in the request and response.
    """
    def middleware(request):
        # Log request cookies
        print("Request Cookies:", request.COOKIES)

        # Call the next middleware or view
        response = next(request)

        # Log response cookies
        print("Response Cookies:", response.cookies)

        return response

    return middleware