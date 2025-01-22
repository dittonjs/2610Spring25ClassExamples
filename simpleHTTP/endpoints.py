from response import Response

def home(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="<h1>I am on the home page!<a href='/about'>Go to about</a></h1>",
    )

def about(req):
    return Response(
        version=req.version,
        code=200,
        reason="Ok",
        headers={},
        body="<h1>I am on the about page!<a href='/profile'>Go to profile</a></h1>",
    )
