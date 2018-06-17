#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    for i in fs.keys():
        print i + ": " + str(fs.getvalue(i))

go()
