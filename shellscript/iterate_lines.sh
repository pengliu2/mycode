#!/bin/sh

while read line; do
    adb -s $1 pull /vendor/bin/${line}
done < $2
