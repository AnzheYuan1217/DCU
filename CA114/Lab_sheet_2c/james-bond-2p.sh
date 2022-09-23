#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/james-bond.txt" |
  grep Moore |
  wc -l
