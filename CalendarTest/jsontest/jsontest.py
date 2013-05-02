import json


json_data = open('records')
data = json.load(json_data)

print data

#for colorsArray in data['colorsArray']: 
#    print colorsArray['colorName'], colorsArray['hexValue']
    
#print data["colorsArray"][2]["colorName"]
#for colorsArray in data['colorsArray']: 
#    print colorsArray['colorName']
#print data["colorsArray"] 

print data["records"]

print data["table"]

print "\n\n\n"
for records in data['records']:
#    records['email'] = '/view?email=%s' % (records['phone'])
     records['email'] = 'project3team07@gmail.com'

data['records'].append({"name":"Bob", "phone":"999-999-9999", "email":"osdiuhg"})
print data['records']
#data['records'][0]['name'] = 'William'



json_data.close()


with open('records', 'w') as outfile:
  json.dump(data, outfile)