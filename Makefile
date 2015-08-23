# Ian Dennis Miller
# nexus5-root

SHELL=/bin/bash

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

download:
	fab -c nexus5.conf download_nexus_image
	fab -c nexus5.conf download_twrp
	fab -c nexus5.conf download_autoroot

sdk:
	fab -c nexus5.conf download_sdk

bootloader:
	fab -c nexus5.conf bootloader

unlock:
	fab -c nexus5.conf unlock

flash:
	fab -c nexus5.conf flash

backup:
	fab -c nexus5.conf backup

restore:
	fab -c nexus5.conf restore

.PHONY: clean install
