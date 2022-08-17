from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
from tkinter import ttk
import globalvar
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
        for F in (StudentMainMenu, LateForm, EarlyDismissal,UniformPass):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.place(x=0,y=0,width=350,height=400)
            

        self.show_frame("StudentMainMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    

class StudentMainMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        lbl = Label(self, text="Student Menu", font= ("Helvetica", 23))
        lbl.place(x=110 , y=5)

        Late = Button(self, text= "Late Pass", font= ("Helvetica", 12), width= 15, bg = "#3357ad", fg= "White",command=lambda: controller.show_frame("LateForm"))
        Early = Button(self, text= "Early Dismissal", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White", command=lambda: controller.show_frame("EarlyDismissal"))
        Uniform = Button(self, text= "Uniform Pass", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda: controller.show_frame("UniformPass"))
        History = Button(self, text= "History", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda: StudentMainMenu.History(self))
        Log_out = Button(self, text= "Log out", font= ("Helvetica", 12), width = 8, bg = "#f02f28", fg= "White",command=lambda: Main.quit(self))

        Late.place(x=120 , y=80 )
        Early.place(x=120 , y=130 )
        Uniform.place(x=120 , y=180 )
        History.place(x=120 , y=230 )
        Log_out.place(x= 20, y= 300)

    def History(self):
        forms = open("forms.csv")
        window = Tk()
        window.title('Swiftform - History')
        window.iconbitmap("Images/Logo.ico")
        window.geometry('1200x250')
        window.resizable(0,0)
        # define columns
        columns = ('date','homegroup', 'formType', 'formReason','parentSig','isConfirmed')
        tree = ttk.Treeview(window, columns=columns, show='headings')
        # define headings
        tree.heading('date', text='Date')
        tree.heading('formType', text='Form Type')
        tree.heading('homegroup', text='Student Form Group')
        tree.heading('formReason', text='Reason')
        tree.heading('parentSig',text='Signature Given?')
        tree.heading('isConfirmed',text='Confirmed/Denied')
        # generate sample data
        infoForms = []
        for line in forms.readlines():
            readUsername = line.split(',')[0]
            if readUsername == globalvar.username:
                infoForms.append(line.split(',')[1:len(line.split(','))])
        # add data to the treeview
        for form in infoForms:
            tree.insert('', END, values=form)
        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                messagebox.showinfo(title='Information', message=','.join(record))
        tree.bind('<<TreeviewSelect>>', item_selected)
        tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

class LateForm(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        #Labels
        title = Label(self, text="Late Pass", font= ("Helvetica", 23))
        title.place(x=140 , y=5)
        Codeentry = Label(self, text="Student Code:", font= ("Helvetica", 12))
        Codeentry.place(x=25 , y=80)
        Formentry = Label(self, text="Form Group:", font= ("Helvetica", 12))
        Formentry.place(x=25 , y=120)
        reasonentry = Label(self, text="Reason:", font= ("Helvetica", 12))
        reasonentry.place(x=60 , y=160)
        teacherentry = Label(self, text="Teacher Code:", font= ("Helvetica", 12))
        teacherentry.place(x=20 , y=200)
        #Text Fields
        Student_ID = Entry(self, font= ("Helvetica", 18), width= 18)
        Student_ID.insert(END,globalvar.username)
        Student_Form = Entry(self, font= ("Helvetica", 18), width= 18)
        Reason = Entry(self, font= ("Helvetica", 18), width= 18)
        Teacher = Entry(self, font= ("Helvetica", 18), width= 18)
        Student_ID.place(x=135, y=80)
        Student_Form.place(x=135, y=120)
        Reason.place(x=135, y=160)
        Teacher.place(x=135, y=200)

        #Buttons
        Submit_Button = Button(self, text= "Submit", font= ("Helvetica", 12), width= 10, bg = "#3357ad", fg= "White",
        command= lambda: submit(Student_ID.get(),"Late Pass",Student_Form.get(),Reason.get()))
        Back = Button(self, text= "Back", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda: controller.show_frame("StudentMainMenu"))
        Upload = Button(self, text= "Upload Signature", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White")
        Submit_Button.place(x=250 , y=310 )
        Back.place(x=2 , y=310 )
        Upload.place(x=2 , y=275 )

class EarlyDismissal(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        lbl = Label(self, text="Early Dismissal", font= ("Helvetica", 23))
        lbl.place(x=100 , y=5)
        Codeentry = Label(self, text="Student Code:", font= ("Helvetica", 12))
        Codeentry.place(x=25 , y=80)
        Formentry = Label(self, text="Form Group:", font= ("Helvetica", 12))
        Formentry.place(x=25 , y=120)
        reasonentry = Label(self, text="Reason:", font= ("Helvetica", 12))
        reasonentry.place(x=40 , y=160)
        teacherentry = Label(self, text="Teacher Code:", font= ("Helvetica", 12))
        teacherentry.place(x=20 , y=200)
        #entry fields
        Student_ID = Entry(self, font= ("Helvetica", 18), width= 18)
        Student_ID.insert(END,globalvar.username)
        Student_Form = Entry(self, font= ("Helvetica", 18), width= 18)
        Reason = Entry(self, font= ("Helvetica", 18), width= 18)
        Teacher = Entry(self, font= ("Helvetica", 18), width= 18)
        Student_ID.place(x=135, y=80)
        Student_Form.place(x=135, y=120)
        Reason.place(x=135, y=160)
        Teacher.place(x=135, y=200)

        #buttons
        Submit = Button(self, text= "Submit", font= ("Helvetica", 12), width= 10, bg = "#3357ad", fg= "White",
        command=lambda: submit(Student_ID.get(),"Early Dismissal",Student_Form.get(),Reason.get(),""))
        Back = Button(self, text= "Back", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda: controller.show_frame("StudentMainMenu"))
        Upload = Button(self, text= "Upload Signature", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White")
        Submit.place(x=250 , y=310 )
        Back.place(x=2 , y=310 )
        Upload.place(x=2 , y=275 )   

class UniformPass(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Label
        lbl = Label(self, text="Uniform Pass", font= ("Helvetica", 23))
        lbl.place(x=120 , y=5)
        Codeentry = Label(self, text="Student Code:", font= ("Helvetica", 12))
        Codeentry.place(x=25 , y=80)
        Formentry = Label(self, text="Form Group:", font= ("Helvetica", 12))
        Formentry.place(x=25 , y=120)
        reasonentry = Label(self, text="Reason:", font= ("Helvetica", 12))
        reasonentry.place(x=40 , y=160)
        teacherentry = Label(self, text="This pass expires after one day", font= ("Helvetica", 12))
        teacherentry.place(x=4 , y=320)
        #entry fields
        Student_ID = Entry(self, font= ("Helvetica", 18), width= 18)
        Student_ID.insert(END,globalvar.username)
        Student_Form = Entry(self, font= ("Helvetica", 18), width= 18)
        Reason = Entry(self, font= ("Helvetica", 18), width= 18)
        Student_ID.place(x=135, y=80)
        Student_Form.place(x=135, y=120)
        Reason.place(x=135, y=160)
        #buttons
        Submit = Button(self, text= "Submit", font= ("Helvetica", 12), width= 10, bg = "#3357ad", fg= "White",
        command=lambda: submit(Student_ID.get(),"Uniform Pass",Student_Form.get(),Reason.get()))
        Back = Button(self, text= "Back", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda: controller.show_frame("StudentMainMenu"))
        Upload = Button(self, text= "Upload Signature", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White")
        Submit.place(x=250 , y=280 )
        Back.place(x=2 , y=280 )
        Upload.place(x=2 , y=245 )
       

def submit(studentID,formType,formGroup,formReason, parentSig="",confirmed=False,date=globalvar.current_date):
    info = str(studentID),str(date),str(formGroup),str(formType),str(formReason),str(parentSig),str(confirmed)
    forms = open("forms.csv",'a')
    forms.write(','.join(info) + '\n')
    messagebox.showinfo('Form Submitted', 'Your form has successfully been submitted!')

def run():
    app = Main()
    app.resizable(0,0)
    app.geometry("405x355")
    app.iconbitmap("Images/Logo.ico")
    app.title("Swiftform - Student Menu")
    app.mainloop()
