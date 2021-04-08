import os
from pygame import mixer
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.minsize(500,300)

listamusica = []
indice = 0
v = StringVar()
labelCanz = Label(root, textvariable=v, width=65)

def Play(event):
	global indice
	pygame.mixer.music.load(listamusica[indice])
	pygame.mixer.music.play()
	AggiornaLabelCanz()

def ProsCanz(event):
	global indice
	indice += 1
	pygame.mixer.music.load(listamusica[indice])
	pygame.mixer.music.play()
	AggiornaLabelCanz()

def PrecCanz(event):
	global indice
	indice -= 1
	pygame.mixer.music.load(listamusica[indice])
	pygame.mixer.music.play()
	AggiornaLabelCanz()

def PausaCanz(event):
	pygame.mixer.music.pause()
	v.set("")

def RicominCanz(event):
	global indice
	pygame.mixer.music.unpause()
	v.set(listamusica[indice])

def AggiornaLabelCanz():
	 global indice
	 v.set(listamusica[indice])

def Directory():
	directory = askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			listamusica.append(files)
			
	pygame.mixer.init()
	pygame.mixer.music.load(listamusica[0])
	#pygame.mixer.music.play()

def LivVolumeAudio(event):
	valore = VolumeLiv.get()
	pygame.mixer.music.set_volume(valore/100)

Directory()

label = Label(root, text="Music Player")
label.pack()

listbox = Listbox(root, width=50, height=12)	
listbox.pack()
#listamusica.reverse()
for musica in listamusica:
	listbox.insert(0, musica)
#listamusica.reverse()

IniziaBTN = Button(root, text="▷", foreground = "orange", background = "purple", width=5, height=1)
IniziaBTN.place(x=100, y=240)

ProsBTN = Button(root, text=">>", foreground = "white", background = "orange", width=5, height=1)
ProsBTN.place(x=200, y=240)

PrecBTN = Button(root, text="<<", foreground = "white", background = "blue", width=5, height=1)
PrecBTN.place(x=150, y=240)

PauseBTN = Button(root, text="■", foreground = "red", background = "yellow", width=5, height=1)
PauseBTN.place(x=250, y=240)

RicominBTN = Button(root, text="||", foreground = "green", background = "black", width=5, height=1)
RicominBTN.place(x=300, y=240)

VolumeLiv = Scale(root, from_=0, to_=100, orient=VERTICAL, resolution=1, command=LivVolumeAudio)
VolumeLiv.place(x=400, y=120)
VolumeLiv.set(70)  # implement the default value of scale when music player starts
mixer.music.set_volume(0.7)

IniziaBTN.bind("<Button-1>",Play)
ProsBTN.bind("<Button-1>",ProsCanz)
PrecBTN.bind("<Button-1>",PrecCanz)
PauseBTN.bind("<Button-1>",PausaCanz)
RicominBTN.bind("<Button-1>",RicominCanz)
VolumeLiv.bind("<B1-Motion>",LivVolumeAudio)

labelCanz.pack()

root.mainloop() 
