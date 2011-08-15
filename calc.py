#!/usr/bin/python
import gtk
import time
import gtk.glade
import sys
class CalcGUI:
	def __init__(self):
		self.num1=0
		self.memory=0
		self.clearit=0
		self.wTree=gtk.glade.XML("gui.glade","Calculator")
		
		dic={"on_Calculator_destroy" : self.quit,
			  "on_button1_clicked" : self.backspace,
			  "on_button2_clicked" : self.ce,
			  "on_button3_clicked" : self.clear,
			  "on_button4_clicked" : self.plus_or_minus,
			  "on_button5_clicked" : (self.num,"7"),
			  "on_button6_clicked" : (self.num,"8"),
			  "on_button7_clicked" : (self.num,"9"),
			  "on_button8_clicked" : (self.calc,"4"),
			  "on_button9_clicked" : (self.num,"4"),
			  "on_button10_clicked" : (self.num,"5"),
			  "on_button11_clicked" : (self.num,"6"),
			  "on_button12_clicked" : (self.calc,"3"),
			  "on_button13_clicked" : (self.num,"1"),
			  "on_button14_clicked" : (self.num,"2"),
			  "on_button15_clicked" : (self.num,"3"),
			  "on_button16_clicked" : (self.calc,"2"),
			  "on_button17_clicked" : (self.num,"0"),
			  "on_button18_clicked" : (self.num,"."),
			  "on_button19_clicked" : self.equals,
			  "on_button20_clicked" : (self.calc,"1"),
			  "on_copy1_activate" : (self.copy_cut,1),
			  "on_cut1_activate" : (self.copy_cut,2),
			  "on_paste1_activate" : self.paste,
			  "on_about1_activate" : self.show_about,
			  "on_quit1_activate" : self.quit,}
		self.wTree.signal_autoconnect(dic)	  
		self.textentry=self.wTree.get_widget("entry1")
		self.pasteButton=self.wTree.get_widget("paste1")
		self.selection=gtk.gdk.SELECTION_CLIPBOARD
		self.clipboard=gtk.clipboard_get(self.selection)
		
	
	def quit(self,widget):
		"Handles the destroy signal of the window."	
		gtk.main_quit()
		sys.exit(1)
	
	def show_about(self,widget):
		"Shows the about window"
		self.AboutWindow=gtk.glade.XML("gui.glade","About")
		dic={"on_closeabout_clicked" : self.close_about,
			 "on_license_clicked" : self.show_license,}
		self.AboutWindow.signal_autoconnect(dic)	 
	
	def close_about(self,widget):
		closeabout_button = self.AboutWindow.get_widget("closeabout")
		gtk.gtk_widget_destroy(gtk_widget_get_toplevel(closeabout_button))
	
	def show_license(self,widget):
		"Display the license text"		 
		self.LicenseWindow=gtk.glade.XML("gui.glade","License")
	
	def num(self,widget,n):
		"Handles when the number buttons are clicked"
		
		if n is '.': #to avoid inserting more than one decimal point in a number
			text=self.textentry.get_text()
			if text.find('.') is -1:
				self.textentry.insert_text(n,position=30)
			else:
				return	
					
		if self.clearit is 1: #to clear the text entry box if operator button is one pressed just before
			self.textentry.set_text(n)
			self.clearit=0
		else:
			self.textentry.insert_text(n,position=30)
	
	def calc(self,widget,n):
		"Handles when the operators are clicked."
		self.memory=int(n)
		
		try:
			self.num1=float(self.textentry.get_text())
			self.clearit=1 #to st
			
		except ValueError:
			if self.memory is 1 :
				self.textentry.insert_text("+")
				return
			elif self.memory is 2:
				self.textentry.insert_text("-")
				self.memory=1
				return	
		#self.textentry.set_text("")
		
	def clear(self,widget):
		"Clear the text entry box."
		self.textentry.set_text("")
		self.num1='n'
		self.memory=0
	
	def ce(self,widget):
		"Clear the text entry box."
		self.textentry.set_text("")
		
		
	def backspace(self,widget):
		"Removes the right most digit in text entry box."
		temp=self.textentry.get_text()
		temp=temp[:-1]
		self.textentry.set_text(temp)
	
	def plus_or_minus(self,widget):
		"Clicked plus or minus button."
		temp=float(self.textentry.get_text())
		temp=-(temp)	
		self.textentry.set_text(str(temp))

	
	def equals(self,widget):
		"Handles when '=' button is clicked."
		self.num2=self.textentry.get_text()
		
		if self.num1=='n': #if equal button is pressed without mentioning second value
		   self.textentry.set_text(self.num2)
		   return
		   
		self.num2=float(self.num2)	
		
		if self.memory is 1:
			sum=str(self.num1+self.num2)
			if sum.split('.')[1] is '0':
				
				self.textentry.set_text(sum.split('.')[0])
			else :
				self.textentry.set_text(sum)	
		
		if self.memory is 2:
			diff=str(self.num1-self.num2)
			if diff.split('.')[1] is '0':
				self.textentry.set_text(diff.split('.')[0])
			else:
				self.textentry.set_text(diff)
		
		if self.memory is 3:
			prod=str(self.num1*self.num2)
			if prod.split('.')[1] is '0':
				self.textentry.set_text(prod.split('.')[0])
			else:
				self.textentry.set_text(prod)
		
		if self.memory is 4:
			div=str(self.num1/self.num2)
			if div.split('.')[1] is '0':
				self.textentry.set_text(div.split('.')[0])
			else:
				self.textentry.set_text(div)		
		
	def copy_cut(self,widget,n):
		self.pasteButton.set_sensitive(True)	
		self.clipboard.request_text(self.clipboard_text_received)
		
		
	
	def paste(self,widget):
		self.textentry.insert_text(self.cache,position=30)				
	

if __name__=='__main__':
	CalcGUI()
	try:
		gtk.gdk.threads_init()
	except:
		print "No threading was enabled when you compiled pyGTK! "
		import sys
		sys.exit(1)
	gtk.gdk.threads_enter()
	gtk.main()
	gtk.gdk.threads_leave()

