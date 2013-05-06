import subprocess
import os
from subprocess import call

#git_query=subprocess.Popen( '!/bin/sh/git status', cwd = os.path.dirname('\Downloads\team07project3'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
git_query=subprocess.Popen(['git','add','onlineStorages4.py'], cwd = os.path.dirname('\Downloads\team07project3'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
pr=git_query
(out, error) = pr.communicate()
output=git_query.stdout
#print(output)
#print error


print os.getcwd()
print os.path.basename(__file__)
print os.path.abspath(__file__)
print os.path.dirname(__file__)


subprocess.Popen(["ls"], cwd = 'Z:/onlineStorageTest/git')


#p = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE)
#out, _ = p.communicate()
#repo_root = out.splitlines()[0]
#print out

#p = subprocess.Popen(['find', repo_root, '-name', 'manage.py'], stdout=subprocess.PIPE)
#out, err = p.communicate()
#print out, error
#



#cmd = ['!/bin/sh', 'status']
#pipe = subprocess.Popen(cmd, 1, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
#(out, error) = pipe.communicate()
#print out, error




(git_status, error) = git_query.communicate()
(out, error) = pr.communicate()
print out, error
print('hihihi')