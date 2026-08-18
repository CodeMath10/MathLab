from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def home():
    return f"""<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{{background-color:#FFFFF5}}
h1{{font-family:"Poppins",sans-serif;font-size:4.75vw;font-weight:700;color:#FF8C00;margin:5px}}
h2{{font-family:"Poppins",sans-serif;font-size:2.89375vw;font-weight:600;color:#FF8C00;margin:0px}}
p{{font-family:"Poppins";font-size:1.25vw;color:#000028;margin:2px}}
Form{{margin-bottom:0px}}
input{{width:200px;padding:10px;margin:8px;font-size:15px;font-family:"Poppins";border:2px solid #ccc;border-radius:8px}}
button{{background-color:#FF8C00;color:white;font-family:"Poppins";font-size:1vw;padding:10px 20px;border:none;border-radius:10px;cursor:pointer;width:15vw}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card0{{flex:2.5}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.nav{{position:absolute;top:15px;right:15px}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | The Chosen Number</title>
</head>
<body>
<h1>The Chosen Number</h1>
<p>Choose almost any four-digit number. Rearrange, subtract, repeat... and see where you end up.</p>

<div class="cardrow">
<div class="card Card1">
<h2>The process</h2>
<p>The process to magic isn't very hard!<br><br><b>1. Choose a 4 digit number<br>2. Arrange its digits in 2 ways: one where they are in ascending order and one where they are in descending.<br>3. Subtract the smaller number from the bigger one<br>4. Repeat</b></p>
</div>

<div class="card Card0">
<h2>Try it out</h2>
<br><br>
<p>Enter the number below and watch as the chosen number appears</p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>
</div>

<br>

<div class="cardrow">
<div class="card Card1">
<h2>Why does this happen?</h2><br>
<p>When we rearrange and subtract the digits, lots of completely different numbers start giving the same results. For example, 3524 and 4253 both contain the same digits, so both become 5432 − 2345 = 3087. This quickly reduces thousands of possible numbers into a much smaller set of possibilities. As the process repeats, these paths eventually meet and lead to 6174.<br><br>6174 is especially interesting because it is a fixed point: arranging its digits gives 7641 and 1467, and 7641 − 1467 = 6174. So once you reach it, you're stuck there forever!</p>
</div>

<div class="card Card2">
<h2>Dr Kaprekar</h2><br>
<p>D. R. Kaprekar was an Indian mathematician who loved playing around with numbers and finding strange patterns in them.<br><br>In 1949, he discovered the strange behaviour of 6174, which is now known as Kaprekar's Constant. Surprisingly, he made many of his discoveries while working as a school teacher!</p>
<div class="la" style="margin-top:-25px"><br>
<button onclick="location.href='HOMEURL'" style="width:auto">Home</button>
<button onclick="location.href='QUIZURL'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""

@app.route("/ns",methods=["GET","POST"])
def ns():
    if request.method=="GET":
        return f"""<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{{background-color:#FFFFF5}}
h1{{font-family:"Poppins",sans-serif;font-size:4.75vw;font-weight:700;color:#FF8C00;margin:5px}}
h2{{font-family:"Poppins",sans-serif;font-size:2.89375vw;font-weight:600;color:#FF8C00;margin:0px}}
p{{font-family:"Poppins";font-size:1.25vw;color:#000028;margin:2px}}
Form{{margin-bottom:0px}}
input{{width:200px;padding:10px;margin:8px;font-size:15px;font-family:"Poppins";border:2px solid #ccc;border-radius:8px}}
button{{background-color:#FF8C00;color:white;font-family:"Poppins";font-size:1vw;padding:10px 20px;border:none;border-radius:10px;cursor:pointer;width:15vw}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card0{{flex:2.5}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.nav{{position:absolute;top:15px;right:15px}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | The Chosen Number</title>
</head>
<body>
<h1>The Chosen Number</h1>
<p>Choose almost any four-digit number. Rearrange, subtract, repeat... and see where you end up.</p>

<div class="cardrow">
<div class="card Card1">
<h2>The process</h2>
<p>The process to magic isn't very hard!<br><br><b>1. Choose a 4 digit number<br>2. Arrange its digits in 2 ways: one where they are in ascending order and one where they are in descending.<br>3. Subtract the smaller number from the bigger one<br>4. Repeat</b></p>
</div>

<div class="card Card0">
<h2>Try it out</h2>
<br><br>
<p>Enter the number below and watch as the chosen number appears</p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>
</div>

<br>

<div class="cardrow">
<div class="card Card1">
<h2>Why does this happen?</h2><br>
<p>When we rearrange and subtract the digits, lots of completely different numbers start giving the same results. For example, 3524 and 4253 both contain the same digits, so both become 5432 − 2345 = 3087. This quickly reduces thousands of possible numbers into a much smaller set of possibilities. As the process repeats, these paths eventually meet and lead to 6174.<br><br>6174 is especially interesting because it is a fixed point: arranging its digits gives 7641 and 1467, and 7641 − 1467 = 6174. So once you reach it, you're stuck there forever!</p>
</div>

<div class="card Card2">
<h2>Dr Kaprekar</h2><br>
<p>D. R. Kaprekar was an Indian mathematician who loved playing around with numbers and finding strange patterns in them.<br><br>In 1949, he discovered the strange behaviour of 6174, which is now known as Kaprekar's Constant. Surprisingly, he made many of his discoveries while working as a school teacher!</p>
<div class="la" style="margin-top:-25px"><br>
<button onclick="location.href='HOMEURL'" style="width:auto">Home</button>
<button onclick="location.href='QUIZURL'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""

    r=""
    n=int(request.form["nm"])

    if len(str(n))!=4:
        r="Invalid Number"
        return f"""<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{{background-color:#FFFFF5}}
h1{{font-family:"Poppins",sans-serif;font-size:4.75vw;font-weight:700;color:#FF8C00;margin:5px}}
h2{{font-family:"Poppins",sans-serif;font-size:2.89375vw;font-weight:600;color:#FF8C00;margin:0px}}
p{{font-family:"Poppins";font-size:1.25vw;color:#000028;margin:2px}}
Form{{margin-bottom:0px}}
input{{width:200px;padding:10px;margin:8px;font-size:15px;font-family:"Poppins";border:2px solid #ccc;border-radius:8px}}
button{{background-color:#FF8C00;color:white;font-family:"Poppins";font-size:1vw;padding:10px 20px;border:none;border-radius:10px;cursor:pointer;width:15vw}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card0{{flex:2.5}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.nav{{position:absolute;top:15px;right:15px}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | The Chosen Number</title>
</head>
<body>
<h1>The Chosen Number</h1>
<p>Choose almost any four-digit number. Rearrange, subtract, repeat... and see where you end up.</p>

<div class="cardrow">
<div class="card Card1">
<h2>The process</h2>
<p>The process to magic isn't very hard!<br><br><b>1. Choose a 4 digit number<br>2. Arrange its digits in 2 ways: one where they are in ascending order and one where they are in descending.<br>3. Subtract the smaller number from the bigger one<br>4. Repeat</b></p>
</div>

<div class="card Card0">
<h2>Try it out</h2>
<br><br>
<p>{r}</p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>
</div>

<br>

<div class="cardrow">
<div class="card Card1">
<h2>Why does this happen?</h2><br>
<p>When we rearrange and subtract the digits, lots of completely different numbers start giving the same results. For example, 3524 and 4253 both contain the same digits, so both become 5432 − 2345 = 3087. This quickly reduces thousands of possible numbers into a much smaller set of possibilities. As the process repeats, these paths eventually meet and lead to 6174.<br><br>6174 is especially interesting because it is a fixed point: arranging its digits gives 7641 and 1467, and 7641 − 1467 = 6174. So once you reach it, you're stuck there forever!</p>
</div>

<div class="card Card2">
<h2>Dr Kaprekar</h2><br>
<p>D. R. Kaprekar was an Indian mathematician who loved playing around with numbers and finding strange patterns in them.<br><br>In 1949, he discovered the strange behaviour of 6174, which is now known as Kaprekar's Constant. Surprisingly, he made many of his discoveries while working as a school teacher!</p>
<div class="la" style="margin-top:-25px"><br>
<button onclick="location.href='HOMEURL'" style="width:auto">Home</button>
<button onclick="location.href='QUIZURL'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""
    if len(set(str(n)))==1:
        r="Invalid Number"
        return f"""<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{{background-color:#FFFFF5}}
h1{{font-family:"Poppins",sans-serif;font-size:4.75vw;font-weight:700;color:#FF8C00;margin:5px}}
h2{{font-family:"Poppins",sans-serif;font-size:2.89375vw;font-weight:600;color:#FF8C00;margin:0px}}
p{{font-family:"Poppins";font-size:1.25vw;color:#000028;margin:2px}}
Form{{margin-bottom:0px}}
input{{width:200px;padding:10px;margin:8px;font-size:15px;font-family:"Poppins";border:2px solid #ccc;border-radius:8px}}
button{{background-color:#FF8C00;color:white;font-family:"Poppins";font-size:1vw;padding:10px 20px;border:none;border-radius:10px;cursor:pointer;width:15vw}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card0{{flex:2.5}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.nav{{position:absolute;top:15px;right:15px}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | The Chosen Number</title>
</head>
<body>
<h1>The Chosen Number</h1>
<p>Choose almost any four-digit number. Rearrange, subtract, repeat... and see where you end up.</p>

<div class="cardrow">
<div class="card Card1">
<h2>The process</h2>
<p>The process to magic isn't very hard!<br><br><b>1. Choose a 4 digit number<br>2. Arrange its digits in 2 ways: one where they are in ascending order and one where they are in descending.<br>3. Subtract the smaller number from the bigger one<br>4. Repeat</b></p>
</div>

<div class="card Card0">
<h2>Try it out</h2>
<br><br>
<p>{r}</p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>
</div>

<br>

<div class="cardrow">
<div class="card Card1">
<h2>Why does this happen?</h2><br>
<p>When we rearrange and subtract the digits, lots of completely different numbers start giving the same results. For example, 3524 and 4253 both contain the same digits, so both become 5432 − 2345 = 3087. This quickly reduces thousands of possible numbers into a much smaller set of possibilities. As the process repeats, these paths eventually meet and lead to 6174.<br><br>6174 is especially interesting because it is a fixed point: arranging its digits gives 7641 and 1467, and 7641 − 1467 = 6174. So once you reach it, you're stuck there forever!</p>
</div>

<div class="card Card2">
<h2>Dr Kaprekar</h2><br>
<p>D. R. Kaprekar was an Indian mathematician who loved playing around with numbers and finding strange patterns in them.<br><br>In 1949, he discovered the strange behaviour of 6174, which is now known as Kaprekar's Constant. Surprisingly, he made many of his discoveries while working as a school teacher!</p>
<div class="la" style="margin-top:-25px"><br>
<button onclick="location.href='HOMEURL'" style="width:auto">Home</button>
<button onclick="location.href='QUIZURL'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""

    while n!=6174:
        s=str(n).zfill(4)
        h=int("".join(sorted(s,reverse=True)))
        l=int("".join(sorted(s)))
        r=f"{r}{h}-{l}={h-l}→"
        n=h-l

    return f"""<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{{background-color:#FFFFF5}}
h1{{font-family:"Poppins",sans-serif;font-size:4.75vw;font-weight:700;color:#FF8C00;margin:5px}}
h2{{font-family:"Poppins",sans-serif;font-size:2.89375vw;font-weight:600;color:#FF8C00;margin:0px}}
p{{font-family:"Poppins";font-size:1.25vw;color:#000028;margin:2px}}
Form{{margin-bottom:0px}}
input{{width:200px;padding:10px;margin:8px;font-size:15px;font-family:"Poppins";border:2px solid #ccc;border-radius:8px}}
button{{background-color:#FF8C00;color:white;font-family:"Poppins";font-size:1vw;padding:10px 20px;border:none;border-radius:10px;cursor:pointer;width:15vw}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card0{{flex:2.5}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.nav{{position:absolute;top:15px;right:15px}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | The Chosen Number</title>
</head>
<body>
<h1>The Chosen Number</h1>
<p>Choose almost any four-digit number. Rearrange, subtract, repeat... and see where you end up.</p>

<div class="cardrow">
<div class="card Card1">
<h2>The process</h2>
<p>The process to magic isn't very hard!<br><br><b>1. Choose a 4 digit number<br>2. Arrange its digits in 2 ways: one where they are in ascending order and one where they are in descending.<br>3. Subtract the smaller number from the bigger one<br>4. Repeat</b></p>
</div>

<div class="card Card0">
<h2>Try it out</h2>
<br><br>
<p>{r}<b>6174</b></p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>
</div>

<br>

<div class="cardrow">
<div class="card Card1">
<h2>Why does this happen?</h2><br>
<p>When we rearrange and subtract the digits, lots of completely different numbers start giving the same results. For example, 3524 and 4253 both contain the same digits, so both become 5432 − 2345 = 3087. This quickly reduces thousands of possible numbers into a much smaller set of possibilities. As the process repeats, these paths eventually meet and lead to 6174.<br><br>6174 is especially interesting because it is a fixed point: arranging its digits gives 7641 and 1467, and 7641 − 1467 = 6174. So once you reach it, you're stuck there forever!</p>
</div>

<div class="card Card2">
<h2>Dr Kaprekar</h2><br>
<p>D. R. Kaprekar was an Indian mathematician who loved playing around with numbers and finding strange patterns in them.<br><br>In 1949, he discovered the strange behaviour of 6174, which is now known as Kaprekar's Constant. Surprisingly, he made many of his discoveries while working as a school teacher!</p>
<div class="la" style="margin-top:-25px"><br>
<button onclick="location.href='HOMEURL'" style="width:auto">Home</button>
<button onclick="location.href='QUIZURL'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""

app.run(host="0.0.0.0",port=5020)