from Tkinter import *
import RPi.GPIO as GPIO

blue_code = 25
yellow_code = 18
red_code = 14

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_code, GPIO.OUT)
GPIO.setup(yellow_code, GPIO.OUT)
GPIO.setup(red_code, GPIO.OUT)

GPIO.output(blue_code, GPIO.LOW)
GPIO.output(yellow_code, GPIO.LOW)
GPIO.output(red_code, GPIO.LOW)



window = Tk()

window.title("LED control panel")

window.geometry('350x200')

def onExit():
	window.destroy()

exitButton = Button(window, text="Exit", command=onExit)

def onRed():
	GPIO.output(blue_code, GPIO.LOW)
	GPIO.output(yellow_code, GPIO.LOW)
	GPIO.output(red_code, GPIO.HIGH)

red = Radiobutton(window,text='Red', value=1, command=onRed)

def onYellow():
	GPIO.output(red_code, GPIO.LOW)
	GPIO.output(blue_code, GPIO.LOW)
	GPIO.output(yellow_code, GPIO.HIGH)
	

yellow = Radiobutton(window,text='Yellow', value=2, command=onYellow)

def onBlue():
	GPIO.output(yellow_code, GPIO.LOW)
	GPIO.output(red_code, GPIO.LOW)
	GPIO.output(blue_code, GPIO.HIGH)
	
blue = Radiobutton(window,text='Blue', value=3, command=onBlue)

red.grid(column=0, row=0)

yellow.grid(column=1, row=0)

blue.grid(column=2, row=0)

exitButton.grid(column=3, row=0)



window.mainloop()

GPIO.cleanup()
