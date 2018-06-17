#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    for i in fs.keys():
        print "<h1>" + i + ": " + str(fs.getvalue(i)) + "</h1><br>"

go()
