#!/bin/bash
a=`sqlite3 /var/.secret.db3 'select secret from pass where app = "DJANGO01"'`
echo $a

