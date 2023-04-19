from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# function which will use Translator from googletrans to tanslate
def change(text="type", src="English", dest='Hindi'):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator() #making object of Translator class
    trans1 = trans.translate(text,src=src1,dest=dest1)# varible which will return, using the translate function of Translate class
    return trans1

# function to get data for translation
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk() # creating a object of TK class
root.title('Google Translator')  # set title of window
root.geometry('500x700')  # set the default opening window size 
root.config(bg='red') #set background color red

lab_txt = Label(root, text = 'Translator', font=("Times New Roman", 40, 'bold')) # creating a header label
lab_txt.place(x=100,y=30,height=50,width=300) # placing this lable on the top

frame = Frame(root,).pack(side=BOTTOM) #creating frame, then put out data inside frame, we place frame using pack

lab_txt = Label(root, text = 'Source Text', font=("Times New Roman", 17, 'bold'), fg='black', bg = 'red') # label for source text
lab_txt.place(x=100,y=105,height=20,width=300) # placing this lable on the text area

sor_txt = Text(frame, font=("vardana", 20, 'bold'), wrap=WORD )  # making a text field where user will put his text which he wants to translate
sor_txt.place(x=10,y=130,height=150,width=480)

# combo box to select source language
list_text = list(LANGUAGES.values())    #languages list from googletrans
comb_sor = ttk.Combobox(frame, value=list_text)  # source language combo box
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")  # set default lang. 

button_change = Button(frame, text="Translate", relief=RAISED, command=data) # translate button, relief is used to view button as 3D when it's pressed and released.
button_change.place(x=170,y=300,height=40,width=150)

# combo box for destination lang
comb_dest = ttk.Combobox(frame, value=list_text)  # destination language combo box
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("Hindi")  # set default lang.


# Label and text area for destination
lab_txt = Label(root, text = 'Destination Text', font=("Times New Roman", 17, 'bold'), fg='black', bg = 'red') # label for source text
lab_txt.place(x=100,y=375,height=20,width=300) # placing this lable on the text area

dest_txt = Text(frame, font=("vardana", 20, 'bold'), wrap=WORD )  # making a text field where user will put his text which he wants to translate
dest_txt.place(x=10,y=400,height=150,width=480)



root.mainloop() # this should be last line , required to show a tkinter window