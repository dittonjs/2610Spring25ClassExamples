from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login(request):
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()
    res = cur.execute(f"SELECT * FROM user  WHERE email = ? AND password = ?;", (
        request.POST.get('email'), request.POST.get('password')
    ))
    # SELECT * FROM user WHERE email = '' AND password = '' OR ''='' AND email = 'thomas@example.com'; --
    user = res.fetchone()
    print(user)
    if user:
        return render(request, 'core/purchase_orders.html', {"user_name": user[0]})
    else:
        return render(request, 'core/index.html')

