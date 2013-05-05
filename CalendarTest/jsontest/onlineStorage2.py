'''
Created on May 5, 2013

@author: twc2429
'''
import json
import gitshelve


json_data=open('UserDatabase.json')
userData=json.load(json_data)
#userData=json.dumps(userData, ensure_ascii=False)
print(userData)
userData=userData


userData['Users'].append({"username":"123", "userpassword":"123",
                                       "googleid":"123", "googlepass":"123",
                                       "grouplist":[]})
        
with open('UserDatabase.json', 'w') as outfile:
    outfile.write(json.dumps(userData, sort_keys=True, indent=2))
gitoutfile=gitshelve.open('UserDatabase.json', 'w')
#gitoutfile.commit()
gitoutfile.sync()
