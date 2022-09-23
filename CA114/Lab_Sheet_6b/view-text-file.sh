#!/bin/sh

base="$1"

if test -f "$base.ascii"
then
   cat "$base.ascii"
elif test -f "$base.txt"
then
   cat "$base.txt"
elif test -f "$base.html"
then
   cat "$base.html"
else
   false
fi
