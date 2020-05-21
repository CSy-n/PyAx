#https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


import json
"""
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
   """     
        
        
def write_text(fp, text):
  with open(fp, 'w') as outfile:
    outfile.write(text)
    

        
def write_json(fp, text):
  with open(fp, 'w') as outfile:
    json.dump(text.json(), outfile, indent=2) 
