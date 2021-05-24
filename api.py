import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


fakeDbData = [
  {
    'id': 1,
    'code': 1312,
    'name': 'Rodrigo Donizetti'
  },
  {
    'id': 2,
    'code': 1313,
    'name': 'Rodrigo Vimieiro'
  },
]

@app.route('/', methods=['GET'])
def home():
  return "<h1>Hello Flask API!</h1><h3>To retrieve DB Data try /api/v1/employee/all </h3>"

@app.route('/api/v1/employee/all', methods=['GET'])
def employee_all():
  return jsonify(fakeDbData)

@app.route('/api/v1/employee', methods=['GET'])
def employee_code():
  if 'code' in request.args:
    code = int(request.args['code'])
  else:
    return "Error: No CODE field provided. Please specify it using ?code=desiredEmployeeCode"
  
  results = []

  for employee in fakeDbData:
    if employee['code'] == code:
      results.append(employee)

  return jsonify(results)


app.run()