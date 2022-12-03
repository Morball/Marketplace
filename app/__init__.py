from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
from flask_migrate import Migrate
from datetime import timedelta
app=Flask(__name__)
app.config.from_pyfile("../config.py")
app.secret_key="secret"
app.permanent_session_lifetime=timedelta(seconds=3600)



from app.models.models import db

db.init_app(app)
migrate=Migrate(app,db)
limiter=Limiter(app, key_func=get_remote_address)


breadcrumbs_alias={
    "":"Home",
    "home": "Home",
    "login": "Log in",
    "register": "Register",
    "listing": "Listing",
    "user": "User",
    "create":"Create"
}





from app.views.auth import routes
from app.views.errors import routes
from app.views.home import routes
from app.views.listing import routes
from app.views.user import routes