import PySimpleGUI as sg
import mysql.connector as mc
def user():
     col2=[[sg.Text('username')],[sg.Input('Username')]]
     col1= [[sg.Text('password')],[sg.Input('Password')]]
     layout=[[sg.Column(col2),sg.Column(col1)],[sg.Button('signin'),sg.Button('back')],[sg.Image('fl.png',size=(200,150))]]
     window=sg.Window('AIRLINE RESERVATION SYSTEM',layout,element_justification='c').finalize()
     event,values=window.read()
     print(event,values)
     return(event,values)

