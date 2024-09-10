import PySimpleGUI as sg
sg.theme('Dark Brown')
a=[sg.Text('WELCOME TO ARS', size=(40, 1), font=('Any 15'))]
b=[sg.Image('WELCOME.png')]
c=[sg.Button('enter')]
layout=[a,b,c]
window=sg.Window('WELCOME SCREEN',layout,element_justification='c',text_justification='c')
event,value=window.read()
print(event,value)
if event=='enter':
   import entry
   event1,values=entry.entry()
   print(event1,values)
