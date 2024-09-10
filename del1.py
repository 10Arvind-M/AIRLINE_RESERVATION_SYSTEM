import PySimpleGUI as sg
import mysql.connector as mc
import pandas as pd
import main1
def del1():
 mydb=mc.connect(host="localhost",
                database= "airline_reservation_system",
                user="root",
                password="root");
 cursor=mydb.cursor()
 cursor.execute("SELECT  flight_no,airlines,departure,arrival,boarding_time,price FROM bh ;")
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
          [sg.T('Selected Row: None ', key='sr')],
          [sg.Button('cancel flight')],[sg.Button('back')]]
 staff_window = sg.Window('delete',layout,size=(1500,500))
 staff_event , staff_value = staff_window.read()
 print(staff_event,staff_value)
 staff_event , staff_value = staff_window.read()
 print(staff_event,staff_value)
 if staff_event=='Table':
        data_selected=[records_staff[row] for row in staff_value[staff_event]]
        print(data_selected[0][0])
        selected_row = staff_value['Table'][0]
        staff_window.Element('sr').Update('Selected Row: %s' % selected_row)
 if staff_event == 'cancel flight':
      col1=[[sg.Text('flight_no')],[sg.Input()]]
      layout=[[sg.Column(col1)],[sg.Button('delete')],[sg.Button('back')]]
      window=sg.Window('AIRLINE RESERVATION SYSTEM',layout).finalize()
      event,value=window.read()
      print(event,value)
      if event=='delete':
       cursor.execute('DELETE FROM bh WHERE flight_no=%s',(value[0],))
       col=[sg.Image('cancel.png')]
       layout=[[sg.popup('ticket cancelled',value[0],image='cancel.gif')]]
       window=sg.Window('cancellation',layout)
       event,values=window.read()
       print(event,values)
       mydb.commit()
       return(event,values)
      if event=='back':
         import del1
         e,v=del1.del1()
         print(e,v)
 if staff_event=='back':
     import main2
     event,values=main2.main2()
     print(event,values)
 
