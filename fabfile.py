# -*- coding: utf-8 -*-
# nexus5-root (c) Ian Dennis Miller

from fabric.api import task, env
import shutil
import requests
import os.path
import time
from subprocess import call

adb_cmd = os.path.join(env.sdk_path, "platform-tools", "adb")
fastboot_cmd = os.path.join(env.sdk_path, "platform-tools", "fastboot")


def download_url(source_url, destination_filename):
    if not os.path.isfile(destination_filename):
        print("downloading {0}...".format(source_url))
        r = requests.get(source_url, stream=True, headers={'referer': source_url})
        if r.status_code == 200:
            with open(destination_filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print("image downloaded to {0}".format(destination_filename))
    else:
        print("already downloaded as {0}".format(destination_filename))


@task
def download_sdk():
    "download the Android SDK"
    download_url(env.sdk_url, os.path.join(env.destination_path, "sdk.tgz"))
    call(["tar", "-xvzf", os.path.join(env.destination_path, "sdk.tgz"),
        "-C", env.sdk_path])


@task
def download_twrp():
    "download TWRP"
    download_url(env.bootloader_url, os.path.join(env.destination_path, "twrp.img"))


@task
def download_nexus_image():
    "download the stock Nexus image"
    download_url(env.image_url, os.path.join(env.destination_path, "nexus-image.tgz"))
    call(["tar", "-xvzf", os.path.join(env.destination_path, "nexus-image.tgz"),
        "-C", env.destination_path])


@task
def download_autoroot():
    "download CF-autoroot"
    download_url(env.autoroot_url, os.path.join(env.destination_path, "cf-autoroot.zip"))
    call(["unzip", os.path.join(env.destination_path, "cf-autoroot.zip"),
        "-d", os.path.join(env.destination_path, "cf-autoroot")])


@task
def bootloader():
    "reboot the phone into the bootloader"
    call([fastboot_cmd, "reboot-bootloader"])


@task
def reboot():
    "reboot the phone"
    call([fastboot_cmd, "reboot"])


@task
def unlock():
    "unlock the phone's bootloader.  NB: This step will wipe all user data."
    call([fastboot_cmd, "oem", "unlock"])
    raw_input('Press ENTER after you have unlocked the bootloader.')
    reboot()


@task
def backup():
    "copy backup from phone to local system"
    call([adb_cmd, "reboot", "pull", env.remote_backup_path, env.local_backup_path])


@task
def restore():
    "restore backup from local system to phone"
    call([adb_cmd, "reboot", "push", env.local_backup_path, env.remote_backup_path])


@task
def flash_bootloader():
    "flash the stock bootloader"
    call([
        fastboot_cmd, "flash", "bootloader",
        os.path.join(
            env.destination_path,
            env.image_base,
            "bootloader-*.img")
    ])
    bootloader()
    time.sleep(5)


@task
def flash_radio():
    "flash the radio image"
    call([
        fastboot_cmd, "flash", "radio",
        os.path.join(
            env.destination_path,
            env.image_base,
            "radio-*.img")
    ])
    bootloader()
    time.sleep(5)


@task
def flash_image():
    "flash the nexus image"
    call([
        fastboot_cmd, "-w", "update",
        os.path.join(
            env.destination_path,
            env.image_base,
            "image-*.zip")
    ])


@task
def flash_autoroot():
    "flash CF-auto-root"
    bootloader()
    time.sleep(5)
    call([
        fastboot_cmd, "-w", "update",
        os.path.join(
            env.destination_path,
            "cf-autoroot",
            "image",
            "CF-*.img")
    ])
