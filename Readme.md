# nexus-root

Root your nexus.  This installs a specific version of the nexus roms.  Currently supported out of the box are:

- Nexus 5 (nexus5.conf)
- Nexus 6 (nexus6.conf)

## quickstart

If you are starting with a stock phone and you've already backed up the sdcard, then just jump right in.  First, edit the Makefile to use the correct configuration file for your device.

    make download unlock flash root

This will do the following:

- download a system image
- download a custom recovery (TWRP)
- unlock the bootloader (and wipe the sdcard)
- flash the system image
- flash the custom recovery (which roots the device)

## verify the configuration

Everything is controlled by nexus5.conf, which points to:

- the Android image to download
- the URL for Team Win Recovery Project (TWRP)

Find the image download link here: https://developers.google.com/android/nexus/images

In order to target a different phone, update the configuration accordingly.

## command details

### install requirements (Android SDK)

If the Android SDK is not already installed, then install it here.

    make requirements

### download the images

    make download

### back up user data

First, use a program like Titaniam Backup or MyBackup to create a backup of your user data.  Then, run the following command to copy that backup to your laptop.

    make backup

### unlock the phone

This step will wipe all user data, so ensure you have a backup first.

    make unlock

### flash the new rom

This will install a new bootloader image, radio image, and a new system image.

    make flash

After this step is completed, enable developer mode so that further USB debugging is possible.

- get into your phone's settings menu
- in "About Phone" locate Build Number at bottom of screen
- Tap "Build Number" 5 times
- Developer Options:
    - check "USB Debugging" box

### custom recovery and root

Now, boot into the custom recovery.

    make root

Select "reboot" and then "system".  When you are prompted to install SuperSU, choose "yes" to install it.