#!/usr/bin/env bash

### Remove useless dependencies in Arch Linux Only ###

if [ $(id -u) -eq 0 ] and [ -x /usr/bin/pacman ]
then
    pacman -R $(pacman -Qdt | sed 's/\ .*//')
fi
