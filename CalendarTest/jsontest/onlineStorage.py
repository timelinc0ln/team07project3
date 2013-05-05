import urllib2
import json
import gitshelve



req = urllib2.Request("https://raw.github.com/timelinc0ln/team07project3/master/CalendarTest/CalendarReader/GroupDatabase.json", None, {'user-agent':'syncstream/vimeo'})
opener = urllib2.build_opener()
f = opener.open(req)
json_data=json.load(f)
print(json_data)
print("\n\n\n")

json_data['Groups'].append({"groupName":"123", "dateCreated":"123",
                                          "calendarId":"123", "password":"123", 
                                          "members":[{"name":"123"}]})
f.write(json.dumps(json_data, sort_keys=True, indent=2))
f.sync()




url = "https://raw.github.com/timelinc0ln/team07project3/master/CalendarTest/CalendarReader/GroupDatabase.json"
json = urllib2.urlopen(url).read()

# convert to a native python object
(true,false,null) = (True,False,None)
profiles = eval(json)
print("\n\n\n")
print(profiles)

#data = gitshelve.open(repository = '/timelinc0ln/team07project3/blob/master/CalendarTest/CalendarReader/GroupDatabase.json')
#print(data)


