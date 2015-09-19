# team-hd.ru standard routines file

# import section
from fabric.api import *

def prepare_deploy():
	print("Clean public folder")
	local("rm -rf ./public/*")
	local("hugo -t teamhd2")

def tar_site():
	with lcd("public"):
		local('tar cvzf ../../team-hd.hugo.tar.gz .')

def send_xserve():
	put("../team-hd.hugo.tar.gz", "~/")

def unpak_xserve():
	with cd("/var/www/team-hd.ru/public_html"):
		sudo("rm -rf *")
		sudo("tar xvzf ~/team-hd.hugo.tar.gz")
		sudo("chown -R www-data:root *")


# deploy site to test server
def deploy_xserve():
	prepare_deploy()
	tar_site()
	send_xserve()
	unpak_xserve()

# deploy to main server
def deploy():
	prepare_deploy()
	with lcd("public"):
		local('git add --all .')
		local('git commit -m "Site update"')
		local('git push')
