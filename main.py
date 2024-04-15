import cmath as m
import matplotlib.pyplot as plt

c=340
x=[[q/100 for q in range(-22,23,3)] for w in range(-22,23,3)]
y=[[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

freqz=[500, 1000, 2000, 10000]

plt.figure(1)
for f in freqz:
    print(f)
    XH=[]
    phi=[]
    for i in range(180):
        loc_phi=i-90
        loc_XH=0+0j
        for j in range(len(x)):
            for k in range(len(x[0])):
                delay=x[j][k]/c*m.sin(loc_phi/180*m.pi)
                phase=2*m.pi*f*delay

                w = 0.5*(1-m.cos(2*m.pi*k/len(x)))

                loc_XH += w*m.exp(1j*phase)
        XH.append(abs(loc_XH))
        phi.append(loc_phi)

    max_XH=max(XH)
    for i in range(180):
        XH[i]/=max_XH
    plt.plot(phi, XH)

plt.legend([str(freqz[i])for i in range(len(freqz))])
plt.grid(True)

plt.figure(2)
plt.plot(x,y,'*')

plt.show()