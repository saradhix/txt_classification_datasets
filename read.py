import json

fp=open('reuters_8class.json','r')

for line in fp:
    json_obj=json.loads(line)
    print json_obj['sentence']
