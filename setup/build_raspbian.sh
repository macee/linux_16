#!/bin/sh

umount /dev/mmcblk0p1
umount /dev/mmcblk0p2

dd bs=4M if=2016-05-27-raspbian-jessie.img of=/dev/mmcblk0
