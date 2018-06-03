
import re
import types


class flames():

    def main(self):
        self.__init__()
        
    def __init__(self):
        self.text=list("FLAMES")
        self.trys=0
        self.menu() 
    def menu(self):
        
        print("FLAMES")
        print("1.Press S to start")
        print("2.Press Q to quit")
        self.ch=input("Enter the option:")
        self.check(self.ch)
    def check(self,ch1):
        if(str.isalpha(ch1)==True):
            self.startup(ch1)
        else:
            print("enter valid character")
            self.menu()
            
    def startup(self,ch2):
        
        if(self.trys!=3):
            if(ch2=="S" or ch2=="s"):
                self.flame()
            elif(ch2=="Q" or ch2=="q"):
                exit()
            else:
                print("enter valid input")
                self.trys=self.trys+1
                self.menu()
            
        else:
            print("Bloody Hell!!")
            exit()
            
                

    def flame(self):
        self.name1=input("Enter the first name:")
        
        self.name1=self.name1.strip()
        self.name1=str.lower(self.name1)
        
        self.name2=input("Enter the second name:")
        self.name2=self.name2.strip()
        self.name2=str.lower(self.name2)
        if(set("`~1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:',<.>/?+-*/.").intersection(self.name1) or set("`~1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:',<.>/?+-*/.").intersection(self.name2)):
            print("enter valid name")
            self.flame()
        else:
           
            tot=len(self.name1)+len(self.name2)
        
        self.n1=list(self.name1)
        
        self.n2=list(self.name2)
        
        l1=len(self.n1)
        l2=len(self.n2)
        self.lencalc(l1,l2)
        self.result()
    def lencalc(self,l1,l2):
        for i in range(0,l1):
            for j in range(0,l2):
                try:
                    if(self.n1[i]==self.n2[j]):
                        self.n1.remove(self.n1[i])
                        self.n2.remove(self.n2[j])
                    else:
                        continue
                except IndexError:
                    l1=l1-1
                    l2=l2-1
                    self.lencalc(l1,l2)
                finally:
                    self.totallen=len(self.n1)+len(self.n2)
        self.flgame(self.totallen)

    def flgame(self,clen):
        clen=self.totallen
        check=clen%len(self.text)
        if((check==0) or (check>clen)):
            clen=len(self.text)
        else:
            clen=check
        for i in range(0,clen):
            ivalue=i
        self.flcalc(ivalue,clen)
    def flcalc(self,ivalue1,clen1):
        cou=0
    
    
        while(len(self.text)!=1):
            try:
               from collections import deque
               text1=deque(self.text)
               text1.remove(text1[ivalue1])
               text1.rotate(len(text1)-ivalue1)
               self.text=list(text1)
               self.flgame(clen1)
        
            except IndexError:
                from collections import deque
                pseudo=(clen1-1)-len(self.text)
                self.text.pop((clen1-1)-len(self.text))
                text1=deque(self.text)
                text1.rotate(len(text1)-pseudo)
                self.text=list(text1)
                self.flgame(clen1)
            

    
        
        
    def result(self):
        for i in range(0,1):
            if(self.text[0]=='F'):
                print('{0} and {1} are FRIENDS'.format(self.name1,self.name2))
    
            elif(self.text[0]=='L'):
                print('{0} and {1} are LOVERS'.format(self.name1,self.name2))
        
            elif(self.text[0]=='A'):
                print('{0} and {1} are AFFECTIONIATE WITH EACH OTHER'.format(self.name1,self.name2))
            elif(self.text[0]=='M'):
                print('{0} and {1} are MARRIED or WEDDINGS BELLS ARE RINGING'.format(self.name1,self.name2))
            elif(self.text[0]=='E'):
                print('{0} and {1} are ENEMIES'.format(self.name1,self.name2))
            else:
                print('{0} and {1} are SIBLINGS'.format(self.name1,self.name2))
        
            
        
        
        
    
flames()
