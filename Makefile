# Ian Dennis Miller
# nexus5-root

SHELL=/bin/bash
CONFIG=nexus7.conf

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

download:
	fab -c $(CONFIG) ensure_paths
	fab -c $(CONFIG) download_nexus_image
	fab -c $(CONFIG) download_twrp

requirements:
	fab -c $(CONFIG) download_sdk

bootloader:
	fab -c $(CONFIG) adb_bootloader

unlock:
	fab -c $(CONFIG) adb_bootloader
	fab -c $(CONFIG) unlock

backup:
	fab -c $(CONFIG) backup

restore:
	fab -c $(CONFIG) restore

flash:
	fab -c $(CONFIG) fastboot_bootloader
	fab -c $(CONFIG) flash_bootloader
	fab -c $(CONFIG) flash_radio
	fab -c $(CONFIG) flash_image

root:
	fab -c $(CONFIG) adb_bootloader
	fab -c $(CONFIG) flash_recovery

.PHONY: clean install download sdk bootloader unlock backup restore flash root
