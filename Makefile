install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/hello_world.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-hello-world
	rm /etc/wazo-admin-ui/conf.d/hello_world.yml
	systemctl restart wazo-admin-ui
