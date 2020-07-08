#!/bin/bash
cp my-httpd.conf /usr/local/apache2/conf
rm /usr/local/apache2/htdocs/index.html
cp /home/code/Templates/index.html /usr/local/apache2/htdocs
python3 /home/code/src/http-file-server.py