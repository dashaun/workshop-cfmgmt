import yaml
import os
import string
import random

# uaa file
# uaa:
# - target: uaa.sys.us-central1.gcp.dashaun.cloud
#   user_id: <user_id>
#   secret: <client_secret>

#  users file
# users:
# - username: <username>
#   email: <email>

def randomPassword(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

with open(r'uaa.yml') as file:
    uaas = yaml.full_load(file)
    for item, uaa in uaas.items():
    	for target in uaa:
    		os.system("cf api " + target["target"])
    		os.system("cf login -u " + target["user_id"] + " -p " + target["secret"] + " -o system")
	    # load users
	        with open(r'users.yml') as users_file:
	    		users = yaml.full_load(users_file)
	    		for item, users in users.items():
	    		   for user in users:
	    		   	    os.system("cf create-user " + user["email"] + " " + randomPassword())
	    		   	    os.system("cf-mgmt-config space --org workshop --space " + user["username"])