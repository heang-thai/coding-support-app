# AP CSP Create Task
# Author: Dechehsey, Heang, Sam

#Imports required modules
import tkinter #Import the standard tkinter library 
import customtkinter #Import a custom tkinter library
import random
from tkinter import * #Imports all the classes from tkinter module 
from customtkinter import * #Imports all the classes from customtkinter module 
from tkinter.ttk import * #Imports themed widgets from tkinter
from PIL import Image #Imports the Image module from the Pillow library
from pytube import * #Imports from the pytube module for data collection
import time #Importing time module

#Sets the GUI look
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#Creates root for GUI
app = customtkinter.CTk()

#These functions open classes listed below as toplevel windows
def List_toplevel():
    app.toplevel_window = Listsl(app)
    app.withdraw()

def Py_toplevel():
    app.toplevel_window = Pythonsl(app)
    app.withdraw()

def Java_toplevel():
    app.toplevel_window = Javasl(app)
    app.withdraw()

def Csharp_toplevel():
    app.toplevel_window = Csharpsl(app)
    app.withdraw()

def maincopy_toplevel():
    app.toplevel_window = maincopy(app)
    app.withdraw()

def Support_toplevel():
    app.toplevel_window = Supportsl(app)
    app.withdraw()

def Quiz_toplevel():
    app.toplevel_window = quizsl(app)
    app.withdraw()

#This section is the main page, the root app

