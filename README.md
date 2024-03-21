# recipe-app 
This is my first public app which I still work on. This is mainly my playground. This app should store some recipes which can be used by the whole family.

## backend
The backend is build with python. It consists of three layer:
  - api_controller: It communicates with the db controller and it's the interface for the frontend.
  - db_controller: It's the middle layer. The db_controller communicates with with the api and db_connector. Firstly, the sql-query will be defined and secondly the data will be prepared here.
  - db_connection: This is the db-connector which will fetch the data from the mysql-db.

Also, you will find some utilities which supports the backend.

## frontend
The frontend is build with vue.js and just follows an easy design.
