import sqlite3,time
#conn = sqlite3.connect('Database software.db')
#c = conn.cursor()
#for row in c.execute('SELECT * FROM `user`'):
#        print (row[0])
def login(usern,passw):
        while True:
                username = usern
                password = passw
                with sqlite3.connect("Database software.db") as db:
                        cursor = db.cursor()
                        find_user = ('SELECT * FROM user WHERE username =? and password =?')
                        cursor.execute(find_user,[(usern),(passw)])
                        results = cursor.fetchall()

                        if results:
                            for i in results:
                                print("Welcome" +username)
                            return 1
                            
                        else:
                            print("username or password is not correct.")
                            #again = input("do you want to try again?(y/n): ")
                            #if again.lower() == "n":
                            #    print('goodbye')
                            #    time.sleep(1)
                            return 0
                
