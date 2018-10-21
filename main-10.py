#Created for the McMaster Engineering Competition, Group 98
#This defines the libraries and outside functions used in our program
from tkinter import *
from tkinter import messagebox
import pyttsx3;

#Did not have enough time to implement
#from twilio.rest import TwilioRestClient


class Window(Frame):

    #creates a window where our function is implemented
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
    #Defines the function of our text to speech implementation, takes string of text in the text box.    
    def regButton(self):
        text = self.e1.get()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    

    #Implementation of pre-determined words, inserts the string in our text box for speech interpretation  
    def OY(self):
        
        self.e1.insert(END, "Oh Yeah")
        
    def WO(self):
        
        self.e1.insert(END, "Wow")

    def BY(self):
        
        self.e1.insert(END, "Bye")

    def WT(self):
        
        self.e1.insert(END, "I need water")
        
    def FD(self):
        
        self.e1.insert(END, "I need food")

    def HL(self):
        
        self.e1.insert(END, "Hello")
    def TY(self):
        
        self.e1.insert(END, "Thank you")
    def FN(self):
        
        self.e1.insert(END, "Fine")
    def s(self):
        
        self.e1.insert(END, "Sorry")

    def auk(self):
        self.e1.insert(END, "Are you kidding me?")

    def y(self):
        self.e1.insert(END, "Yes")

    def n(self):
        self.e1.insert(END, "No")

    def em(self):
        self.e1.insert(END, "Excuse me")

    #End of pre-determined word buttons

    #Start of keyboard buttons, this inserts the character in our text box

    def p(self):
        self.e1.insert(END, "Please")


    def Q(self):
        self.e1.insert(END,"q")
        
    def W(self):
        self.e1.insert(END,"w")
    def E(self):
        self.e1.insert(END,"e")
    def R(self):
        self.e1.insert(END,"r")
    def T(self):
        self.e1.insert(END,"t")
    def Y(self):
        self.e1.insert(END,"y")  
    def U(self):
        self.e1.insert(END,"u")
    def I(self):
        self.e1.insert(END,"i")    

    def O(self):
        self.e1.insert(END,"o")
    def P(self):
        self.e1.insert(END,"p")
    def A(self):
        self.e1.insert(END,"a")

    def S(self):
        self.e1.insert(END,"s")

    def D(self):
        self.e1.insert(END,"d")
    def F(self):
        self.e1.insert(END,"f")
    def G(self):
        self.e1.insert(END,"g")

    def H(self):
        self.e1.insert(END,"h")
    def J(self):
        self.e1.insert(END,"j")

    def K(self):
        self.e1.insert(END,"q")

    def L(self):
        self.e1.insert(END,"l")

    def Z(self):
        
        self.e1.insert(END,"z")

    def X(self):
        
        self.e1.insert(END,"x")

    def C(self):
        
        self.e1.insert(END,"c")
    def V(self):
       
        self.e1.insert(END,"v")
    def B(self):
        
        self.e1.insert(END,"b")
    def N(self):
        
        self.e1.insert(END,"n")   

    def M(self):
        self.e1.insert(END,"m")



    def space(self):
        self.e1.insert(END," ")
    def clear(self):
        self.e1.delete(0, END)

    #End of keyboard buttons

    #Defines the function of our emergency button, adds text to screen that emergency contact has been notified

    def emerg(self):
        self.e1.insert(END,"Your Emergency Contact has been notified")
        #############################################
        #here is where our sms send code would go, it would implement twilio api to send a text message
        #from a users phone, to a destination phone that is chosen by the user.
        #We did not have the time to implement properly so we removed it.

	
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Welcome")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        
        large_font = ('Verdana',30)
        median_font = ('Verdana',20)

        bName = Label(self, text="Text to enter",font=median_font)
        bName.place(x=0,y=30)
        
        
        self.e1=Entry(self,width=100,font=large_font)
        self.e1.place(x=220,y=30)

        #self.e2=Entry(self)
        #self.e2.place(x=110,y=100)

        ClearButton = Button(self, text="Clear",font=large_font,command = self.clear)
        ClearButton.place(x= 500,y = 100)
                

        # creating a button instance
        regButton = Button(self, text="Text to Speech", font=large_font,command=self.regButton)
        regButton.place(x=30, y=100)

        WO = Button(self, text="WOW",font=median_font,command=self.WO)
        WO.place(x=300,y=200)
        
        OY = Button(self, text="Oh Yeah",font=median_font,command=self.OY)
        OY.place(x=300, y=300)

        y=Button(self,text="Yes",font=median_font,command=self.y)
        y.place(x=400,y=200)
        
        n=Button(self,text="No",font=median_font,command=self.n)
        n.place(x=400,y=300)

        HL = Button(self, text="Hello",font=median_font,command=self.HL)
        HL.place(x=500, y=200)

        BY = Button(self, text="Bye",font=median_font,command=self.BY)
        BY.place(x=500, y=300)
        

        WT = Button(self, text="Water",font=median_font,command=self.WT)
        WT.place(x=650, y=300)

        FD = Button(self, text="Food",font=median_font,command=self.FD)
        FD.place(x=650, y=200)


        FN = Button(self, text="Fine",font=median_font,command=self.FN)
        FN.place(x=800, y=200)


        em=Button(self,text="Excuse me",font=median_font,command=self.em)
        em.place (x=800,y=300)

        TY = Button(self, text="Thank you",font=median_font,command=self.TY)
        TY.place(x=1000, y=200)

        p=Button(self,text="Please",font= median_font,command=self.p)
        p.place(x=1000,y=300)

        auk=Button(self,text="Are you kidding",font=median_font,command=self.auk)
        auk.place(x=1200,y=200)



        keyboard = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']



        
        tmp = 0
        
        a = {}
        

        count = 1
        i = keyboard[count - 1]
        a[1]=Button(self,text=i,font=median_font,command = self.Q)
        count = count + 1;
        i = keyboard[count - 1]
        a[2]=Button(self,text=i,font=median_font,command = self.W)
        count = count + 1;
        i = keyboard[count - 1]
        a[3]=Button(self,text=i,font=median_font,command = self.E)
        count = count + 1;
        i = keyboard[count - 1]
        a[4]=Button(self,text=i,font=median_font,command = self.R)
        count = count + 1;
        i = keyboard[count - 1]
        a[5]=Button(self,text=i,font=median_font,command = self.T)
        count = count + 1;
        i = keyboard[count - 1]
        a[6]=Button(self,text=i,font=median_font,command = self.Y)
        count = count + 1;
        i = keyboard[count - 1]
        a[7]=Button(self,text=i,font=median_font,command = self.U)
        count = count + 1;
        i = keyboard[count - 1]
        a[8]=Button(self,text=i,font=median_font,command = self.I)
        count = count + 1;
        i = keyboard[count - 1]
        a[9]=Button(self,text=i,font=median_font,command = self.O)
        count = count + 1;
        i = keyboard[count - 1]
        a[10]=Button(self,text=i,font=median_font,command = self.P)
        count = count + 1;
        i = keyboard[count - 1]
        a[11]=Button(self,text=i,font=median_font,command = self.A)
        count = count + 1;
        i = keyboard[count - 1]
        a[12]=Button(self,text=i,font=median_font,command = self.S)
        count = count + 1;
        i = keyboard[count - 1]
        a[13]=Button(self,text=i,font=median_font,command = self.D)
        count = count + 1;
        i = keyboard[count - 1]
        a[14]=Button(self,text=i,font=median_font,command = self.F)
        count = count + 1;
        i = keyboard[count - 1]
        a[15]=Button(self,text=i,font=median_font,command = self.G)
        count = count + 1;
        i = keyboard[count - 1]
        a[16]=Button(self,text=i,font=median_font,command = self.H)
        count = count + 1;
        i = keyboard[count - 1]
        a[17]=Button(self,text=i,font=median_font,command = self.J)
        count = count + 1;
        i = keyboard[count - 1]
        a[18]=Button(self,text=i,font=median_font,command = self.K)
        count = count + 1;
        i = keyboard[count - 1]
        a[19]=Button(self,text=i,font=median_font,command = self.L)
        count = count + 1;
        i = keyboard[count - 1]
        a[20]=Button(self,text=i,font=median_font,command = self.Z)
        count = count + 1;
        i = keyboard[count - 1]
        a[21]=Button(self,text=i,font=median_font,command = self.X)
        count = count + 1;
        i = keyboard[count - 1]
        a[22]=Button(self,text=i,font=median_font,command = self.C)
        count = count + 1;
        i = keyboard[count - 1]
        a[23]=Button(self,text=i,font=median_font,command = self.V)
        count = count + 1;
        i = keyboard[count - 1]
        a[24]=Button(self,text=i,font=median_font,command = self.B)
        count = count + 1;
        i = keyboard[count - 1]
        a[25]=Button(self,text=i,font=median_font,command = self.N)
        count = count + 1;
        i = keyboard[count - 1]
        a[26]=Button(self,text=i,font=median_font,command = self.M)
        count = count + 1;
        
      

        count = 1
        tmp1= 250
        tmp2=250
        tmp3=250
        for j in keyboard:
            if count<11:
              a[count].place(x=tmp1,y=400)
              tmp1= tmp1 + 50
              count = count + 1
            elif count<20:
                a[count].place(x=tmp2,y=450)
                tmp2= tmp2+ 50
                count = count + 1
            else:
                a[count].place(x=tmp3,y=500)
                tmp3= tmp3+ 50
                count = count + 1

        space = Button(self,text="Space",font=median_font,command = self.space,width=20)
        space.place(x=350,y=550)
        #HL = Button(self,text="Hello",font=medium)

        emerg=Button(self,text="Emergency",font=median_font,command=self.emerg)
        emerg.place(x=550,y=700)
        #logButton = Button(self, text="Log in")
        #slogButton.place(x=150, y=200)
        
   
          

root = Tk()

#size of the window
root.geometry("1920x1080")

app = Window(root)
root.mainloop()  
