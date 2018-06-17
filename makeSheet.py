#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    qnum = fs.getvalue('numberOfQuestions')
    try:
        qnum = int(qnum)
        if qnum < 1:
            qnum = 1
        elif qnum > 200:
            qnum = 200
    except:
        qnum = 100
        
    cnum = int(fs.getvalue('choices'))

    body = ["""<!doctype html>
            <html lang="en">
              <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <meta name="author" content="Joan Chirinos">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

                <title>Answer Sheet Generator</title>
                <link rel="stylesheet" type="text/css" href="style.css">
              </head>
              <body>

              """, """

                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
              </body>
            </html>"""]
    toWrite = ""
    for q in range(1, qnum + 1):
        











    
