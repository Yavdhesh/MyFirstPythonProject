'''
Created on Dec 24, 2017

@author: hp
'''

if __name__ == '__main__':
    Map={'a':"b",'b':"a",'c':"d",'d':"c"};
    print Map;
    
    b=55;
    a=95;
    Map2={'a':b,'b':a};
    print Map2;
    
    print Map2.get('a')
    
    print Map2.iterkeys();
    
    #we can iterate keys
    for x in Map2.iterkeys():
        print Map2[x];
        
    print Map2.__len__();
    
    print Map2.itervalues()
    
    # we can iterate values
    for x in Map2.itervalues():
        print x;
    
    print Map.items();
    
    for x in Map.items():
        for y in x:
            print y;
            
    # if there's no element
    print Map.get("x");
   
    
    if('None'== Map.get('x')):
        print "Ha ji"