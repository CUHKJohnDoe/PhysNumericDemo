import matplotlib.pyplot as plt
import numpy as np

print("Initial Displacement:\n")
x_init=float(input("x_0="))
print("\nInitial Velocity:\n")
v_init=float(input("y_0="))
print("\nInitial Acceleration:\n")
a_init=float(input("a_0="))

print("\nTime each step (s):\n")
t_step=float(input("delta_t="))

print("\nTerminal Time:\n")
t_n=float(input("t_n="))

xlist=[x_init]
vlist=[v_init]
alist=[a_init]


def _updnext_():
    xpre=xlist[len(xlist)-1]
    vpre=vlist[len(vlist)-1]
    apre=alist[len(alist)-1]
    xlist.append(xpre+t_step*vpre)
    vlist.append(vpre+t_step*apre)
    alist.append(apre)
    return

t_cur=float(0)

while (t_cur<t_n):
    t_cur=t_cur+t_step
    _updnext_()

xaxis=np.arange(0,t_n,t_step)

plt.xlabel("Time(t)")
plt.plot(xaxis,xlist[0:len(xaxis):1],'b')
plt.plot(xaxis,vlist[0:len(xaxis):1],'g')
plt.plot(xaxis,alist[0:len(xaxis):1],'r')
plt.show()

