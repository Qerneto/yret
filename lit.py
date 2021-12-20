from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget 

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

import math

class Quadratic_equations(App):
	def update_label(self):
		self.lbl.text = self.formula

	def add_number(self, instance):
		
		self.append += instance.text
		if self.append == '-':
			self.coef[self.n][0] = self.coef[self.n][0]
		else:
			self.coef[self.n][0] = float(self.append)

		if self.coef[1][0] < 0:
			if self.coef[2][0] < 0:
				self.formula = (str(self.coef[0][0])+" x^2 " + '' +  str(self.coef[1][0]) + " x " + "" + str(self.coef[2][0]))
			else:
				self.formula = (str(self.coef[0][0])+" x^2 " + '' +  str(self.coef[1][0]) + " x " + " + " + str(self.coef[2][0]))

		elif self.coef[2][0] < 0:
			if self.coef[1][0] < 0:
				self.formula = (str(self.coef[0][0])+" x^2 " + '' +  str(self.coef[1][0]) + " x " + "" + str(self.coef[2][0]))
			else:
				self.formula = (str(self.coef[0][0])+" x^2 " + ' + ' +  str(self.coef[1][0]) + " x " +  "" + str(self.coef[2][0]))

		else:
			self.formula = (str(self.coef[0][0])+" x^2 " + ' + ' +  str(self.coef[1][0]) + " x " +" + " + str(self.coef[2][0]))

		
		self.D = int(self.coef[1][0])**2 - 4*int(self.coef[0][0])*int(self.coef[2][0])

		self.update_label()
		
	def replace_right(self, instance):
		self.n += 1
		self.append = ''

		if self.n > 2:
			self.n = 2

		self.update_label()

	def replace_left(self, instance):
		self.n -= 1 
		self.append = ''

		if self.n < 0:
			self.n = 0

		self.update_label()
#Пересмотреть вывод lbl.text
	def result(self, instance):
		if self.D > 0:
			self.lbl.text = str((self.coef[1][0]**2 - math.sqrt(self.D))/(2*self.coef[0][0])) + ' and ' + str((self.coef[1][0]**2 + math.sqrt(self.D))/(2*self.coef[0][0]))
			
		
		elif self.D == 0 :
			self.lbl.text = str((self.coef[1][0]**2)/(2*self.coef[0][0]))
			
		else:
			self.lbl.text = ("Нет ответов")

		if self.coef[1][0] < 0:
			if self.coef[2][0] < 0:
				self.formula = (str(self.coef[0][0])+" x^2 " + '' +  str(self.coef[1][0]) + " x " + "" + str(self.coef[2][0]))
			else:
				self.formula = (str(self.coef[0][0])+" x^2 " + '' +  str(self.coef[1][0]) + " x " + " + " + str(self.coef[2][0]))

		elif self.coef[2][0] < 0:
			if self.coef[1][0] < 0:
				self.formula = (str(self.coef[0][0])+" x^2 " + '' +  str(self.coef[1][0]) + " x " + "" + str(self.coef[2][0]))
			else:
				self.formula = (str(self.coef[0][0])+" x^2 " + ' + ' +  str(self.coef[1][0]) + " x " +  "" + str(self.coef[2][0]))

		else:
			self.formula = (str(self.coef[0][0])+" x^2 " + ' + ' +  str(self.coef[1][0]) + " x " +" + " + str(self.coef[2][0]))
			

		self.append = ''


	def build(self):
		self.append = ""
		self.coef = [[1,"a"],[1,'b'],[1,'c']]
		self.n = 0
		self.D = self.coef[1][0]**2 - 4*self.coef[0][0]*self.coef[2][0]
		self.formula =  (str(self.coef[0][0])+" x^2 " + ' + ' +  str(self.coef[1][0]) + " x " +" + " + str(self.coef[2][0]))


		bl = BoxLayout(orientation = 'vertical', padding = 25)
		gl = GridLayout(cols = 3 , rows = 5, spacing = 3 , size_hint = (1, .6))

		self.lbl =  Label(text = self.formula, font_size = 40, size_hint = (1, .4))
		bl.add_widget( self.lbl )
		
		
		gl.add_widget( Button(text = '7', on_press = self.add_number))
		gl.add_widget( Button(text = '8', on_press = self.add_number))
		gl.add_widget( Button(text = '9', on_press = self.add_number))
		

		gl.add_widget( Button(text = '4', on_press = self.add_number))
		gl.add_widget( Button(text = '5', on_press = self.add_number))
		gl.add_widget( Button(text = '6', on_press = self.add_number))
		

		gl.add_widget( Button(text = '1', on_press = self.add_number))
		gl.add_widget( Button(text = '2', on_press = self.add_number))
		gl.add_widget( Button(text = '3', on_press = self.add_number))

		gl.add_widget( Button(text = ".", on_press = self.add_number))
		gl.add_widget( Button(text = '0', on_press = self.add_number))
		gl.add_widget( Button(text = "=", on_press = self.result))

		gl.add_widget( Button(text = '<--', on_press = self.replace_left))
		gl.add_widget( Button(text = "-", on_press = self.add_number))
		gl.add_widget( Button(text = '-->', on_press = self.replace_right))
		
		
		bl.add_widget( gl ) 
		return bl

if __name__ == "__main__":
	Quadratic_equations().run()

