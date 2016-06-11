import sys
from random import randint
from ui.Show import Ui_MainWindow
from ui.winnerDialog import Ui_Dialog

from PyQt4 import QtGui, QtCore
import time
# from time import strftime
import datetime
import pygame
pygame.mixer.init()

from common import _fromUtf8

OPEN = 'wav/open.wav'  # played at the staring of the software
START = 'wav/start.wav'  # player at starting the race
END = 'wav/end.wav'  # played when the race ends for bowth
WRONGS = [
	# 'wav/wrong.wav',
	'wav/tone1.wav',
	'wav/tone2.wav',
	'wav/tone3.wav',
	'wav/tone4.wav'
]  # player wen anyone touches the wire
WRONGC = 'wav/wrong.wav'  # player wen anyone touches the wire

TEST = False
PRI = True  # defines if it is being used with the Raspberry pi or not

PUNISHMENT = 1
TIME = 0.5  # delay in seconds
INPUTS = [27, 17]
CTRLSP = [22, 10]


if PRI:
	import RPi.GPIO as GPIO


class Main(QtGui.QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):
		super(Main, self).__init__()
		self.setupUi(self)
		self.showMaximized()

		# button connections
		self.connect(self.btnStart, QtCore.SIGNAL("clicked()"), self.PreStart)
		self.connect(self.btnStop, QtCore.SIGNAL("clicked()"), self.Stop)
		self.connect(self.btnReset, QtCore.SIGNAL("clicked()"), self.Reset)
		self.connect(self.btnOpening, QtCore.SIGNAL("clicked()"), self.Opening)

		self.connect(self.btnStopP1, QtCore.SIGNAL("clicked()"), self.StopP1)
		self.connect(self.btnStopP2, QtCore.SIGNAL("clicked()"), self.StopP2)

		self.connect(self.btnPointP1, QtCore.SIGNAL("clicked()"), self.PointP1)
		self.connect(self.btnPointP2, QtCore.SIGNAL("clicked()"), self.PointP2)
		self.loadInit()

	def loadInit(self):
		# Reasignes the start variables
		self.TP1 = self.TP2 = 0

		# initializes the gpio pins
		self.initializeGPIO()

		# timer definitions
		self.timer = QtCore.QTimer(self)
		self.P1timer = QtCore.QTimer(self)
		self.P2timer = QtCore.QTimer(self)
		# cloks at 0
		t0 = '0:0:0'
		self.ClockLCD.display(t0)

		self.ClockP1.display(t0)
		self.ClockP2.display(t0)

		# Main timer
		self.timer.timeout.connect(self.Time)

		if not TEST:
			self.GroupboxTests.hide()
		self.startCts()

	def Opening(self):
		self.playSound(OPEN)

	def initializeGPIO(self):
		if PRI:
			GPIO.setmode(GPIO.BCM)
			pins = INPUTS + CTRLSP
			try:
				for pin in pins:
					GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
				GPIO.add_event_detect(INPUTS[0], GPIO.FALLING, bouncetime=int(1000 * TIME), callback=self.PointP1)
				GPIO.add_event_detect(INPUTS[1], GPIO.FALLING, bouncetime=int(1000 * TIME), callback=self.PointP2)
				GPIO.add_event_detect(CTRLSP[0], GPIO.FALLING, bouncetime=200, callback=self.StopP1)
				GPIO.add_event_detect(CTRLSP[1], GPIO.FALLING, bouncetime=200, callback=self.StopP2)
			except RuntimeError:
				GPIO.cleanup()
				self.initializeGPIO()

	def startCts(self):
		self.started = False
		# Time lapsed for each player in secs
		self.s = self.P1s = self.P2s = self.t1 = self.t2 =  0

		# Points per player
		self.Points_P1 = 0
		self.Points_P2 = 0

		self.PointP1()
		self.PointP2()

		# continuity vars
		self.TP1 = self.TP2 = 1

	def PreStart(self):
		self.playSound(START)
		time.sleep(3)
		self.Start()

	def Reset(self):
		self.timer.stop()

		time = str(datetime.timedelta(seconds=0))

		self.ClockLCD.setDigitCount(len(time))
		self.ClockLCD.display(time)

		self.ClockP1.display(time)
		self.ClockP2.display(time)
		self.loadInit()
		self.startCts()

	def Start(self):
				# continuity vars
		self.TP1 = self.TP2 = 1
		self.startCts()
		self.started = True
		self.timer.start(1000)
		self.P1timer.start(1000)
		self.P2timer.start(1000)

	def Stop(self):
		if PRI:
			GPIO.cleanup()

		self.started = False
		self.timer.stop()
		self.StopP1()
		self.StopP2()
		self.playSound(END)
		self.results()

	def StopP1(self, dummy=False):
		self.TP1 = 0
		self.P1timer.stop()

	def StopP2(self, dummy=False):
		self.TP2 = 0
		self.P2timer.stop()

	def update_score(self):
		self.P1s = self.t1 + PUNISHMENT * self.Points_P1
		self.P2s = self.t2 + PUNISHMENT * self.Points_P2

	def Time(self):
		self.s += 1
		time = str(datetime.timedelta(seconds=self.s))
		self.ClockLCD.setDigitCount(len(time))
		self.ClockLCD.display(time)

		self.update_score()

		if self.TP1:
			self.t1 = self.s 
			self.ClockP1.setDigitCount(len(time))
			self.ClockP1.display(str(datetime.timedelta(seconds=self.P1s)))

		if self.TP2:
			self.t2 = self.s 
			self.ClockP2.setDigitCount(len(time))
			self.ClockP2.display(str(datetime.timedelta(seconds=self.P2s)))

		if not self.TP1 and not self.TP2 and self.started:
			self.Stop()
		self.update_score()

	def PointP1(self, dummy=False):
		if self.TP1 and self.started:
			self.playSound(WRONGS[randint(0, len(WRONGS) - 1)])
			self.Points_P1 += 1
			self.ClockP1.display(str(datetime.timedelta(seconds=self.P1s)))
		self.update_score()

	def PointP2(self, dummy=False):
		if self.TP2 and self.started:
			self.playSound(WRONGC)
			self.Points_P2 += 1
			self.ClockP2.display(str(datetime.timedelta(seconds=self.P2s)))
		self.update_score()

	def playSound(self, path):
		pygame.mixer.music.load(path)
		pygame.mixer.music.play()

	def results(self):
		self.ClockP1.display(str(datetime.timedelta(seconds=self.P1s)))
		self.ClockP2.display(str(datetime.timedelta(seconds=self.P2s)))

		if self.P1s < self.P2s:
			winner = _fromUtf8(":/people/user_1.jpg")
		else:
			winner = _fromUtf8(":/people/user_2.jpg")
		W = Winner(winner, self)
		W.exec_()

	def __del_(self):
		if PRI:
			GPIO.cleanup()


class Winner(QtGui.QDialog, Ui_Dialog):

	def __init__(self, winner, parent=None):
		super(Winner, self).__init__()
		self.setupUi(self)
		self.p1_name.setPixmap(QtGui.QPixmap(winner))


def main():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
