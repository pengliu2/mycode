#!/bin/sh

count=$1
command=$2

for run in $(seq $count); do
    $command
    sleep 1
done

