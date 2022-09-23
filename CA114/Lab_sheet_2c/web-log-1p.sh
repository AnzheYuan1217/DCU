#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/weblogs.txt" |
  grep 'compiler.php'
