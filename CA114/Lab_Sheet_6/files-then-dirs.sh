#!/bin/sh

for f in "$@"
do
   if test -f "$f"
   then
      echo "$f"
   fi
done

for f in "$@"
do
   if test -d "$f"
   then
      echo "$f"
   fi
done
