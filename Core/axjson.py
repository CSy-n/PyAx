import json



def decode_json(string):
  return json.loads(string)
  
def encode_json(json_, indent=0):
  return json.dumps(json_, indent=indent)
  
  
def stringify(pyobject, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, indent=None, separators=None, default=None, sort_keys=True):
  return json.dumps(pyobject, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, default=default, sort_keys=sort_keys)
