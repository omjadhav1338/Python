from tkinter import *
r=Tk()
i=0
c=Canvas(r,bg="orange",width=920,height=240)
c1=Canvas(r,width=920,height=240)
c2=Canvas(r,bg="green",width=920,height=240)
for i in range(0,24):
    c1.create_oval(340,3,580,241,width=4,outline="navy")
    c1.create_arc(340,3,580,241,width=2,start=0,extent=15*i,outline="navy")
    c1.create_oval(456,118,464,126,width=2,fill="white",outline="white")
c.pack()
c1.pack()
c2.pack()
r.mainloop()