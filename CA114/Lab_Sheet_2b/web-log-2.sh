#!/bin/sh

# Fetch the web log data, and store it in a file.
wget -q -O - "https://www.activepeers.com/files/weblogs.txt" > ca114-log.txt

# Filter out all lines except those pertaining to ip "10.131.2.1".
grep "10.131.2.1" ca114-log.txt > user-1013121.txt

# Of the remaining lines, keep only those which are uploads.
grep "login.php" user-1013121.txt > user-1013121-login.txt

# And count the remaining lines.
wc -l < user-1013121-login.txt
