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
        for F in (TeacherMainMenu, StudentList):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.place(x=0,y=0,width=350,height=225)
        self.show_frame("TeacherMainMenu")

    def Requests(self):
        forms = open("forms.csv")
        window = Tk()
        window.title('Swiftform - History')
        window.iconbitmap("Images/Logo.ico")
        window.geometry('1200x250')
        window.resizable(0,0)
        # define columns
        columns = ('studentId','date','homegroup', 'formType', 'formReason','parentSig','isConfirmed')
        tree = ttk.Treeview(window, columns=columns, show='headings')
        # define headings
        tree.heading('studentId', text='Student ID')
        tree.heading('date', text='Date')
        tree.heading('formType', text='Form Type')
        tree.heading('homegroup', text='Student Form Group')
        tree.heading('formReason', text='Reason')
        tree.heading('parentSig',text='Signature Given?')
        tree.heading('isConfirmed',text='Confirmed/Denied')
        # generate sample data
        infoForms = []
        for line in forms.readlines():
            infoForms.append(line.split(','))
        # add data to the treeview
        for form in infoForms:
            tree.insert('', END, values=form)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                EditFormDetails(item['values'])

        tree.bind('<<TreeviewSelect>>', item_selected)
        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        #Tkinter Menu Bar

        def EditFormDetails(item):
            #WINDOW
            window = Tk()
            window.geometry("400x250")
            window.resizable(0,0)
            window.iconbitmap("Images/Logo.ico")
            #LABELS
            studentID = Label(window, text="Student ID: " + str(item[0]), font= ("Helvetica", 12))
            studentID.place(x=10 , y=10)
            date = Label(window, text="Date: " + str(item[1]), font= ("Helvetica", 12))
            date.place(x=10 , y=40)
            studentFormGroup = Label(window, text="Form Group: " + str(item[2]), font= ("Helvetica", 12))
            studentFormGroup.place(x=10 , y=70)
            formType = Label(window, text="Form Type: " + str(item[3]), font= ("Helvetica", 12))
            formType.place(x=10 , y=100)
            reason = Label(window, text="Reason: " + str(item[4]), font= ("Helvetica", 12))
            reason.place(x=10 , y=100)
            window.mainloop()




    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
class TeacherMainMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        #Label
        lbl = Label(self, text="Teacher Menu", font= ("Helvetica", 23))
        lbl.place(x=120 , y=5)
        #buttons
        Students = Button(self, text= "Students", font= ("Helvetica", 12), width= 15, bg = "#3357ad", fg= "White",command=lambda:controller.show_frame("StudentList"))
        Requests = Button(self, text= "Requests", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",command=lambda: Main.Requests(self))
        Log_out = Button(self, text= "Log out", font= ("Helvetica", 12), width = 8, bg = "#f02f28", fg= "White",command=lambda: Main.quit(self))

        Students.place(x=120 , y=80 )
        Requests.place(x=120 , y=130 )
        Log_out.place(x= 5, y= 185)


class StudentList(Frame):

    def __init__(self,parent,controller):
        forms = open("forms.csv")
        Frame.__init__(self, parent)
        self.controller = controller
        # Creating a Listbox and
        # attaching it to self self
        listbox = Listbox(self, width=50, font= ("Helvetica", 12))
        # Adding Listbox to the left
        # side of self self
        listbox.place(x= 5, y= 0)
        # Creating a Scrollbar and
        # attaching it to self self
        scrollbar = Scrollbar(self)
        # Adding Scrollbar to the right
        # side of self self
        scrollbar.pack(side = RIGHT, fill = Y)
        Back = Button(self, text= "Back", font= ("Helvetica", 12), width = 15, bg = "#3357ad", fg= "White",
        command=lambda: controller.show_frame("TeacherMainMenu"))
        Back.pack(side = BOTTOM)

        # Insert elements into the listbox
        for form in forms.readlines():
            id = str(form.split(',')[0])
            if id not in listbox.get(0,END):
                listbox.insert(END, id)
        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        listbox.config(yscrollcommand = scrollbar.set)
        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command = listbox.yview)


def run():
    app = Main()
    app.resizable(0,0)
    app.geometry("400x225")
    app.iconbitmap("Images/Logo.ico")
    app.title("Swiftform - Teacher Menu")
    app.mainloop()
