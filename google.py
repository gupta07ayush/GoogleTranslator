from tkinter import *
from tkinter import ttk

root = Tk() # creating a object of TK class
root.title('Google Translator')  # set title of window
root.geometry('500x700')  # set the default opening window size 
root.config(bg='red') #set background color red

lab_txt = Label(root, text = 'Translator', font=("Times New Roman", 40, 'bold')) # creating a header label
lab_txt.place(x=100,y=40,height=50,width=300) # placing this lable on the top

frame = Frame(root,).pack(side=BOTTOM) #creating frame, then put out data inside frame, we place frame using pack

lab_txt = Label(root, text = 'Source Text', font=("Times New Roman", 17, 'bold'), fg='black', bg = 'red') # label for source text
lab_txt.place(x=100,y=105,height=20,width=300) # placing this lable on the text area

sor_txt = Text(frame, font=("vardana", 20, 'bold'), wrap=WORD )  # making a text field where user will put his text which he wants to translate
sor_txt.place(x=10,y=130,height=150,width=480)








root.mainloop() # this should be last line , required to show a tkinter window