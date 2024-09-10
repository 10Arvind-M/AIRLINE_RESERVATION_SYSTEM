import PySimpleGUI as sg
import mysql.connector as mc
import pandas as pd
import datetime
def main2():
 sg.ChangeLookAndFeel('Dark')
 combobox = sg.InputCombo(values=['BOOK FLIGHT','CANCEL TICKET','BOOKING HISTORY'], size=(100,105))
 layout =  [[sg.Image('user_s.png')],[sg.Text('WELCOME USER', size=(40, 1), font=('Any 15'))],
                
                [sg.T('SELECT'), combobox, sg.Button('go')],
                [sg.Button('Exit', button_color=('white', 'firebrick3'))]
                ]

 window = sg.Window('user', element_justification='c',text_justification='c', default_element_size=(15,1), font=('Any 14')).Layout(layout)
 event, values = window.Read()
 if event=='Exit':
        import entry
        e,v=entry.entry()
        print(e,v)
 if values[1] == 'BOOK FLIGHT':
                import main1
                event,values=main1.flight_screen()
                print('Getting list of subtitles....')
                print('Done')
 elif values[1]=='BOOKING HISTORY':
                mydb=mc.connect(host="localhost",
                database= "airline_reservation_system",
                user="root",
                password="root");
                cursor=mydb.cursor()
                selected_row=None
                cursor.execute("SELECT flight_no,airlines,departure,arrival,boarding_time,price FROM bh NATURAL JOIN air_no ")
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
                staff_window = sg.Window('bookings',layout,size=(1500,500))
                staff_event , staff_value = staff_window.read()
                print(staff_event,staff_value)
                if staff_event=='Table':
                           data_selected=[records_staff[row] for row in staff_value[staff_event]]
                           print(data_selected[0][0])
                           selected_row = staff_value['Table'][0]
                           staff_window.Element('sr').Update('Selected Row: %s' % selected_row)
                if staff_event=='back':
                            import main2
                            e,v=main2.main2()
                            print(e,v)
 else:
                import del1
                event,value=del1.del1()
                print(event,value)
 







      
