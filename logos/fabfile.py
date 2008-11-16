set(
	fab_hosts = ['192.168.2.44'],
	fab_user = 'root',

	proj_name = 'eskal.gr',
	repo = '/var/www/phaethon/bzr/logos',
	branch = '/var/www/phaethon/checkouts/logos',
)


def hello_remote():
	run('echo hello from  $(fab_hosts) to $(fab_user).')

def bzr_checkout():
	run('cd $(branch); bzr co $(repo)')

def bzr_push():
	local('bzr push sftp://%s@%s//var/www/phaethon/bzr/logos' % ('root', '192.168.2.44'))

def bzr_pull():
	run('cd $(branch); bzr pull $(repo)')

def reboot():
	run('apachectl -k graceful')

def deploy(initial=False):
	bzr_push()
	bzr_pull()
	reboot()
