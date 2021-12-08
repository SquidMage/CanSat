import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use("fivethirtyeight")

fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax2 = fig.add_subplot(2,1,1)
ax3 = fig.add_subplot(1,1,1)

def animate(i):
    counter = 0
    c = []
    
    tpa_data = open("TPA.txt", "r").read()
    tpa_lines = tpa_data.split("\n")
    ts = []
    ps = []
    alts = []
    
    
    for line in tpa_lines:
        if len(line) > 1:
            t,p,a = line.split(",")
            ts.append(float(t))
            ps.append(float(p))
            alts.append(float(a))
            
            
    
    gyro_data = open("GYRO.txt", "r").read()
    gyro_lines = gyro_data.split("\n")
    xs1 = []
    ys1 = []
    zs1 = []
    xs2 = []
    ys2 = []
    zs2 = []
    xs3 = []
    ys3 = []
    zs3 = []
    xs4 = []
    ys4 = []
    zs4 = []
    xs5 = []
    ys5 = []
    zs5 = []
    
    for line in gyro_lines:
        if len(line) > 1:
            x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5 = line.split(",")
            xs1.append(float(x1))
            ys1.append(float(y1))
            zs1.append(float(z1))
            xs2.append(float(x2))
            ys2.append(float(y2))
            zs2.append(float(z2))
            xs3.append(float(x3))
            ys3.append(float(y3))
            zs3.append(float(z3))
            xs4.append(float(x4))
            ys4.append(float(y4))
            zs4.append(float(z4))
            xs5.append(float(x5))
            ys5.append(float(y5))
            zs5.append(float(z5))
            counter = counter + 1
            c.append(float(counter))
    
    #ax1.clear()
    #ax2.clear()
    ax3.clear()
    
    #ax1.plot(alts, ps)
    #ax2.plot(alts, ts)
    ax3.plot(c, xs1)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()