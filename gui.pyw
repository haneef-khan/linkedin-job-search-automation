from tkinter import *
import botLogin


screen=Tk();

def sendCredentials():
    
    user = str(username.get())
    pwd  = str(password.get())

    

    #Calling 
    botLogin.mainLogin(username,password,keyword,location)
   # screen.destroy()

#GUI for Login
def main_screen():
   
    global username, password, keyword, location
    global username_input, password_input, keyword_input, location_input

    screen.geometry('210x265')
    screen.title('Linkedin login')

    Label(screen,text="").grid(row = 0)

    
    username = StringVar()
    password = StringVar()
    keyword  = StringVar()
    location = StringVar()
    
    
    Label(screen,text = 'Username: ').grid(row = 2)
    username_input = Entry(screen,textvariable = username).grid(row = 2,column=1)

    Label(screen,text="").grid(row = 3)
    Label(screen,text = 'Password: ').grid(row = 4)
    password_input = Entry(screen,textvariable = password,show='*').grid(row = 4,column=1)


    Label(screen,text="").grid(row = 5)
    Label(screen,text = 'Job Title: ').grid(row = 6)
    keyword_input = Entry(screen,textvariable = keyword).grid(row = 6,column=1)

    Label(screen,text="").grid(row = 7)
    Label(screen,text = 'Location: ').grid(row = 8)
    location_input = Entry(screen,textvariable = location).grid(row = 8,column=1)
    
    Label(screen,text="").grid(row = 9)

    screen.bind("<Return>",lambda click:sendCredentials())    
    Button(screen,text="Submit",width=10,height=1,command=sendCredentials).grid(row=10,column=1)

       
    screen.mainloop()
    


main_screen()

