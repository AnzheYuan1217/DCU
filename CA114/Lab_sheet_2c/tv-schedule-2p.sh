#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/bbc1.txt" |
  grep 'Live With Lucy Hockings'
