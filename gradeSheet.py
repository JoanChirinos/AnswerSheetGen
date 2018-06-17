#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    print 'yo'

go():
