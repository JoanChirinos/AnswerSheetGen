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
        qnum = 50
        
    cnum = int(fs.getvalue('options'))

    testname = fs.getvalue('testName', 'Your Test')
    if testname.strip() == '':
        testName = 'YourTest'
    #cnum = 4

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
              <body><form action="gradeSheet.py" method="post"><div class="container text-center">

              """, """
                </div></form>
                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
              </body>
            </html>"""]
    toWrite = '<div class="sm-space"></div>\n<div class="row"><div class="col-sm"><h1>' + testname + '</h1></div></div>\n\n'
    toWrite += '<div class="md-space"></div>\n'
    for q in range(1, qnum + 1):
        if (q % 3 == 1):
            toWrite += '<div class="row">\n'

        toWrite += '<div class="col-sm-4">' + str(q) + '<br/><div class="btn-group btn-group-toggle" data-toggle="buttons">\n'
        for i in range(1, cnum + 1):
            toWrite += '<label class="btn btn-secondary"><input required type="radio" name="' + str(q) + '" value="' + str(i) + '" autocomplete="off" checked>' + str(i) + '</label>\n'
        toWrite += '</div></div>\n\n\n<div class="lg-space"></div>\n\n\n'
        
        if (q % 3 == 0 or q == qnum):
            toWrite += '</div>\n'
    toWrite += '\n\n\n<div class="lg-space"></div>\n\n\n<div class="row text-center">\n<div class="col"><input class="btn btn-success btn-lg btn-block" type="submit" value="Submit"></div></div>'

    print body[0] + toWrite + body[1]

go()











    
