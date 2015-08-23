# nexus5-root

Root your nexus 5.  This installs a specific version of the nexus5 roms.

## verify the configuration

Everything is controlled by nexus5.conf, which points to:

- the Android image to download
- the URL for Team Win Recovery Project (TWRP)

Find the image download link here: https://developers.google.com/android/nexus/images

## download the image

    make download

## unlock the phone

    make unlock

## enter the bootloader

    make bootloader

## flash the new rom

    make flash