#Sets the logo of the app    
app_logo = customtkinter.CTkImage(Image.open("csc.png"), size=(250, 250))
#Creates the title
image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
image.pack(pady = 20)
#Sets the app icon
app.iconbitmap("csc.ico")
#Sets the app to start automatically maximized
app._state_before_windows_set_titlebar_color = 'zoomed'
#Sets the title that the user sees at the top left of the screen(For windows)
app.title("Coding Support")
#Sets the welcome text
Welcome = customtkinter.CTkLabel(app, text = "Welcome to Coding Support!", font = ("Bahnschrift",25,"bold"))
Welcome.pack(padx=10, pady=20)
#Prompts and buttons for the program
Select = customtkinter.CTkLabel(app, text = "Please select a language you would like to learn", font = ("Bahnschrift",25,"bold"))
Select.pack(padx=10, pady=20)
Python_button = customtkinter.CTkButton(app, corner_radius= 66,hover_color= "#d3d3d3", fg_color= "white", text_color= "black", text = "Python", command = Py_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
Python_button.pack(padx=10, pady=10)
Java_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black",  text = "Javascript", command = Java_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
Java_button.pack(padx=10, pady=10)
Csharp_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "C#", command = Csharp_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
Csharp_button.pack(padx=10, pady=10)
List_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "List Available Info", command = List_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
List_button.pack(padx=10, pady=10)
Support_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Provide Feedback", command = Support_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
Support_button.pack(padx=10, pady=10)
Quiz_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Quiz", command = Quiz_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
Quiz_button.pack(padx=10, pady=10)
    
#The variables are the information that will be used for the program
python_info = ["if condition: \n  code \n", "variableName = value \n", "def functionName(parameters):\n  code \n", "\n # Single line \n \"\"\" Multi line comment \"\"\" \n", "for i in range(limit):\n  code \n", "while condition:\n  code \n"]
java_info = ["if (condition) {\n  code\n} \n", "var variableName = value \n", "function functionName(parameters) {\n  code\n} \n", "// comment \n /* Multi line comment */ \n", "for (var i = 0; i < limit; i++) {\n  code\n} \n", "while (condition) {\n  code\n} \n" ]
csharp_info = ["if (condition)\n{\n  code\n} \n", "type variableName = value \n", "public static void functionName(parameters)\n{\n  code\n} \n", "// comment \n /* Multi line comment */ \n", "for (int i = 0; i < limit; i++)\n{\n  code\n} \n", "while (condition)\n{\n  code\n} \n"]
#These variables list the available info for usage
py_avail = ["Python If condition","Python Variables", "Python Functions", "Python Comments", "Python For Loops", "Python While Loops"]
java_avail = ["Java If condition","Java Variables", "Java Functions", "Java Comments", "Java For Loops", "Java While Loops"]
csharp_avail = ["C# If condition","C# Variables", "C# Functions", "C# Comments", "C# For Loops", "C# While Loops"]

#A function that lists out all the available info utilizing 3 lists for one of the functions
def listing_process():
    for i in range(len(py_avail)):
        print (py_avail[i])
        print (java_avail[i])
        print (csharp_avail[i])

#A copy of the root page for opening later when going back and forth between pages
class maincopy(customtkinter.CTkToplevel):
    #Applies for all classes, these functions allow the toplevels to work and execute properly
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def List_toplevel():
            app.toplevel_window = Listsl(app)
            app.withdraw()

        def Py_toplevel():
            app.toplevel_window = Pythonsl(app)
            app.withdraw()

        def Java_toplevel():
            app.toplevel_window = Javasl(app)
            app.withdraw()

        def Csharp_toplevel():
            app.toplevel_window = Csharpsl(app)
            app.withdraw()

        def Support_toplevel():
            app.toplevel_window = Supportsl(app)
            app.withdraw()

        def Quiz_toplevel():
            app.toplevel_window = quizsl(app)
            app.withdraw()

        #This is the maincopy gui config and page
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        app_logo = customtkinter.CTkImage(Image.open("csc.png"), size=(250, 250))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.title("Coding Support")
        Welcome = customtkinter.CTkLabel(app, text = "Welcome to Coding Support!", font = ("Bahnschrift",25,"bold"))
        Welcome.pack(padx=10, pady=20)
        Select = customtkinter.CTkLabel(app, text = "Please select a language you would like to learn", font = ("Bahnschrift",25,"bold"))
        Select.pack(padx=10, pady=20)
        Python_button = customtkinter.CTkButton(app, corner_radius= 66,hover_color= "#d3d3d3", fg_color= "white", text_color= "black", text = "Python", command = Py_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
        Python_button.pack(padx=10, pady=10)
        Java_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black",  text = "Javascript", command = Java_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
        Java_button.pack(padx=10, pady=10)
        Csharp_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "C#", command = Csharp_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
        Csharp_button.pack(padx=10, pady=10)
        List_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "List Available Info", command = List_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
        List_button.pack(padx=10, pady=10)
        Support_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Provide Feedback", command = Support_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
        Support_button.pack(padx=10, pady=10)
        Quiz_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Quiz", command = Quiz_toplevel, height = 60, width = 320, font = ("Bahnschrift",22,"bold"))
        Quiz_button.pack(padx=10, pady=10)

#Python page, contains the first page asking about what the user wants to find out then each number opens different pages with set information
class Pythonsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #The python page is distributed into 7 top levels including an error page
        class pythonsl2(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Python If")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Python If statements are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= python_info[0], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "For the condition the user able to utilize x ==,!=,>,< etc to other variables or values. \n For the code the user may place any certain statement or run functions.", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class pythonsl3(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Python Variables")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Python Variables are defined like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=python_info[1], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "In order to utilize Variables in python the user must: \n First, name the variable \n Then, give it any value(integer or other variables)", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class pythonsl4(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Python Functions")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Python functions are written like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=python_info[2], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "In order to use Python functions, the user must start by writing def then naming the function finishing with (): \n the parameters may contain variables for specific uses and functions. \n Under the function definition is where the user will write the code that will run when the function is called", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class pythonsl5(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Python Comments")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Python comments are written like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=python_info[3], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Python comments are simple, for single line comments the user can just type a # and write anything next to it within one line. \n for multiline comments the user is able to write a lot but just use 3 quotes at the start and the end of the comment", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class pythonsl6(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Python For Loops")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Python for loops are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=python_info[4], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Utilizing For loops in python, the user first must put in a variable (in this case i is used) \n Then, the user is able to set the range of the variable as certain limits such as amount of times etc. \n Under that loop is where the rest of the code resides.", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class pythonsl7(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Python While Loops")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Python while loops are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=python_info[5], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "For python while loops, the user may put in any condition such as true, x = value etc \n The code will then keep repeating until the condition stops", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class invalidinput(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                app.title("Coding Support | Error")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Invalid", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
#These are the functons that run when the user enters the prompts 
        def inval_toplevel():
            app.withdraw()
            app.toplevel_window = invalidinput(app)
        def destroy():
            app.destroy()
        def pyif():
            app.withdraw()
            app.toplevel_window = pythonsl2(app)
        def pyvar():
            app.withdraw()
            app.toplevel_window = pythonsl3(app)
        def pyfunc():
            app.withdraw()
            app.toplevel_window = pythonsl4(app)
        def pycom():
            app.withdraw()
            app.toplevel_window = pythonsl5(app)
        def pyfor():
            app.withdraw()
            app.toplevel_window = pythonsl6(app)
        def pywhile():
            app.withdraw()
            app.toplevel_window = pythonsl7(app)

        #In case of too many invalid inputs, the toplevel goes to invalid input, otherwise will open the toplevel windows needed
        def pyfinal():
            dec = 0
            while dec == 0:
                getpythoninput = pyinput1.get('1.0', END)
                if int(getpythoninput) == 1:
                    pyif()
                    dec = 1
                elif int(getpythoninput) == 2:
                    pyvar()
                    dec = 1
                elif int(getpythoninput) == 3:
                    pyfunc()
                    dec = 1
                elif int(getpythoninput) == 4:
                    pycom()
                    dec = 1
                elif int(getpythoninput) == 5:
                    pyfor()
                    dec = 1
                elif int(getpythoninput) == 6:
                    pywhile()
                    dec = 1
                elif int(getpythoninput) == 0:
                    destroy()
                    dec = 1
                else:
                    inval_toplevel()
                    dec = 1
        #This is the python main page gui config            
        app.title("Coding Support | Python")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Please enter a number to select:", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=5)
        prompt0 = customtkinter.CTkLabel(app, text = "0 to exit", font = ("Bahnschrift",22,"bold"))
        prompt0.pack(padx=10, pady=5)
        prompt1 = customtkinter.CTkLabel(app, text = "1 for If Syntax", font = ("Bahnschrift",22,"bold"))
        prompt1.pack(padx=10, pady=5)
        prompt2 = customtkinter.CTkLabel(app, text = "2 for Variable Syntax", font = ("Bahnschrift",22,"bold"))
        prompt2.pack(padx=10, pady=5)
        prompt3 = customtkinter.CTkLabel(app, text = "3 for Function Syntax", font = ("Bahnschrift",22,"bold"))
        prompt3.pack(padx=10, pady=5)
        prompt4 = customtkinter.CTkLabel(app, text = "4 for Comments", font = ("Bahnschrift",22,"bold"))
        prompt4.pack(padx=10, pady=5)
        prompt5 = customtkinter.CTkLabel(app, text = "5 for For Loop Syntax", font = ("Bahnschrift",22,"bold"))
        prompt5.pack(padx=10, pady=5)
        prompt6 = customtkinter.CTkLabel(app, text = "6 for While Loop Syntax", font = ("Bahnschrift",22,"bold"))
        prompt6.pack(padx=10, pady=5)
        pyinput1 = customtkinter.CTkTextbox(app, width = 696, height = 50, font = ("Bahnschrift",24))
        pyinput1.pack(padx = 10, pady = 10)
        pyinput1_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Enter", command = pyfinal, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        pyinput1_button.pack(padx=10, pady=10)

#Java page, contains the first page asking about what the user wants to find out then each number opens different pages with set information             
class Javasl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #The Java page is distributed into 7 top levels including an error page
        class javasl2(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Javascript If")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Javascript If statements are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= java_info[0], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "To use if statements in Javascript, the user must first enter a condition after typing if, these conditions can be num > 1 etc. \n Afterwards, just like in python the user may enter anything under the if statement, could be a print command or functions", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class javasl3(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Javascript Variables")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Javascript Variables are defined like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=java_info[1], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "For the variables in Javascript, the user must name the variable next to var, \n Then the user will need to give it any value(integer or other variables)", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class javasl4(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Javascript Functions")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Javascript functions are written like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=java_info[2], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Unlike Python, Javascript utilizes function instead of def to create a function, after using the command the user name name the function and set any parameter within the parenthesis \n Then the user is able to enter any code under the function that will run when called upon.", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class javasl5(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Javascript Comments")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Javascript comments are written like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=java_info[3], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Simple like Python, Javascript comments are written with // for single line comments and /* at the beginning and the end for multi-line comments", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class javasl6(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Javascript For Loops")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Javascript for loops are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=java_info[4], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Javascript loops are a bit tricky, the user must first set var = 0 then set the limits for how long the code will run, \n Then the user may enter the code under the for loop that needs running. (code will run in increments of 1 due to i++)", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class javasl7(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | Javascript While Loops")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Javascript while loops are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=java_info[5], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "While loops in Javascript are similar to Python, the user first writes down the condition then the code that runs during the active condition", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class invalidinput(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                app.title("Coding Support | Error")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Invalid", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        #These are functions that are needed for the Java top levels to open once the user clicks any button on the Java page
        def destroy():
            app.destroy()
        def Javaif():
            app.withdraw()
            app.toplevel_window = javasl2(app)
        def Javavar():
            app.withdraw()
            app.toplevel_window = javasl3(app)
        def Javafunc():
            app.withdraw()
            app.toplevel_window = javasl4(app)
        def Javacom():
            app.withdraw()
            app.toplevel_window = javasl5(app)
        def Javafor():
            app.withdraw()
            app.toplevel_window = javasl6(app)
        def Javawhile():
            app.withdraw()
            app.toplevel_window = javasl7(app)
        def inval_toplevel():
            app.withdraw()
            app.toplevel_window = invalidinput(app)
        #This function is used to open the error page then the user has too many invalid inputs
        def javafinal():
            dec = 0
            while dec == 0:
                getjavainput = javainput1.get('1.0', END)
                if int(getjavainput) == 1:
                    Javaif()
                    dec = 1
                elif int(getjavainput) == 2:
                    Javavar()
                    dec = 1
                elif int(getjavainput) == 3:
                    Javafunc()
                    dec = 1
                elif int(getjavainput) == 4:
                    Javacom()
                    dec = 1
                elif int(getjavainput) == 5:
                    Javafor()
                    dec = 1
                elif int(getjavainput) == 6:
                    Javawhile()
                    dec = 1
                elif int(getjavainput) == 0:
                    destroy()
                    dec = 1
                else:
                    inval_toplevel()
                    dec = 1

        #This is the Java main page gui config 
        app.title("Coding Support | Javascript")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Please enter a number to select:", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=5)
        prompt0 = customtkinter.CTkLabel(app, text = "0 to exit", font = ("Bahnschrift",22,"bold"))
        prompt0.pack(padx=10, pady=5)
        prompt1 = customtkinter.CTkLabel(app, text = "1 for If Syntax", font = ("Bahnschrift",22,"bold"))
        prompt1.pack(padx=10, pady=5)
        prompt2 = customtkinter.CTkLabel(app, text = "2 for Variable Syntax", font = ("Bahnschrift",22,"bold"))
        prompt2.pack(padx=10, pady=5)
        prompt3 = customtkinter.CTkLabel(app, text = "3 for Function Syntax", font = ("Bahnschrift",22,"bold"))
        prompt3.pack(padx=10, pady=5)
        prompt4 = customtkinter.CTkLabel(app, text = "4 for Comments", font = ("Bahnschrift",22,"bold"))
        prompt4.pack(padx=10, pady=5)
        prompt5 = customtkinter.CTkLabel(app, text = "5 for For Loop Syntax", font = ("Bahnschrift",22,"bold"))
        prompt5.pack(padx=10, pady=5)
        prompt6 = customtkinter.CTkLabel(app, text = "6 for While Loop Syntax", font = ("Bahnschrift",22,"bold"))
        prompt6.pack(padx=10, pady=5)
        javainput1 = customtkinter.CTkTextbox(app, width = 696, height = 50, font = ("Bahnschrift",24))
        javainput1.pack(padx = 10, pady = 10)
        javainput1_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Enter", command = javafinal, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        javainput1_button.pack(padx=10, pady=10)

    
#Csharp page, contains the first page asking about what the user wants to find out then each number opens different pages with set information
class Csharpsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #The Csharp page is distributed into 7 top levels including an error page
        class csharpsl2(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | C# If")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="C# If statements are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=csharp_info[0], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "To utilize the if statement the user must set specific conditions then enter the code that will run once the conditions are met", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class csharpsl3(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | C# Variables")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="C# Variables are defined like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=csharp_info[1], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "In order to utilize the variables of C# the user define the name after putting in type then giving the variable it's value", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class csharpsl4(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | C# Functions")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="C# functions are written like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=csharp_info[2], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "C# uses public static void to define it's functions, the user then enters the function name and it's parameters within the parenthesis. \n Afterwards the code will be written under the function that will be executed once called upon", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class csharpsl5(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | C# Comments")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="C# comments are written like shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=csharp_info[3], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Same as Javascript, C# comments are written using // for single-line and /* for multi-line", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class csharpsl6(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | C# For Loops")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="C# for loops are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=csharp_info[4], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "In order to utilize the for loops of C# the user must set int i = 0 which is equivalent to Javascript's var i = 0 \n Then the user sets the limits of the for loop(how many times it runs) and enters the code that runs under the for loop(repeats in increments of 1 like javascript due to i++)", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class csharpsl7(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                def destroy():
                    app.destroy()
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                super().__init__(*args, **kwargs)
                app.title("Coding Support | C# While Loops")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="C# while loops are written as shown below:", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text=csharp_info[5], font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text= "Similarly like other languages, C# While loops are written with the requirement of the user entering the condition then the code that runs when the condition is still active.", font = ("Bahnschrift",20))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        class invalidinput(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                app.title("Coding Support | Error")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Invalid", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)
        #These functions are for opening the toplevel windows on the csharp page when a button command is triggered
        def destroy():
            app.destroy()
        def Csharpif():
            app.withdraw()
            app.toplevel_window = csharpsl2(app)
        def Csharpvar():
            app.withdraw()
            app.toplevel_window = csharpsl3(app)
        def Csharpfunc():
            app.withdraw()
            app.toplevel_window = csharpsl4(app)
        def Csharpcom():
            app.withdraw()
            app.toplevel_window = csharpsl5(app)
        def Csharpfor():
            app.withdraw()
            app.toplevel_window = csharpsl6(app)
        def Csharpwhile():
            app.withdraw()
            app.toplevel_window = csharpsl7(app)
        def inval_toplevel():
            app.withdraw()
            app.toplevel_window = invalidinput(app)
        #This function is used to open the error page then the user has too many invalid inputs
        def csharpfinal():
            dec = 0
            while dec == 0:
                getcsinput = csinput1.get('1.0', END)
                if int(getcsinput) == 1:
                    Csharpif()
                    dec = 1
                elif int(getcsinput) == 2:
                    Csharpvar()
                    dec = 1
                elif int(getcsinput) == 3:
                    Csharpfunc()
                    dec = 1
                elif int(getcsinput) == 4:
                    Csharpcom()
                    dec = 1
                elif int(getcsinput) == 5:
                    Csharpfor()
                    dec = 1
                elif int(getcsinput) == 6:
                    Csharpwhile()
                    dec = 1
                elif int(getcsinput) == 0:
                    destroy()
                    dec = 1
                else:
                    inval_toplevel()
                    dec = 1

        #This is the Csharp main page gui config
        app.title("Coding Support | C#")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Please enter a number to select:", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=5)
        prompt0 = customtkinter.CTkLabel(app, text = "0 to exit", font = ("Bahnschrift",22,"bold"))
        prompt0.pack(padx=10, pady=5)
        prompt1 = customtkinter.CTkLabel(app, text = "1 for If Syntax", font = ("Bahnschrift",22,"bold"))
        prompt1.pack(padx=10, pady=5)
        prompt2 = customtkinter.CTkLabel(app, text = "2 for Variable Syntax", font = ("Bahnschrift",22,"bold"))
        prompt2.pack(padx=10, pady=5)
        prompt3 = customtkinter.CTkLabel(app, text = "3 for Function Syntax", font = ("Bahnschrift",22,"bold"))
        prompt3.pack(padx=10, pady=5)
        prompt4 = customtkinter.CTkLabel(app, text = "4 for Comments", font = ("Bahnschrift",22,"bold"))
        prompt4.pack(padx=10, pady=5)
        prompt5 = customtkinter.CTkLabel(app, text = "5 for For Loop Syntax", font = ("Bahnschrift",22,"bold"))
        prompt5.pack(padx=10, pady=5)
        prompt6 = customtkinter.CTkLabel(app, text = "6 for While Loop Syntax", font = ("Bahnschrift",22,"bold"))
        prompt6.pack(padx=10, pady=5)
        csinput1 = customtkinter.CTkTextbox(app, width = 696, height = 50, font = ("Bahnschrift",24))
        csinput1.pack(padx = 10, pady = 10)
        csinput1_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Enter", command = csharpfinal, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        csinput1_button.pack(padx=10, pady=10)
        
#Lists page, opens a page that runs the command listing_process which lists all info available for the user in the terminal
class Listsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def destroy():
            app.destroy()
        app.title("Coding Support | List Avail")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Please redirect to the terminal.", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=5)
        print("Information Available:")
        listing_process()
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)
#Variables used for the feedback receiving procedure
a = []
empty = []   
Support = []
#Support page, Recieves feedback from the text box and prints it in the terminal on the command of the enter button.
class Supportsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def ssenter():
            app.withdraw()
            app.toplevel_window = Thanks(app)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def ssfinal():
            ssenter()
            def receiving(empty,Recieved):
                Recieved = (ssinput1.get('1.0', END))
                empty.append(Recieved)
                return empty
            print("Received Feedback")
            empty = receiving(a,Support)
            for i in range(len(empty)):
                    print (empty[i])
        #This is the support sub-page, it's just a thank you page
        class Thanks(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def go_back():
                    app.withdraw()
                    maincopy_toplevel()
                def destroy():
                    app.destroy()
                app.title("Coding Support | Thank You!")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                app.label = customtkinter.CTkLabel(app, text="Thank you for your feedback!", font = ("Bahnschrift",30))
                app.label.pack(padx=20, pady=20)
                app.label = customtkinter.CTkLabel(app, text="(Check in terminal for recieved feedback)", font = ("Bahnschrift",10))
                app.label.pack(padx=20, pady=20)
                back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", 
                                                      command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                back_button.pack(padx=10, pady=10)
                Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", 
                                                      command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                Exit_button.pack(padx=10, pady=10)

        def destroy():
            app.destroy()
        #This is the GUI config for the support/feedback main page
        app.title("Coding Support | Feeback")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Please enter any feedback:", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=5)
        ssinput1 = customtkinter.CTkTextbox(app, width = 696, height = 50, font = ("Bahnschrift",24))
        ssinput1.pack(padx = 10, pady = 10)
        ssinput1_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Enter", 
                                                  command = ssfinal, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        ssinput1_button.pack(padx=10, pady=10)
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", 
                                              text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", 
                                              text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)

#These variables are all the possibilities of the user's scoring
final_score = []
Full = ["correct", "correct", "correct", "correct"]
Aw = ["wrong", "wrong", "wrong", "wrong"]
Op2 = ["correct", "wrong", "wrong", "wrong"]
Op3 = ["correct", "correct", "wrong", "wrong"]
Op4 = ["correct", "correct", "correct", "wrong"]
Op5 = ["correct", "correct", "wrong", "correct"]
Op6 = ["wrong", "correct", "wrong", "correct"]
Op7 = ["correct", "wrong", "wrong", "correct"]
Op8 = ["wrong", "wrong", "wrong", "correct"]
Op9 = ["correct", "wrong", "correct", "correct"]
Op10 = ["correct", "wrong", "correct", "wrong"]
Op11 = ["wrong", "correct", "wrong", "wrong"]
Op12 = ["wrong", "wrong", "correct", "wrong"]
Op13 = ["wrong", "wrong", "correct", "correct"]
Op14 = ["wrong", "correct", "correct", "correct"]

#The quiz page, contains four questions and a scoring system
class quizsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        #The quiz is divided into four sub-classes
        super().__init__(*args, **kwargs)
        #If the user answers the right answer, the command of the right answer will run and the score will be counted
        def q1ransw():
            score = "correct"
            final_score.append(score)
            app.withdraw()
            app.toplevel_window = quizl2(app)
        #If the user answers the wrong answer, the command of the wrong answer will run and the score will be counted
        def q1wansw():
            score = "wrong"
            final_score.append(score)
            app.withdraw()
            app.toplevel_window = quizl2(app)
        class quizl2(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def q2ransw():
                    score = "correct"
                    final_score.append(score)
                    app.withdraw()
                    app.toplevel_window = quizl3(app)
                def q2wansw():
                    score = "wrong"
                    final_score.append(score)
                    app.withdraw()
                    app.toplevel_window = quizl3(app)
                app.title("Coding Support | Quiz")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                prompt = customtkinter.CTkLabel(app, text = "Python|Java|C# Quiz", font = ("Bahnschrift",25,"bold"))
                prompt.pack(padx=10, pady=40)
                prompt0 = customtkinter.CTkLabel(app, text = "2. Which of the following is the correct syntax for function in Java?", font = ("Bahnschrift",22,"bold"))
                prompt0.pack(padx=10, pady=15)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "def functionName(parameters): code", command = q2wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "function functionName(parameters) { code }", command = q2ransw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "public static void functionName(parameters){ code }", command = q2wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
        class quizl3(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def q3ransw():
                    score = "correct"
                    final_score.append(score)
                    app.withdraw()
                    app.toplevel_window = quizl4(app)
                def q3wansw():
                    score = "wrong"
                    final_score.append(score)
                    app.withdraw()
                    app.toplevel_window = quizl4(app)
                app.title("Coding Support | Quiz")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                prompt = customtkinter.CTkLabel(app, text = "Python|Java|C# Quiz", font = ("Bahnschrift",25,"bold"))
                prompt.pack(padx=10, pady=40)
                prompt0 = customtkinter.CTkLabel(app, text = "3. How do you declare a variable in Python?", font = ("Bahnschrift",22,"bold"))
                prompt0.pack(padx=10, pady=15)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "variableName = value", command = q3ransw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "type variableName = value", command = q3wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "var variableName = value", command = q3wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
        class quizl4(customtkinter.CTkToplevel):
            def __init__(app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                def q4ransw():
                    score = "correct"
                    final_score.append(score)
                    #After appending the final score, the program scrolls through all the possibilities and determines which page to open
                    if final_score == Full:
                        app.withdraw()
                        app.toplevel_window = Fullsl(app)
                        final_score.clear()
                    elif final_score == Aw:
                        app.withdraw()
                        app.toplevel_window = zerosl(app)
                        final_score.clear()
                    elif final_score == Op2:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op3:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op4:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                    elif final_score == Op5:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                    elif final_score == Op6:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op7:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op8:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op9:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                    elif final_score == Op10:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op11:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op12:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op13:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op14:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                def q4wansw():
                    score = "wrong"
                    final_score.append(score)
                    if final_score == Full:
                        app.withdraw()
                        app.toplevel_window = Fullsl(app)
                        final_score.clear()
                    elif final_score == Aw:
                        app.withdraw()
                        app.toplevel_window = zerosl(app)
                        final_score.clear()
                    elif final_score == Op2:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op3:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op4:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                    elif final_score == Op5:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                    elif final_score == Op6:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op7:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op8:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op9:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                    elif final_score == Op10:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op11:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op12:
                        app.withdraw()
                        app.toplevel_window = onesl(app)
                        final_score.clear()
                    elif final_score == Op13:
                        app.withdraw()
                        app.toplevel_window = halfsl(app)
                        final_score.clear()
                    elif final_score == Op14:
                        app.withdraw()
                        app.toplevel_window = threesl(app)
                        final_score.clear()
                
                app.title("Coding Support | Quiz")
                app._state_before_windows_set_titlebar_color = 'zoomed'
                app.after(250, lambda: app.iconbitmap('csc.ico'))
                image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
                image.pack(pady = 20)
                prompt = customtkinter.CTkLabel(app, text = "Python|Java|C# Quiz", font = ("Bahnschrift",25,"bold"))
                prompt.pack(padx=10, pady=40)
                prompt0 = customtkinter.CTkLabel(app, text = "4. What is the syntax for C# for loop?", font = ("Bahnschrift",22,"bold"))
                prompt0.pack(padx=10, pady=15)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "for i in range(limit): code", command = q4wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
                answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "for (var i = 0; i < limit; i++) { code }", command = q4ransw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
                answ_button.pack(padx=10, pady=10)
                
        #This is the configuration of the quiz main page GUI            
        app.title("Coding Support | Quiz")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Python|Java|C# Quiz", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=40)
        prompt0 = customtkinter.CTkLabel(app, text = "1. Which of these is the correct syntax for Python single-line comments?", font = ("Bahnschrift",22,"bold"))
        prompt0.pack(padx=10, pady=15)
        answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "#Comment", command = q1ransw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        answ_button.pack(padx=10, pady=10)
        answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "/*Comment*/", command = q1wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        answ_button.pack(padx=10, pady=10)
        answ_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "//Comment", command = q1wansw, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        answ_button.pack(padx=10, pady=10)

#This is the toplevel that opens when the user gets a full score
class Fullsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def destroy():
            app.destroy()
        app.title("Coding Support | Quiz Results")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Congratulations! You scored a Full score!", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=100)
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)

#This toplevel window opens when the user scores a zero
class zerosl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def destroy():
            app.destroy()
        app.title("Coding Support | Quiz Results")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Unfortunately, you scored a zero", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=100)
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)

#This toplevel window opens when the user scores half
class halfsl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def destroy():
            app.destroy()
        app.title("Coding Support | Quiz Results")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "You score 2/4!", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=100)
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)

#This toplevel window opens when the user scores a one
class onesl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def destroy():
            app.destroy()
        app.title("Coding Support | Quiz Results")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "You scored a 1/4, Try harder next time!", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=100)
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)

#This toplevel opens when the user scores a three
class threesl(customtkinter.CTkToplevel):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def go_back():
            app.withdraw()
            maincopy_toplevel()
        def destroy():
            app.destroy()
        app.title("Coding Support | Quiz Results")
        app._state_before_windows_set_titlebar_color = 'zoomed'
        app.after(250, lambda: app.iconbitmap('csc.ico'))
        image = CTkLabel(app,image = app_logo, text = "Coding Support",compound="top", font = ("Bahnschrift",40,))
        image.pack(pady = 20)
        prompt = customtkinter.CTkLabel(app, text = "Great Job! You scored 3/4!", font = ("Bahnschrift",25,"bold"))
        prompt.pack(padx=10, pady=100)
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)

#This is the mainloop that runs the program
app.mainloop()