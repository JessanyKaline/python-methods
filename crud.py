from flask import Flask
from flask import request 
from flask import abort

app = Flask (__name__)

@app.route("/echo", methods=["POST"])
def hello():
    print(request.data)
    return "oláááá"

database = {}
 
@app.route("/user", methods=["POST"])
def create_user():
   data = request.json
   name = data.pop("nome")
   database[name] = data
   return "olá, Tera!"

@app.route("/users", methods=["GET"])
def read_users():
 
   data = database
  
   return data



@app.route("/user/<string:name>", methods=["GET"])
def read_user(name):
   if name not in database:
       abort(404)
 
   
   data = database[name]
   data["nome"] = name
   return data

@app.route("/user/<string:name>", methods=["PUT"])
def update_user(name):
   if name not in database:
       abort(404)
 
   data = request.json
   database[name] = data
   return data

@app.route("/user/<string:name>", methods=["DELETE"])
def delete_user(name):
   if name not in database:
       abort(404)
 
   del database[name]
   return "ok", 200

if __name__=="__main__":
    app.run(debug=True)
