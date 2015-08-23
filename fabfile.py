# -*- coding: utf-8 -*-
# nexus5-root (c) Ian Dennis Miller

from fabric.api import task
import shutil
import requests
import os.path
from subprocess import call

platform_tools = "/Users/idm/Library/Code/android-sdk-macosx/platform-tools"
adb_cmd = os.path.join(platform_tools, "adb")
fastboot_cmd = os.path.join(platform_tools, "fastboot")

# https://developers.google.com/android/nexus/images
base_url = "https://dl.google.com/dl/android/aosp"
destination_path = "/tmp"

image_filename = "hammerhead-lmy48i-factory-a38c3441.tgz"  # 5.1.1-rev2
image_base = "hammerhead-lmy48i"


@task
def download():
    "download image"

    destination_filename = "{0}/{1}".format(destination_path, image_filename)
    source_url = "{0}/{1}".format(base_url, image_filename)

    if not os.path.isfile(destination_filename):
        print("downloading {0}...".format(source_url))
        r = requests.get(source_url, stream=True)
        if r.status_code == 200:
            with open(destination_filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print("image downloaded to {0}".format(destination_filename))
    else:
        print("already downloaded image")


@task
def extract():
    destination_filename = "{0}/{1}".format(destination_path, image_filename)
    call(["tar", "-xvzf", destination_filename, "-C", destination_path])


@task
def bootloader():
    call([adb_cmd, "reboot", "bootloader"])


@task
def unlock():
    call([fastboot_cmd, "oem", "unlock"])


@task
def flash():
    call([
        fastboot_cmd,
        "flash",
        "bootloader",
        os.path.join(
            destination_path,
            image_base,
            "bootloader-*.img")
    ])

    """fastboot flash bootloader bootloader.img
    fastboot reboot-bootloader
    fastboot flash radio radio.img
    fastboot reboot-bootloader
    fastboot flash system system.img
    fastboot flash boot boot.img
    fastboot flash recovery recovery.img
    fastboot flash cache cache.img"""
