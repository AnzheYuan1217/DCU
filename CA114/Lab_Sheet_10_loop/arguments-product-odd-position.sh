#!/bin/sh

tem=1
flag=0
n=$#
for i in "$@"
do
 #echo $(( n / 2 ))
 flag=$(($flag+1))
 if test $flag -le $(( n/2 + n%2 ))
  then
   result=$(($1*$tem))
   tem=$result
 fi

 if [ "$#" -gt 1 ]
  then
    shift 2
  fi

done
echo $result
