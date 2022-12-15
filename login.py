from dataclasses import dataclass
from flask import Flask, abort, request, render_template 
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user
)

from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
app = Flask (__name__)
login_manager.init_app(app)

app.config["SECRET_KEY"] = "secret"
 
@dataclass
class User:
   username: str
   password: str
   is_active: bool = True
   is_anonymous: bool = False
   is_authenticated: bool = True
 
   def get_id(self):
       return self.username

from werkzeug.security import generate_password_hash, check_password_hash
 
database = {}
 
@app.route("/user", methods=["POST"])
def create_user():
   data = request.json
   data["password"] = generate_password_hash(data["password"])
   return f"olá, {data['username']}"

@app.route("/user/<string:name>", methods=["GET"])
def read_user(name):
   if name not in database:
       abort(404)
 
   data = database[name]
   data["nome"] = name
   return data

@app.route("/login", methods=["GET", "POST"])
def login():
   if request.method == "GET":
       return """
              <form action='login' method='POST'>
               <input type='text' name='username' id='username' placeholder='username'/>
               <input type='password' name='password' id='password' placeholder='password'/>
               <input type='submit' name='submit'/>
              </form>
              """
   username = request.form.get("username")
   user = database.get(username)
 
   if user and check_password_hash(user.password, request.form.get("password")):
       login_user(user)
       return "Login com sucesso!"
   else:
       return "Login falhou"

@login_required
@app.route("/user/<string:name>", methods=["GET"])
def read_user(name):
   if not current_user.is_authenticated or current_user.username != name:
       abort(403)
   if name not in database:
       abort(404)
 
   data = database[name]
   return f"Olá, {data.username}"


if __name__ =="__main__":
    app.run(debug=True)

