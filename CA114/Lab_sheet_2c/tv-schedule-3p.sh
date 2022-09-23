#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/bbc1.txt" |
  grep -w News |
  grep -w -v 'Got News'
