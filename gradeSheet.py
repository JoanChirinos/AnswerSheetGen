#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

print 'Content-type: text/html\n\n'

def go():

    body = ["""
<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="author" content="Joan Chirinos">
      

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        
        <link rel="stylesheet" type="text/css" href="style.css">

        <title>Answer Sheet Generator</title>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col">
                    <h1>Your responses</h1>
                </div>
            </div>""", """
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
        <script>
            function updateFromRange() {
                var val = document.getElementById("numberOfQuestions").value;
                document.getElementById("questionDisplay").value = val + "";
            }
            function updateFromDisplay() {
                var val = document.getElementById("questionDisplay").value;
                console.log(val);
                document.getElementById("numberOfQuestions").value = val + "";
            }
        </script>
    </body>
</html>"""]

    toWrite = ""
    
    fs = cgi.FieldStorage()
    corrects = fs.getvalue('correctAnswers')
    qnum = fs.getvalue('qnum', str(len(fs.keys()) - 2))
    for q in range(1, int(qnum) + 1):
        try:
            toWrite += ans(q, fs.getvalue(str(q)), correct[q - 1])
        except:
            toWrite += ans(q, 'error', 'something went wrong here')
    print body[0] + toWrite + body[1]
        
def ans(num, choice, correct):
    if (str(choice) == str(correct)):
        return '<div class="row"><div class="col">' + str(num) + ': <span style="color: green;">' + str(choice) + '</span></div></div>'
    return '<div class="row"><div class="col">' + str(num) + ': <span style="color: red;"><i>' + str(choice) + '</i></span>&nbsp;&nbsp;&nbsp;<span style="color: green;"><i>' + str(correct) + '</i></span></div></div>'

go()











