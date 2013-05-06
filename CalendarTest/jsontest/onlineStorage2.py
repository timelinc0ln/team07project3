'''
Created on May 5, 2013

@author: twc2429
'''
import json
import gitshelve


with open('UserDatabase.json', "r") as f:
    userData = json.loads(f.read())
  
#json_data=open('UserDatabase.json')
#userData=json.load(json_data)
#userData=json.dumps(userData, ensure_ascii=False)
print(userData)
userData=userData


userData['Users'].append({"username":"123", "userpassword":"123",
                                       "googleid":"123", "googlepass":"123",
                                       "grouplist":[]})
        
with open('UserDatabase.json', 'w') as outfile:
    outfile.write(json.dumps(userData, sort_keys=True, indent=2))

#data = gitshelve.open(repository = '/team07project3/CalendarTest/jsontest')
#data['/team07project3/CalendarTest/jsontest/UserDatabase.json']="something"
#data.sync()

gitoutfile=gitshelve.open('test')
gitoutfile['C:/Users/twc2429/Downloads/team07project3/CalendarTest/jsontest/UserDatabase.json']="Hi"
print("TESTING", gitoutfile)
gitoutfile.sync()
gitoutfile.close()
#gitoutfile.commit("commit testing")