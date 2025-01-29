from response import Response
from middleware import loggingMiddlewareFactory

def home(req):
    with open("templates/index.html") as f:
        body = f.read()
        return Response(
            version=req.version,
            code=200,
            reason="Ok",
            headers={},
            body=body
        )


def about(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="<h1>I am on the about page!<a href='/profile'>Go to profile</a></h1>",
    )
