# email
# user_name
# password
# phone_number

from . import bp
from flask import render_template, request, flash, url_for, redirect
from flask_app.database import models, helpers
from werkzeug.security import generate_password_hash
import time


@bp.route("/sign_up", methods = ["get", "post"])
def sign_up():
    if request.method == 'POST':
        today = time.localtime()
        data = dict(request.form.copy())

        hashed_password = generate_password_hash(data.get("password"))

        data.update(password=hashed_password)
        data.update(last_login = time.strftime('%d-%m-%Y', today))

        helpers.create_record(models.user_account, **data)
        flash("account created", "info")
        return redirect(url_for("auth.sign_in"))
        
    return render_template("sign-up.html")