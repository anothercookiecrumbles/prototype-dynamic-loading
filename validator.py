from importlib import import_module
import os
import sys

#Should eventually be able to iterate through multiple validations
#and return True if all validation conditions are met and an error
#if that is not the case.
#The different validations can be standalone scripts, which allows us
#a bit more flexibility, i.e. different validators depending on the GitHub
#repo we add. But... baby steps.
def validate(filename):
  print("Validating {}".format(filename))
  #check if file exists
  try:
    script = open(filename, 'r').read() + '\n'
  except:
    return "file {} doesn't exist".format(filename)
  #check if valid python file
  try:
    compiled = compile(script, filename, 'exec')
  except:
    return "unable to compile {}".format(filename)
  #check if methods exist – here, I simply manually check if calculate
  #exists. This can be factored out/loaded via config.
  p, m = filename.rsplit(".", 1)
  imported_module = import_module(p)
  #check if function(s) we care about exist – in this case, we only need
  #to ensure that _calculate_ exists
  imported_class = getattr(imported_module, p.title())
  #use callable to distinguish between variables and functions.
  #only functions are callable
  try:
    if not callable(imported_class.calculate):
      return "function {} doesn't exist".format("calculate")
  except:
    return "{} doesn't exist in module".format("calculate")

  return True
