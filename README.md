# python-flask-api

This application is an API example built using Python 3 and Flask. It has a MySQL DB as a Data Provider.

## Before you start

- Make sure you have the MySQL Server 5.5 instance running on your local machine.
 - You can do it using a standard MySQL server installation or using Docker. e.g. **docker run -d --name mysql --network host -e MYSQL_ROOT_PASSWORD=python mysql:5.5**

- Make sure you have MySQL DB Connector installed
 - You can do it using **pip3 install mysql-connector-python**

- Create the "company" database schema
 - A SQL script example can be found at **resources/db/V1__create-database-company-schema.sql**

- Create the "employee" table
 - A SQL script example can be found at **resources/db/V2__create-table-employee.sql**

 - Insert some rows at "employee" table
 - A SQL script example can be found at **resources/db/V3__insert-employees.sql**

## Running the application

You can run the application using the command in CLI: **python3 api.py**

## Consuming the API

You can get instructions accessing the root endpoint: **http://localhost:5000**