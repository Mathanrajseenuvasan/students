from connection_code import *
import re
class Student():
    
    def __init__(self):
        try:
            x = int(raw_input("< 1 > Register \n< 2 > Update \n< 3 > Delete \n< 4 > View Registered Details"))
            
            if x == 1 :
                self._Student__user()
            elif x == 2:
                self._Student__update()
            elif x == 3:
                self._Student__delete()
            elif x == 4:
                self._Student__changes()
            else:
                print('Sorry, we are unable to understand ')
                self.__init__()
        except ValueError:
            print("OOPS Error\nPlease select correct value")
            self.__init__()

    def encap(self,newname,newage):
        self.__name = newname
        self.__age = newage

            
    def __user(self):
        newname = raw_input("Enter name: ")

        if newname.isalpha() == True:
            newage= raw_input("Enter age: ")
        else:
            print("Enter valid name")
            self._Student__user()

        cursor.execute("INSERT INTO students(name, age) VALUES (%s, %s)" , (newname,newage))
        print('Successfully registered')
        x = int(raw_input("Press 1 to home\nPress any other number to exit\n"))
        if x == 1:
            self.__init__()
        else:
            exit
    
    def __delete(self):
        newname = raw_input("Enter name: ")
        sql = "DELETE FROM students WHERE name = %s"
        adr = (newname, )
        cursor.execute(sql, adr)
        x = int(raw_input("Press 1 to check details < deleted or not >\nPress any other number to exit\n"))
        if x == 1:
            self._Student__changes()
        else:
            exit

    def __update(self):
        newname = raw_input("Enter name to update age: ")
        newage = raw_input("Enter age: ")
        sql = "UPDATE students SET age = %s WHERE name = %s"
        adr = (newage,newname, )
        cursor.execute(sql, adr)
        x = int(raw_input("Press 1 to check details < updated or not >\nPress any other number to exit\n"))
        if x == 1:
            self._Student__changes()
        else:
            exit 

    def __changes(self):
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)
        x = int(raw_input("Press 1 to home\nPress any other number to exit\n"))
        if x == 1:
            self.__init__()
        else:
            exit

emp = Student()  
db.commit()