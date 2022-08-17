#Import Tkinter
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
import globalvar, Student_Main_Menu, Teacher_Main_Menu
password = None
class Main(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (LogInMain, StudentLogIn,TeacherLogIn):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.place(x=0,y=0,width=400,height=200)
        self.show_frame("LogInMain")
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class LogInMain(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        lbl = Label(self, text="Log In", font= ("Helvetica", 23))
        lbl.place(x=152 , y=5)
        #Buttons
        student = Button(self, text= "Student", font= ("Helvetica", 23), bg="#3357ad", fg="#f02f28", command= lambda:controller.show_frame("StudentLogIn"))
        teacher = Button(self, text= "Teacher", font= ("Helvetica", 23), bg="#3357ad", fg="#f02f28",command= lambda:controller.show_frame("TeacherLogIn"))
        student.place(x=40 , y=86)
        teacher.place(x=230 , y=86)

class StudentLogIn(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        lbl = Label(self, text="Student Log In", font= ("Helvetica", 23))
        lbl.place(x=103 , y=5)
        namelbl = Label(self, text= "Username", font= ("Helvetica", 12))
        paslbl = Label(self, text="Password", font= ("Helvetica", 12))
        namelbl.place(x=60 , y=80)
        paslbl.place(x=60 , y=120)
        #text fields
        nametxt = Entry(self, text= "Username")
        pastxt = Entry(self, show="*")
        nametxt.place(x=150,y=80)
        pastxt.place(x=150,y=120)
        #buttons
        loginbtn = Button(self, text= "Log In", font= ("Helvetica", 12), width= 15, bg = "#3357ad", fg= "White",command=lambda:StudentLogIn.Login(nametxt.get(),pastxt.get()))
        backbtn = Button(self, text= "Back", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda:controller.show_frame("LogInMain"))
        loginbtn.place(x=250 , y=160 )
        backbtn.place(x=15 , y=160 )

    def Login(username,password):
        username = username.upper()
        isStudent = True
        logins = open("logins.csv")
        usernames = []
        for login in logins.readlines():
            login = login.split(',')
            usernames.append(login[0].upper())
        logins.close()
        logins = open("logins.csv")
        if (username in usernames): #Checks if the username is in STUDENT ID Format
            for login in logins.readlines(): #Goes through all the logins in CSV
                    storedpass = str(login).split(',')[1].strip()
                    if password == storedpass: #Finds and validates the password associated with the username
                        globalvar.username = username
                        Student_Main_Menu.run()
                        break
                    else:
                        messagebox.showerror('Wrong Password', 'Your password is invalid!')
                        break
        else:
            messagebox.showerror('Wrong Username', 'Your username is invalid!')
        logins.close()

class TeacherLogIn(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        lbl = Label(self, text="Teacher Log In", font= ("Helvetica", 23))
        lbl.place(x=103 , y=5)
        namelbl = Label(self, text= "Username", font= ("Helvetica", 12))
        paslbl = Label(self, text="Password", font= ("Helvetica", 12))
        namelbl.place(x=60 , y=80)
        paslbl.place(x=60 , y=120)
        #text fields
        nametxt = Entry(self, text= "Username")
        pastxt = Entry(self, show="*")
        nametxt.place(x=150,y=80)
        pastxt.place(x=150,y=120)
        #buttons
        loginbtn = Button(self, text= "Log In", font= ("Helvetica", 12), width= 15, bg = "#3357ad", fg= "White",command=lambda:TeacherLogIn.Login(nametxt.get(),pastxt.get()))
        backbtn = Button(self, text= "Back", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda:controller.show_frame("LogInMain"))
        loginbtn.place(x=250 , y=160 )
        backbtn.place(x=15 , y=160 )
    def Login(username,password):
        username = username.upper()
        logins = open("logins.csv")
        usernames = []
        for login in logins.readlines():
            login = login.split(',')
            usernames.append(login[0].upper())
        logins.close()
        logins = open("logins.csv")
        if (username in usernames):
            for login in logins.readlines(): #Goes through all the logins in CSV
                    storedpass = str(login).split(',')[1].strip()
                    if password == storedpass: #Finds and validates the password associated with the username
                        globalvar.username = username
                        Teacher_Main_Menu.run()
                        break
                    else:
                        messagebox.showerror('Wrong Password', 'Your password is invalid!')
                        break
        else:
            messagebox.showerror('Wrong Username', 'Your username is invalid!')
        logins.close()

def run():
    app = Main()
    app.resizable(0,0)
    app.geometry("400x200")
    app.title("Swiftform - Login Menu")
    app.iconbitmap("Images/Logo.ico")
    app.mainloop()

run()