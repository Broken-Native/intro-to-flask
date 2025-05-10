# models

# name
# user_name
# dob
# email
# phone numbers
# is_active
# password
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column

# class User1(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     email: Mapped[str]

class user_account(db.Model):
    user_name = db.Column(db.String(50), unique=True, )
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50), primary_key=True)
    phone_num = db.Column(db.String(15))
    password = db.Column(db.String(220))
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.String(12))


# acct_num
# balance