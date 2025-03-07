is_logged_in = True

def session_middleware(next):
    def middleware(req):
        global is_logged_in
        if is_logged_in:
            next(req)
        else:
            print("you are not logged in")

    return middleware


@session_middleware
def login(req):
    print("You are in the login endpoint")

decorated_login = session_middleware(login)


if __name__ == "__main__":
    login("req")
