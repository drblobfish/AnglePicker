
# -*- coding: utf-8 -*-


from tkinter import * 
from math import * 


win = Tk() 
fen = Frame(win, bd = 0)
fen.pack()



def to_angle(x,y): 
	angle = -degrees(atan2(x,y)) 
	if angle<0 :
		angle = angle + 360
	return angle


def click(event): 
	
	
	
	global coord 
	coord = [event.x,event.y]
	
	coord = [250-coord[0],250-coord[1]]
	
	coord_lenght = sqrt(coord[0]**2 + coord[1]**2)
	coord = [coord[0]/coord_lenght,coord[1]/coord_lenght]
	print(coord[0],coord[1],to_angle(coord[0],coord[1])) 
	carte.coords(point,250-(coord[0]*220)-5,250-(coord[1]*220)-5,250-(coord[0]*220)+5,250-(coord[1]*220)+5)
	


def key():

	data = open('data.csv','a')

	global nb_participant
	nb_participant += 1
	data.write(str(nb_participant)+","+str(coord[0])+","+str(coord[1])+","+str(to_angle(coord[0],coord[1]))+"\n")
	data.close
	Lbl_nb_participant.configure(text=("Test n° "+str(nb_participant)))
	carte.coords(point,245,245,255,255)


Lbl_nb_participant = Label(fen,text="Test n° 0",font=("Arial","40"))
Lbl_nb_participant.pack()


carte = Canvas(fen,height=500 , width=500 ,bd = 0)
carte.pack()

enter_butt = Button(fen,command=key,text="Sélectionner",font=("Arial","40"))
enter_butt.pack()



carte.create_oval(30,30,470,470,width=2)
carte.create_line(250,280,250,160, width=2, fill='black')
carte.create_line(220,250,280,250, width=2, fill='black')
point = carte.create_oval(245,245,255,255,fill='red')



data = open('data.csv','r')
nb_participant = int(data.readlines()[-1].split(',')[0])
Lbl_nb_participant.configure(text=("Test n° "+str(nb_participant)))
print(nb_participant)
data.close()

coord = []


carte.bind("<Button-1>", click)


win.mainloop()