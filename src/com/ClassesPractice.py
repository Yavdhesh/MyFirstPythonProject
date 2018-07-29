'''
Created on Dec 24, 2017

@author: hp
'''
import sqlite3
import SqlitePractice
from com.SqlitePractice import DTOClass

class OldExample(SqlitePractice.DTOClass):
    def __init__(self):
        SqlitePractice.DTOClass.__init__(self, "baba","lal", "natd", "Rajasthan", "1009044");
         
        self.appa='appa';
        print self.appa;
    def papa(self,*arg):
        for x in arg:
            print x;

class NewExample(OldExample):
    classVariable=7;
    def __init__(self):
       
        self.classVariable=75;
        print self.classVariable;
        OldExample.__init__(self);
        OldExample.papa(self,"gappu",'chappu');
        self.instace=999;
        

if __name__ == '__main__':
    c=NewExample();
    sq=SqlitePractice.DTOClass("Nathu","Tota", "Thawari", "Rajasthan", "111111");
   
    
    print sq.insertData("NathuBa", "RiLadi", "VicchuMagri", "Rajasthan", "123456");
    print sq.selectData("123456");
    v=sq.selectData("123456");
    l=sq.getConnection().cursor().execute("select * from mytable where empID='7878969'");
    map={};
    ind=0;
    for row in l:
       o= DTOClass(row[0],row[1],row[2],row[3],row[4]);
       print"oole"+o.name,o.surname;
       map['row'+ind]=o;
       ind=ind+1;

    print map;