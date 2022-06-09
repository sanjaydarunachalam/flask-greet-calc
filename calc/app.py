# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.route("/add")
def func_add():
    """adds A + B"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    ans= add(a,b)

    return str(ans)


@app.route("/sub")
def func_sub():
    """subtract A - B"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    ans= sub(a,b)

    return str(ans)


@app.route("/mult")
def func_mult():
    """multiply A * B"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    ans= mult(a,b)

    return str(ans)


@app.route("/div")
def func_div():
    """divide A / B"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    ans= div(a,b)

    return str(ans)


