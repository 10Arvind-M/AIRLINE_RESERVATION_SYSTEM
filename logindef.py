import PySimpleGUI as sg
import mysql.connector as mc
def login():
 col1=[[sg.Button('admin',image_filename='admi.png',image_size=(150, 150))]]
 col2=[[sg.Button('user',image_filename='dwjyaf.png',image_size=(150, 150))]]
 col3=[[sg.Button('user signup',image_filename='images.png',image_size=(150, 150))]]
 col4=[[sg.Button('stats',image_filename='download.png',image_size=(150, 150))]]
 column1=[[sg.Column(col1,background_color='white'),sg.Column(col2,background_color='black'),
          sg.Column(col3,background_color='black'),sg.Column(col4,background_color='black')]]
 column2=[[sg.Image('fli.png',size=(500,300))]]
 layout=[[column1,column2]]
 window=sg.Window ('AIRLINE RESERVATION SYSTEM',layout,keep_on_top=True,element_justification='c')
 event,values=window.read()
 print(event,values)
 return(event,values)

