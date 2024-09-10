import main1
import PySimpleGUI as sg
import mysql.connector as mc
import pandas as pd
def update_():
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
          [sg.Button('update')],[sg.Button('back')]]
  staff_window = sg.Window('reschedule',layout,size=(1500,500))
  staff_event , staff_value = staff_window.read()
  print(staff_event,staff_value)
  if staff_event=='Table':
        data_selected=[records_staff[row] for row in staff_value[staff_event]]
        print(data_selected[0][0])
        selected_row = staff_value['Table'][0]
        staff_window.Element('sr').Update('Selected Row: %s' % selected_row)
  if staff_event=='update':
      col1=[[sg.Text('boarding_time')],[sg.Input()]]
      col2=[[sg.Text('flight_no')],[sg.Input()]]
      layout=[[sg.Column(col1)],[sg.Column(col2)],[sg.Button('update')],[sg.Button('back')]]
      window=sg.Window('AIRLINE RESERVATION SYSTEM',layout).finalize()
      event,value=window.read()
      print(event,value)
      if event=='update':
       cursor.execute('UPDATE mytable SET boarding_time=%s WHERE flight_no=%s',(value[0],value[1]))
       sg.popup('boarding time updated')
       event2,values2=window.read()
       print(event2,values2)
       mydb.commit()
      if event=='back':
        import update_
        e,v=update_.update_()
        print(e,v)
  if staff_event=='back':
    import admin11
    e,v=admin11.admin11()
    print(e,v)
    

