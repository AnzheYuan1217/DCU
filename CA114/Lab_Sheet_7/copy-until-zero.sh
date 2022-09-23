#!/bin/sh

while read line && ! test "$line" = "0"
do
   echo $line
done
