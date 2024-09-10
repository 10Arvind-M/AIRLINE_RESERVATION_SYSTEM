import PySimpleGUI as sg
import mysql.connector as mc
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
def stats():
    sg.theme('Darkblue2')
    col1=[[sg.Button('airlines vs prices',image_filename='line.png',image_size=(150, 150))]]
    col2=[[sg.Button('bookings per airlines',image_filename='pie.png',image_size=(150,150))]]
    col3=[[sg.Button('airline vs employees&seats',image_filename='bar.png',image_size=(150, 150))]]
    column1=[sg.Column(col1,background_color='white'),sg.Column(col2,background_color='black'),
          sg.Column(col3,background_color='black')]
    layout=[[column1,[sg.Button('back')]]]
    window=sg.Window('stats',layout,element_justification='c')
    e,v=window.read()
    print(e,v)
    if e=='airlines vs prices':
        p=pd.read_csv("C:\\Users\\arvin\\Downloads\\flight.csv")
        print(p)
        pl.plot(p.flight_no,p.price,marker='p',label='price')
        pl.xlabel('flight_no')
        pl.ylabel('price')
        pl.title('flight_no vs prices graph')
        pl.legend()
        pl.grid(True)
        pl.xticks(size=5)
        pl.yticks(size=5)
        pl.show()
    elif e=='bookings per airlines':
        l=['INDIGO','AIR_INDIA','VISTARA','SPICEJET']
        pl.pie([2000,1900,3000,4000],labels=l)
        pl.title('flights & their bookings')
        pl.show()
    elif e=='airline vs employees&seats':
        a=pd.read_csv("C:\\Users\\arvin\\Downloads\\bar1.csv")
        k=a.AIRLINES
        b=a.EMPLOYEES
        c=a.SEATS
        x_axis = np.arange(len(k))
        pl.bar(x_axis -0,b,label='employees',width=0.1,color='red')
        pl.bar(x_axis +0.1,c,label='seats',width=0.1,color='blue')
        pl.xticks(x_axis,k)
        pl.yticks()
        pl.ylabel('no.of employees & no. of seats')
        pl.xlabel('airlines')
        pl.title('airlines vs no.of employees & no. of seats')
        pl.legend(loc=1)
        pl.show()
    elif e=='back':
        import entry
        event,values=entry.entry()
        print(event,values)
    return(e,v)


 



        
 



