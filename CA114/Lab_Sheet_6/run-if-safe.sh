#!/bin

if sha256sum -c checksum.txt | grep -q -w 'OK'
then
   sh suspicious.sh
else
   false
fi
