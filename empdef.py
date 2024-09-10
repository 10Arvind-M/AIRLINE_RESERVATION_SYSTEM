import PySimpleGUI as sg
import mysql.connector as mc
def emp():
    col2=[[sg.Text('adminid')],[sg.Input('Username')]]
    col1= [[sg.Text('password')],[sg.Input('Password')]]
    layout=[[sg.Column(col2),sg.Column(col1)],[sg.Button('login'),sg.Button('back')],[sg.Image('admin1.png',size=(200,250))]]
    window=sg.Window('AIRLINE RESERVATION SYSTEM',layout,element_justification='c')
    event,values=window.read()
    print(event,values)
    return(event,values)
    

