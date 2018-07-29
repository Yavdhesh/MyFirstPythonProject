'''
Created on Dec 7, 2017

@author: hp
'''
from first import  arg1

class myClass():
   
    def myClass(self):
        print("constructor myclass")
        
class newmyclass(myClass):
    def myClass(self):
        myClass.myClass(self)  
        print("newmyclass")
        
def main():
    c=myClass()
    c1=newmyclass()
    c1.myClass()
    print arg1;
    
main()

def newPopat():
    print "hello"
    
    
newPopat();    