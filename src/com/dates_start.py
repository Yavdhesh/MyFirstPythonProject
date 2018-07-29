#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
from datetime import date
from datetime import time
from datetime import datetime
import first

def main():
 today=date.today();
 dae=datetime.now();
 doo=datetime.time(datetime.now())
 print "hello",today;
 print "hello",today.day;
 print "hello",date.today().day,date.today().month,date.today().year;
 print "hello",dae;
 print "hello",doo;
 deedee=date.weekday(date.today())
 print "hello",deedee;
 
 d1=date.today();
 d1.month;
 d1.day;
 d1.year
 d2=datetime.now(); 
d3=datetime.time(datetime.now())
datetime.weekday(datetime.now())  
if __name__ == "__main__":
  main();
  for x in [1,2,3,4,5]:
      print "I am",x;
  map={'a':"lala",'b':"bala"};
  list=[1,2,3,4,5,6];
  map['a'];
  print map["b"];
  
  tuple=("gopla",1,"manupal","chaupal",1.5);
  
  date.today();
  datetime.now();
  datetime.time(datetime.now());
  
  map0={1,2,3};
  cmap=(4,5,6);
  d=( map0, cmap);
  print d;
  map0.update(cmap);
  print map0;
  
  mapDu={'papa':'lapa','bapa':'blapa','gapa':'mlbapa'};
  
  gepdu={'mama':'reddy','bmama':'haridhar','Shri':'Ram'};
  
  gepdu.update(mapDu);
  print gepdu.has_key("Shri");
  print gepdu.has_key("papa");
  print gepdu;
  
  for t in tuple:
      print t;
  set={"a",'b',"c"};
  print 'baba' in set;
  