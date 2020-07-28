#!/bin/bash
a=`sqlite3 ~/.secret.db3 'select secret from pass where app = "DJANGO01"'`

