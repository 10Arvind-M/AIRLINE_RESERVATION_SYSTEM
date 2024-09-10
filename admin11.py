import PySimpleGUI as sg
import mysql.connector as mc
import pandas as pd
import update_
def admin():
 sg.ChangeLookAndFeel('Dark')
 combobox = sg.InputCombo(values=['BOOKED FLIGHT','CANCEL FLIGHT','RESCHEDULE FLIGHT'], size=(100,105))
 layout =  [[sg.Image('admin_s.png')],
                [sg.Text('WELCOME ADMIN', size=(40, 1), font=('Any 15'))],
                [sg.T('SELECT'), combobox, sg.Button('go')],
                [sg.Button('Exit', button_color=('white', 'firebrick3'))]
                ]

 window = sg.Window('admin', text_justification='c',element_justification='c', default_element_size=(15,1), font=('Any 14')).Layout(layout)
 event,values=window.read()
 if event=='Exit':
        import entry
        e,v=entry.entry()
        print(e,v)
 if values[1]=='CANCEL FLIGHT':
   import del2
   event,values=del2.del2()
   print(event,values)
 elif values[1]=='BOOKED FLIGHT':
                mydb=mc.connect(host="localhost",
                database= "airline_reservation_system",
                user="root",
                password="root");
                cursor=mydb.cursor()
                cursor.execute("SELECT * FROM nam NATURAL JOIN bh ")
                record2 = cursor.fetchall()
                df2 = pd.DataFrame(record2,columns = list(cursor.column_names))
                df2['date']=pd.to_datetime('today').strftime("%m/%d/%Y")
                column_heading_staff = list(df2.columns)
                records_staff = df2.values.tolist()
                sg.theme('GreenMono')
                layout = [[sg.Table(values = records_staff,
                        headings = column_heading_staff,
                        auto_size_columns = True,
                        expand_x = True,
                        expand_y = True,
                        justification='center',
                        num_rows=20,
                        enable_events=True,
                        key = 'Table')
               ],
          [sg.T('Selected Row: None ', key='sr')],[sg.Button('back')]
          ]
                window = sg.Window('flights',layout,size=(1500,500))
                event,values=window.read()
                print(event,values)
                mydb.commit()
                if event=='back':
                  import admin11
                  e,v=admin11.admin()
                  print(e,v)
 else:
      import update_
      event,values=update_.update_()
      print(event,values)



    
                
