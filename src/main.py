from flask import Flask
from .controllers.routers import router
from .models.Users import *
from .extensions.extension import db
from flask_migrate import Migrate

migrate = Migrate()

def create_app(create_table=False):
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.register_blueprint(router)
    db.init_app(app)
    migrate.init_app(app,db)
    app.app_context().push()
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    if create_table:
        db.create_all() 
    return app 

create_app()