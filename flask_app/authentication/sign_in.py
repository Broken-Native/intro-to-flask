from . import bp
from flask import render_template, request, jsonify, session
from flask_app.database import helpers
from flask_app.database.models import user_account 
from werkzeug.security import check_password_hash
from flask_login import login_user


@bp.route("/sign_in", methods = ["get", "post"])
def sign_in():
   if request.method == 'POST':
      data = request.form.copy()
      user = helpers.get_record(
           user_account, data.get("email")
         )
      if not user:
         # no user record is found
         # meaning the account has not been created
         return jsonify(message = "no user account found")
      
      # if password hash dosen't match line 17 is triggered
      if not check_password_hash(user.password, data.get("password")):
         return jsonify(message = "invalid user_name or password")
       
      # if password hash matched 
      login_user(user)
      return jsonify(message = "loggin successful")
   
   # on get request
   return render_template("sign-in.html")