# Ian Dennis Miller
# nexus5-root

SHELL=/bin/bash

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

download:
	fab -c nexus5.conf download
	fab -c nexus5.conf extract

bootloader:
	fab -c nexus5.conf bootloader

unlock:
	fab -c nexus5.conf unlock

flash:
	fab -c nexus5.conf flash

.PHONY: clean install
