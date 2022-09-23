#!/bin/sh

for a in "$@"
do
   echo "$a"
done | sort > sorted.txt
