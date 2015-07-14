# FlaskAPIBackend

This a basic api call based backend server using SQLite Database.

GET, POST, DELETE api calls have been implemented, Error Handling done appropriately.

Request Response is JSON from all the api calls.

run run.py to start server

Authentication required for all api calls,
username: python
password: flask


API call Documentation<br />
/userlist - get all users<br />
/userlist/<int:user-id> - get user with the given id<br />
/adduser - add user with email and nickname as mandatory and unique details<br />
/deleteuser/<int:user-id> - delete the user with the given id<br />

Example API calls:
curl -u python:flask -i http://localhost:5000/userlist<br />
curl -u python:flask -i http://localhost:5000/userlist/2<br />
curl -u python:flask -i -H "Content-Type: application/json" -X POST -d '{"nickname":"abc", "email":"xyz"}' http://localhost:5000/adduser<br />

Extensions & Libraries Used<br />
flask-SQLAlchemy<br />
flask-migrations<br />
HTTPBasicAuth<br />

To access DataBase through shell,
get into python in the same environment as app<br />
from app import db, models<br />
then, perform commands on db accordingly<br />

Description of all .py files<br />
config.py: file where the configuration of database exist<br />
db_create.py: file to create new db and migration repo<br />
db_migrate.py: stores the old db in repo and upgrades to new db<br />
db_upgrade.py: loads the latest db in repo<br />
db_downgrade.py: downgrades the db by 1 version<br /> 
run.py: Run/Start the server<br />
views.py: all api calls and uri definations here<br />
models.py: database model and structure<br />
