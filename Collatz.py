from flask import Flask,request,send_file
from io import BytesIO
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
app=Flask(__name__)
@app.route("/data")
def data():
    n=int(request.args["n"])
    a=n
    s=0
    sequence=[n]
    gn=n
    while n>1:
        if n%2==0:
            n=n//2
            sequence.append(n)
            s+=1
        else:
            n=3*n+1
            sequence.append(n)
            s+=1
            if n>gn:
                gn=n
    steps=range(len(sequence))
    plt.figure(figsize=(21,8.5),facecolor="#FDF1E5")
    plt.gca().set_facecolor("#FDF1E5")
    plt.plot(steps,sequence,marker="o",color="#FF8C00",linewidth=3,markersize=10)
    plt.title("Collatz Sequence for "+str(a)+"\n",fontsize=32,fontweight="bold")
    plt.xlabel("Step",fontsize=28)
    plt.ylabel("Value",fontsize=28)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.xlim(left=0)
    img=BytesIO()
    plt.savefig(img,format="png", dpi=300)
    plt.close()
    img.seek(0)
    return send_file(img, mimetype="image/png",)
@app.route("/",methods=["GET","POST"])
def collatz():
    if request.method=="POST":
        n=int(request.form["nm"])
        a=n
        s=0
        sequence=[n]
        gn=n
        while n>1:
            if n%2==0:
                n=n//2
                sequence.append(n)
                s+=1
            else:
                n=3*n+1
                sequence.append(n)
                s+=1
                if n>gn:
                    gn=n
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
.Card1{{flex:3;}}
.Card2{{flex:2;}}
.Card3{{flex:1;}}
.tp{{height:23vw}}
.la{{text-align:right}}
#results{{display:none}}
</style>
<title>MathLab | Simple Rules. Complex Patterns.</title>
<script>
function openTab(tab){{document.getElementById("try").style.display="none";document.getElementById("results").style.display="none";document.getElementById(tab).style.display="block";}}
</script>
</head>
<body>
<h1>Simple Rules. Complex Patterns.</h1>
<p>Have you ever wondered how simple rules, can make patterns so complex some mathematicians spend their whole lives trying to solve them? It's one of the many weird things about math.</p>
<br>
<div class="cardrow tp">
<div class="card Card2">
<h2>Let's try one ourselves</h2>
<br>
<button type="button" onclick="openTab('try')">Try It</button>
<button type="button" onclick="openTab('results')">Results</button>
<div id="try">
<p><b>If a number is even, divide it by 2.<br>If it's odd, multiply it by 3 and add 1.</b><br>That's it.</p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
<p style="font-size:20px"><i>P.S. Try 27</i></p>
</div>
<div id="results">
<br><br><br>
<p style="font-size:20px">The greatest number was {gn}<br>It took {s} steps.</p>
</div>
</div>
<div class="card Card1">
<center>
<img src="/data?n={a}" style="width:100%">
</center>
</div>
</div>
<br>
<div class="cardrow">
<div class="card Card3">
<h2>1,4,2...1?</h2>
<p>If you played with the graph enough you should have realised that every number always <I>seems to</I> come back to one and the graph just stops there. The reason it stops isn't because that's where the sequence ends. Let's try for 5. 5, is odd, so 5x3+1=16. 16/2=8, 8/2=4, 4/2=2, 2/2=1, one is odd, so 1x3+1=4, 4 is even, so 4/2=2 and 2/2=1 and it just goes on forever. This problem is known as <b>Collatz Conjecture</b>. The reason it is a conjecture is nobody in the world has proven every number reaches 1. </p>
</div>
<div class="card Card3">
<h2>Why 3x <u><b>+1</b></u></h2>
<p>I'm pretty sure you still have one burning question in your head: if it's odd, why multiply by 3 and <b>add 1</b>? Let's try with an example of 5 again. 5 is odd. 5x3=15. 15 is odd. 15x3=45. 45 is yet again odd. 45x3=135. And 135 is odd too. 135x3=405. And it just keeps growing. This is because whenever you multiply any odd number by another odd number (like 3), the answer stays odd. Adding the 1 makes sure the answer is even and the numbers don't just multiply by 3 forever.</p>
<div class="la" style="margin-top:-25px">
<button onclick="location.href='/index.html'" style="width:auto">Home</button>
<button onclick="location.href='/CollatzQuiz.html'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""
    return"""<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{background-color:#FFFFF5}
h1{font-family:"Poppins",sans-serif;font-size:4.75vw;font-weight:700;color:#FF8C00;margin:5px}
h2{font-family:"Poppins",sans-serif;font-size:2.89375vw;font-weight:600;color:#FF8C00;margin:0px}
p{font-family:"Poppins";font-size:1.25vw;color:#000028;margin:2px}
Form{margin-bottom:0px}
input{width:200px;padding:10px;margin:8px;font-size:15px;font-family:"Poppins";border:2px solid #ccc;border-radius:8px}
button{background-color:#FF8C00;color:white;font-family:"Poppins";padding:10px 20px;border:none;border-radius:10px;cursor:pointer;}
.cardrow{display:flex;gap:20px}
.card{padding:15px;background-color:rgba(251,227,214,0.5);border-radius:20px;}
.Card1{flex:3;}
.Card2{flex:2;}
.Card3{flex:1;}
.tp{height:23vw}
.la{text-align:right}
#results{display:none}
</style>
<title>MathLab | Simple Rules. Complex Patterns.</title>
<script>
function openTab(tab){
document.getElementById("try").style.display="none";
document.getElementById("results").style.display="none";
document.getElementById(tab).style.display="block";
}
</script>
</head>
<body>
<h1>Simple Rules. Complex Patterns.</h1>
<p>Have you ever wondered how simple rules, can make patterns so complex some mathematicians spend their whole lives trying to solve them? It's one of the many weird things about math.</p>
<br>
<div class="cardrow tp">
<div class="card Card2">
<h2>Let's try one ourselves</h2>
<br>
<button type="button" onclick="openTab('try')">Try It</button>
<button type="button" onclick="openTab('results')">Results</button>
<div id="try">
<p><b>If a number is even, divide it by 2.<br>If it's odd, multiply it by 3 and add 1.</b><br>That's it.</p>
<form method="POST">
<input name="nm" placeholder="Enter any number">
<button type="submit">Enter</button>
</form>
<p style="font-size:20px"><i>P.S. Try 27</i></p>
</div>
<div id="results">
<br><br><br>
<p style="font-size:20px">The greatest number was {gn}<br>It took {s} steps.</p>
</div>
</div>
<div class="card Card1">
<center>
<br><br><br><br><br>
<h2 style="color:#000028">Enter the number on the<br> left and see the magic!</h2>
</center>
</div>
</div>
<br>
<div class="cardrow">
<div class="card Card3">
<h2>1,4,2...1?</h2>
<p>If you played with the graph enough you should have realised that every number always <I>seems to</I> come back to one and the graph just stops there. The reason it stops isn't because that's where the sequence ends. Let's try for 5. 5, is odd, so 5x3+1=16. 16/2=8, 8/2=4, 4/2=2, 2/2=1, one is odd, so 1x3+1=4, 4 is even, so 4/2=2 and 2/2=1 and it just goes on forever. This problem is known as <b>Collatz Conjecture</b>. The reason it is a conjecture is nobody in the world has proven every number reaches 1. </p>
</div>
<div class="card Card3">
<h2>Why 3x <u><b>+1</b></u></h2>
<p>I'm pretty sure you still have one burning question in your head: if it's odd, why multiply by 3 and <b>add 1</b>? Let's try with an example of 5 again. 5 is odd. 5x3=15. 15 is odd. 15x3=45. 45 is yet again odd. 45x3=135. And 135 is odd too. 135x3=405. And it just keeps growing. This is because whenever you multiply any odd number by another odd number (like 3), the answer stays odd. Adding the 1 makes sure the answer is even and the numbers don't just multiply by 3 forever.</p>
<div class="la" style="margin-top:-25px">
<button onclick="location.href=''" style="width:auto">Home</button>
<button onclick="location.href='/CollatzQuiz.html'" style="width:auto">Quiz</button>
</div>
</div>
</div>
</body>
</html>"""
app.run(host="0.0.0.0",port=5555)
