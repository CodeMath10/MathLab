import random
import matplotlib.pyplot as plt
ss=int(input("How often to repeat?\n"))
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
plt.figure(figsize=(5,5),facecolor="#FDF1E5")
plt.gca().set_facecolor("#FDF1E5")
plt.scatter(points_x,points_y,s=1,color="#FF8C00")
plt.axis("equal")
plt.axis("off")
plt.show()
