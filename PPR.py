#Procedure I
a = []
empty = []   
Support = []
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
    
#Procedure 2
ssinput1 = customtkinter.CTkTextbox(app, width = 696, height = 50, font = ("Bahnschrift",24))
ssinput1.pack(padx = 10, pady = 10)
ssinput1_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", hover_color= "#d3d3d3", text_color= "black", text = "Enter", 
                                                  command = ssfinal, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
ssinput1_button.pack(padx=10, pady=10)


#List I 
py_avail = ["Python If condition","Python Variables", "Python Functions", "Python Comments", "Python For Loops", "Python While Loops"]
java_avail = ["Java If condition","Java Variables", "Java Functions", "Java Comments", "Java For Loops", "Java While Loops"]
csharp_avail = ["C# If condition","C# Variables", "C# Functions", "C# Comments", "C# For Loops", "C# While Loops"]

#List II
def listing_process():
    for i in range(len(py_avail)):
        print (py_avail[i])
        print (java_avail[i])
        print (csharp_avail[i])

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
        back_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", 
                                              text_color= "black", text = "Go Back", command = go_back, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        back_button.pack(padx=10, pady=10)
        Exit_button = customtkinter.CTkButton(app, corner_radius= 66, fg_color= "white", compound= "bottom",  hover_color= "#d3d3d3", 
                                              text_color= "black", text = "Exit", command = destroy, height = 70, width = 320, font = ("Bahnschrift",22,"bold"))
        Exit_button.pack(padx=10, pady=10)