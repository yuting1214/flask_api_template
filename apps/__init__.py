import os
import pathlib
import connexion
from connexion.resolver import RelativeResolver
from apps.config import db, ma
from db.operations import create_database, update_database, get_data_from_table
from api.models import Note, Person

def configure_database(app):

    @app.before_request
    def initialize_database():
        try:
            existing_people = get_data_from_table(Person)
            if not existing_people:
                create_database(db)

        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e) )

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    basedir = config.basedir
    connex_app = connexion.App(__name__, specification_dir=basedir)
    connex_app.app.config.from_object(config)
    connex_app.add_api(basedir / "swagger.yml", resolver=RelativeResolver('api'))
    # Link the services
    db.init_app(connex_app.app)
    ma.init_app(connex_app.app)
    # Initialize the database
    configure_database(connex_app.app)
    return connex_app
