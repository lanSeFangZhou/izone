from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from v1.models import *
app = create_app('dev')
db.create_all(app=app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
