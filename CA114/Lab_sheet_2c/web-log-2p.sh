#!/bin/sh

wget -q -O - "https://www.activepeers.com/files/weblogs.txt" |
	grep "10.131.2.1" |
	grep "login.php" |
	wc -l
