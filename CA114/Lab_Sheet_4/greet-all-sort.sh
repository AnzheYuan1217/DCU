#!/bin/sh

for a in "$@"
do
   echo "Hello $a."
done | sort
