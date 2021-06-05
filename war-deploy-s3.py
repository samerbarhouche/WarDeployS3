import os
import shutil
import time
from pick import pick


title = 'Please choose an application to deploy: '
path='/tsl/app'
instances = [ item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) ]
instance, index = pick(instances, title)
print("Deploying %s now: "%instance)

with open("instances.txt", 'r') as f:
    for line in f:                        #Iterate each line
        val = line.strip()                #Strip leading and trailing space.
        if val.startswith('%s'%instance):     #Check for value
            var1 = val.split(" ")
            fname=var1[1]   #Get folder name --> this is the Folder name on the s3 bucket
            wname=var1[2]   #Get the war name

def war_copy():
    # shutil.copyfile("/mys3bucket/Wars/%s/%s.war"%(fname,wname), "/tsl/app/%s/webapps/%s.war"%(instance,wname))
    os.system("sudo cp /mys3bucket/Wars/%s/%s.war"%(fname,wname), "/tsl/app/%s/webapps/%s.war"%(instance,wname))
    time.sleep(5)


def tomcat_restart():
    print
    os.system("sudo -u tomcat /tsl/scripts/%s.sh restart"%instance)
    print



war_copy()
tomcat_restart()