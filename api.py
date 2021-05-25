import flask
from flask import request, jsonify

import mysql.connector

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# MySQL
employeeDb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python",
  database="company"
)

@app.route('/', methods=['GET'])
def home():
  return "<h1>Hello Flask API!</h1><h3>To retrieve DB Data try /api/v1/employee/all </h3>"

@app.route('/api/v1/employee/all', methods=['GET'])
def employee_all():
  results = []

  employeeCursor = employeeDb.cursor()
  employeeCursor.execute("SELECT * FROM employee")

  mysqlRes = employeeCursor.fetchall()

  for e in mysqlRes:
    results.append(e)

  return jsonify(results)

@app.route('/api/v1/employee', methods=['GET'])
def employee_code():
  if 'code' in request.args:
    code = int(request.args['code'])
  else:
    return "Error: No CODE field provided. Please specify it using ?code=desiredEmployeeCode"
  
  results = []

  employeeCursor = employeeDb.cursor()
  employeeCursor.execute("%s%d" % ("SELECT * FROM employee WHERE code = ", code))

  mysqlRes = employeeCursor.fetchall()

  for e in mysqlRes:
    results.append(e)

  return jsonify(results)


app.run()