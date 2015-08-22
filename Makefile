# Ian Dennis Miller
# nexus5-root

SHELL=/bin/bash

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

.PHONY: clean install
