import PySimpleGUI as sg
import mysql.connector as mc
def signup():
      col1=[[sg.Text('user_name')],[sg.Input('abcde')]]
      col2= [[sg.Text('password')],[sg.Input('ghijk')]]
      col3=[[sg.Text('phoneno')],[sg.Input('9001234567')]]
      col4=[[sg.Text('email')],[sg.Input('ab@gmail.com')]]
      layout=[[sg.Column(col1),sg.Column(col2)],[sg.Column(col3),sg.Column(col4)],[sg.Button('signup'),sg.Button('back')],[sg.Image('signup.png')]]
      window=sg.Window('AIRLINE RESERVATION SYSTEM',layout,element_justification='c').finalize()
      event,values=window.read()
      print(event,values)
      return(event,values)

    

