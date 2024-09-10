import pandas as pd
import PySimpleGUI as sg
import mysql.connector as mc
def flight_screen():
  mydb=mc.connect(host="localhost",
                database= "airline_reservation_system",
                user="root",
                password="root");
  cursor=mydb.cursor()
  selected_row=None
  cursor.execute("SELECT  flight_no,airlines,departure,arrival,boarding_time,price FROM mytable ;")
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
          [sg.Button('Book')],[sg.Button('back')]]
  staff_window = sg.Window('booking',layout,size=(1500,500))
  while True:
   staff_event , staff_value = staff_window.read()
   print(staff_event,staff_value)
   if staff_event=='Table':
        data_selected=[records_staff[row] for row in staff_value[staff_event]]
        print(data_selected[0][0])
        selected_row = staff_value['Table'][0]
        staff_window.Element('sr').Update('Selected Row: %s' % selected_row)
   if staff_event=="Book":
        print("Yes")
        sg.popup("Airline flight is booked in the flight No,",data_selected[0][0],image='bs.gif')
        qry=("INSERT INTO bh(flight_no,airlines,departure,arrival,boarding_time,price)VALUES (%s,%s,%s,%s,%s,%s)")
        cursor.execute(qry,(data_selected[0][0],data_selected[0][1],data_selected[0][2],data_selected[0][3],data_selected[0][4],data_selected[0][5]))
        mydb.commit()           
   if staff_event=='back':
     import main2
     e,v=main2.main2()
     print(e,v)
  

