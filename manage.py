import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import *




# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/melexia_web"

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()