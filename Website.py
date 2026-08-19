from flask import Flask,request,send_file
from io import BytesIO
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import random
app=Flask(__name__)
@app.route("/data")
def data():
    ss=int(request.args["ss"])
    A=(0,10)
    B=(-5 * 3**0.5, -5)
    C=(5 * 3**0.5, -5)
    corners=[A,B,C] 
    x=0
    y=0
    points_x=[]
    points_y=[]
    for i in range(ss):
        corner=random.choice(corners)
        x=(x+corner[0])/2
        y=(y+corner[1])/2
        points_x.append(x)
        points_y.append(y)
    plt.figure(figsize=(1,1),facecolor="#FDF1E5")
    plt.gca().set_facecolor("#FDF1E5")
    plt.scatter(points_x,points_y,s=0.05,color="#FF8C00",edgecolors="none")
    plt.axis("equal")
    plt.axis("off")
    plt.xlim(-9,9)
    plt.ylim(-5.5,10.5)
    img=BytesIO()
    plt.savefig(img,format="png", dpi=1200)
    plt.close()
    img.seek(0)
    return send_file(img, mimetype="image/png",)
@app.route("/",methods=["GET","POST"])
def tri():
    if request.method=="POST":
        ss=int(request.form["ss"])
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
button{{background-color:#FF8C00;color:white;font-family:"Poppins";padding:10px 20px;border:none;border-radius:10px;cursor:pointer;}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | Random = NOT Random?</title>
</head>
<body>
<h1>Random = <u>NOT</u> Random?</h1>
<p>Isn't it cool how, in math, random rules and random choices can make some of the most complex and non-random patterns? Let's look at one such example ourselves.</p>

<div class="cardrow">
<div class="maincard1 Card1">
<div class="Card3">
<h2>Here it is</h2>
<p><b>Make a triangle.<br>Choose a random point anywhere in the triangle and mark the point exactly halfway to a random corner of the triangle and Repeat</b></p>
<p>Start from 10 and work your way up. Do you see it?</p>

<button type="button" onclick="showPoints(10)">10</button>
<button type="button" onclick="showPoints(100)">100</button>
<button type="button" onclick="showPoints(1000)">1K</button>
<button type="button" onclick="showPoints(10000)">10K</button>
<button type="button" onclick="showPoints(100000)">100K</button>
</div>

<div class="cardd">
<img id="chaosimg" src="/data?ss=10" style="height:100%;width:100%;display:block;">
<script>
function showPoints(n){{document.getElementById("chaosimg").src="/data?ss="+n;}}
</script>
</div>
</div>

<div class="maincard1 Card1">
<div class="Card3">
<h2>Try it yourself</h2>
<p>Enter any random number and watch as the pattern emerges.<br><br><i>Try big numbers for better results.</i></p><br><br>
<form method="POST">
<input name="ss" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>

<div class="cardd">
<img src="/data?ss={ss}" style="width:100%">
</div>
</div>
</div>

<br>

<div class="card">
<h2>The Sierpiński Triangle</h2>
<p>What you've just made is called the <b>Sierpiński Triangle</b>. It is a fractal — a pattern that repeats itself at smaller and smaller scales. Look closely: the large triangle is made of three smaller triangles, and each of those contains three even smaller ones. This pattern can theoretically continue forever. But here's the weird part: we never told the computer to draw a Sierpiński Triangle. It only chose random corners and moved halfway towards them. Random choices + one simple rule created an incredibly organised pattern.</p>

<div class="la" style="margin-top:-25px">
<button onclick="location.href='https://codemath10.github.io/MathLab/'" style="width:auto">Home</button>
<button onclick="location.href='https://codemath10.github.io/MathLab/TriangleQuiz.html'" style="width:auto">Quiz</button>
</div>
</div>
</body>
</html>"""
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
button{{background-color:#FF8C00;color:white;font-family:"Poppins";padding:10px 20px;border:none;border-radius:10px;cursor:pointer;}}
.cardrow{{display:flex;gap:20px}}
.card{{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}}
.maincard1{{background-color:rgba(251,227,214,0.5);border-radius:20px;display:flex;overflow:visible;height:23vw;}}
.cardd{{aspect-ratio:1/1;height:100%}}
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;padding:15px;}}
.tp{{height:23vw}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | Random = NOT Random?</title>
</head>
<body>
<h1>Random = <u>NOT</u> Random?</h1>
<p>Isn't it cool how, in math, random rules and random choices can make some of the most complex and non-random patterns? Let's look at one such example ourselves.</p>

<div class="cardrow">
<div class="maincard1 Card1">
<div class="Card3">
<h2>Here it is</h2>
<p><b>Make a triangle.<br>Choose a random point anywhere in the triangle and mark the point exactly halfway to a random corner of the triangle and Repeat</b></p>
<p>Start from 10 and work your way up. Do you see it?</p>

<button type="button" onclick="showPoints(10)">10</button>
<button type="button" onclick="showPoints(100)">100</button>
<button type="button" onclick="showPoints(1000)">1K</button>
<button type="button" onclick="showPoints(10000)">10K</button>
<button type="button" onclick="showPoints(100000)">100K</button>
</div>

<div class="cardd">
<img id="chaosimg" src="/data?ss=10" style="height:100%;width:100%;display:block;">
<script>
function showPoints(n){{document.getElementById("chaosimg").src="/data?ss="+n;}}
</script>
</div>
</div>

<div class="maincard1 Card1">
<div class="Card3">
<h2>Try it yourself</h2>
<p>Enter any random number and watch as the pattern emerges.<br><br><i>Try big numbers for better results.</i></p><br><br>
<form method="POST">
<input name="ss" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
</div>

<div class="cardd">
<img src="" style="display:none">
</div>
</div>
</div>

<br>

<div class="card">
<h2>The Sierpiński Triangle</h2>
<p>What you've just made is called the <b>Sierpiński Triangle</b>. It is a fractal — a pattern that repeats itself at smaller and smaller scales. Look closely: the large triangle is made of three smaller triangles, and each of those contains three even smaller ones. This pattern can theoretically continue forever. But here's the weird part: we never told the computer to draw a Sierpiński Triangle. It only chose random corners and moved halfway towards them. Random choices + one simple rule created an incredibly organised pattern.</p>

<div class="la" style="margin-top:-25px">
<button onclick="location.href='https://codemath10.github.io/MathLab/'" style="width:auto">Home</button>
<button onclick="location.href='https://codemath10.github.io/MathLab/TriangleQuiz.html'" style="width:auto">Quiz</button>
</div>
</div>
</body>
</html>"""
app.run(host="0.0.0.0",port=5545)
