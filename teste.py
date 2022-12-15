from flask import Flask

app = Flask (__name__)



@app.route("/")
def hello ():
    return "eaeeee"

@app.route("/data")
def pares():
    return{"nome": "gege", "estado": "BA"}

@app.route("/cumprimentar/<string:nome>")
def cumprimentar (nome):
    return f"oiee, {nome}"

if __name__ =="__main__":
    app.run(debug=True)