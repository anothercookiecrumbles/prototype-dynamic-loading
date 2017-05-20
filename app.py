import importlib.machinery
import json

from flask import Flask, request

from validator import validate

app=Flask(__name__, static_url_path='')
app.secret_key = "secret key"

#Route to load functions dynamically
@app.route('/load/<function>')
def load(function):
  print("In load.")
  filename = function + ".py"
  validated = validate(filename)
  if validated:
    validate(filename)
    temp = importlib.machinery.SourceFileLoader(filename, filename).load_module()
    globals().update(temp.__dict__)
    return "Loaded {}.".format(function)
  else:
    return validated

@app.route('/add', methods=["GET"])
def add():
  a = Add()
  print(request.args)
  calculated = a.calculate(request.args.get('a'), request.args.get('b'))
  return json.dumps({"calculated" : str(calculated)})

@app.route('/subtract', methods=["GET"])
def subtract():
  a = Subtract()
  print(request.args)
  calculated = a.calculate(request.args.get('a'), request.args.get('b'))
  return json.dumps({"calculated" : str(calculated)})
