import PySimpleGUI as sg
import mysql.connector as mc
import logindef
import empdef
import userdef
import signupdef
import stats
def entry():
 event,values=logindef.login()
 if event=='admin':
    event1,values1=empdef.emp()
    mydb=mc.connect(
          host='localhost',
          database='airline_reservation_system',
          user='root',
          password='root'
            )
    cursor=mydb.cursor()
    print(event1,values1)
    cursor.execute
    if event1 == 'login':
        cursor.execute('SELECT * FROM admin_login WHERE admin_id = %s AND password_ = %s',(values1[0],values1[1]))
        record=cursor.fetchall()
        print(record)
        print(cursor.rowcount)
        if cursor.rowcount==1:
             sg.popup('login successful')
             print(event,values)
             import admin11
             event,values=admin11.admin()
             print(event,values)
        else:
            sg.popup('invalid credentials')
            
    else:
       import entry
       event,values=entry.entry()
       print(event,values)
 elif event== 'user':
    event2,values2=userdef.user()
    mydb=mc.connect(
        host='localhost',
        database='airline_reservation_system',
        user='root',
        password='root'
        )
    cursor=mydb.cursor()
    print(event2,values2)
    if event2=='signin':
        cursor.execute('SELECT*FROM user_login WHERE user_id=%s AND password_=%s',(values2[0],values2[1]))
        record=cursor.fetchall()
        print(record)
        print(cursor.rowcount)
        if cursor.rowcount==1:
            sg.popup('signin successful')
            print(event2,values2)
            import main2
            event,values=main2.main2()
            print(event,values)
        else:
            sg.popup('invalid credentials')
    else:
        import entry
        event,values=entry.entry()
        print(event,values)
 elif event=='user signup' :
    event3,values3=signupdef.signup()
    mydb=mc.connect(
        host='localhost',
        database='airline_reservation_system',
        user='root',
        password='root'
        )
    cursor=mydb.cursor()
    print(event3,values3)
    if event3 == 'signup':
        cursor.execute('INSERT INTO usersignup(_name,_password,phone_no,email) VALUES (%s,%s,%s,%s)'
                       ,(values3[0],values3[1],values3[2],values3[3]))
        cursor.execute('INSERT INTO user_login(user_id,password_) VALUES (%s,%s)'
                       ,(values3[0],values3[1]))
        mydb.commit()
        sg.popup('signup successful',image='signup1.png')
        import entry
        event,values=entry.entry()
        print(event,values)
    if event3=='back':
        import entry
        e,v=entry.entry()
        print(e,v)
 elif event=='stats':
     e,v=stats.stats()
     print(e,v)
 return(event,values)


             
        

           
       
    

 
 
  

