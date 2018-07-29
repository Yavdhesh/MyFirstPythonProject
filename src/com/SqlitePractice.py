'''
Created on Dec 24, 2017

@author: hp
'''
import sqlite3
from _sqlite3 import Cursor, Row

class DTOClass():
    def __init__(self,name,surname,address,state,empID):
        self.name=name;
        self.surname=surname;
        self.address=address;
        self.state=state;
        self.empID=empID;
        print name,surname,address,state,empID;
        
    def getConnection(self):
        
     return sqlite3.connect("exmaple.db");
    def insertData (self,name,surname,address,state,empID):
       var= self.getConnection().cursor().execute('''insert into mytable values ('''+"'"+name+"'"+''','''+"'"+surname+"'"+''','''+"'"+address+"'"+''','''+"'"+state+"'"+''','''+"'"+empID+"'"''')''');
       self.getConnection().commit();
       self.getConnection().close();
       return var;
    def selectData (self,empID):
      var= self.getConnection().cursor().execute('''select * from mytable where empID ='''+"'"+empID+"'");
      self.getConnection().close(); 
      return var; 
if __name__ == '__main__':
     connection=sqlite3.connect("example.db");
    
     cursor=connection.cursor();
    
  #  cursor.execute('''drop table mytable''');
  
   # cursor.execute('''CREATE TABLE mytable
    #        (name varchar, surname varchar, address varchar ,  state varchar,  empID varchar)''');
    # cursor.execute('''insert into mytable values
     #        ('yavdhesh', 'sanchihar', 'ShriNathdwara','Rajasthan', '1009045')''');
     #cursor.execute('''insert into mytable values
     #        ('Vijay', 'sanchihar', 'ShriNathdwara','Rajasthan', '4899323')''');
   #  cursor.execute('''CREATE TABLE mytable
    #        (name varchar, surname varchar, address varchar ,  state varchar,  empID varchar)''');cursor.execute('''insert into mytable values
     #        ('Sujay', 'sanchihar', 'ShriNathdwara','Rajasthan', '897870')''');
     #cursor.execute('''insert into mytable values
      #       ('Nariyal', 'sanchihar', 'ShriNathdwara','Rajasthan', '7878969')''');
             
    # cursor.execute('''insert into mytable values
     #        ('Always ', 'Reddy', 'ShriNathdwara','Rajasthan', '7898098')''');
    # cursor.execute('''insert into mytable values
     #        ('Haridhar', 'Hegde', 'Dawangere','Karnataka', '232324')''');
    # connection.commit();         
     a=cursor.execute(''' select * from mytable m  ''');
     map={};
     i=0;
     for row in a:
      c=DTOClass(row[0],row[1],row[2],row[3],row[4]);
      map['row'+str(i)]=c;
      i=i+1;
         
    