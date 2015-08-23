# Ian Dennis Miller
# nexus5-root

SHELL=/bin/bash
CONFIG=nexus5.conf

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

download:
	fab -c $CONFIG download_nexus_image
	fab -c $CONFIG download_twrp
	fab -c $CONFIG download_autoroot

requirements:
	fab -c $CONFIG download_sdk

unlock:
	fab -c $CONFIG unlock

backup:
	fab -c $CONFIG backup

restore:
	fab -c $CONFIG restore

flash:
	fab -c $CONFIG flash_bootloader
	fab -c $CONFIG flash_radio
	fab -c $CONFIG flash_image
	fab -c $CONFIG flash_autoroot

.PHONY: clean install download sdk bootloader unlock backup restore flash
