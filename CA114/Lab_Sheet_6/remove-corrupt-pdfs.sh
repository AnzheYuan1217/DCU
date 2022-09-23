#!/bin/sh

for f in "$@"
do
   if ! test -s "$f"
   then
      rm "$f"
   fi
done
