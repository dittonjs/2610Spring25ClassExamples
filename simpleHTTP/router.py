from response import Response
from endpoints import home, about

def router(request):
    if request.uri == "/":
        return home(request)
    elif request.uri == "/about":
        return about(request)
    else:
        return Response(
            code=404,
            reason="Not Found",
            version=request.version,
            headers={},
            body="",
        )


