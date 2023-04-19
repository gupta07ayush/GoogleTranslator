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
    return trans1.text

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
root.config(bg='#000e14') #set background color red

lab_txt = Label(root, text = 'AGTranslator', font=("Times New Roman", 30, 'bold'), bg='#00141f', fg='#00fff9',  borderwidth=3, relief="ridge") # creating a header label
lab_txt.place(x=10,y=10,height=100,width=480) # placing this lable on the top

frame = Frame(root,).pack(side=BOTTOM) #creating frame, then put out data inside frame, we place frame using pack

lab_txt = Label(root, text = 'Source Text', font=("sans serif", 12, "bold"), fg='#e5e5e5', bg = '#001824', anchor='w',) # label for source text
lab_txt.place(x=10,y=127,height=25,width=200) # placing this lable on the text area

sor_txt = Text(frame, font=("vardana", 18, 'bold'), wrap=WORD, bg='#001824', fg='#74c69d',  borderwidth=8, relief="flat")  # making a text field where user will put his text which he wants to translate
sor_txt.place(x=10,y=160,height=120,width=480)
sor_txt.focus_set()

# combo box to select source language
list_text = list(LANGUAGES.values())    #languages list from googletrans
comb_sor = ttk.Combobox(frame, value=list_text, font=('Arial', 12, 'bold'))  # source language combo box
comb_sor.place(x=10,y=340,height=40,width=150)
comb_sor.set("English")  # set default lang. 

button_change = Button(frame, text="Translate", relief=RIDGE, font=('Times new roman', 20, 'bold'), command=data,  bg='#22223b', fg='#dee2e6', borderwidth=2, activebackground='#001e45') # translate button, relief is used to view button as 3D when it's pressed and released.
button_change.place(x=170,y=340,height=40,width=150)

# combo box for destination lang
comb_dest = ttk.Combobox(frame, value=list_text, font=('Arial', 12, 'bold') )  # destination language combo box
comb_dest.place(x=330,y=340,height=40,width=150)
comb_dest.set("Hindi")  # set default lang.


# Label and text area for destination
lab_txt = Label(root, text = 'Destination Text', font=("sans serif", 12, 'bold'), bg = '#00141f', fg='#e5e5e5', anchor="e") # label for source text
lab_txt.place(x=260,y=432,height=25,width=230) # placing this lable on the text area

dest_txt = Text(frame, font=("vardana", 18, 'bold'), wrap=WORD, bg='#00111a',fg='#74c69d', borderwidth=8, relief="flat" )  # making a text field where user will put his text which he wants to translate
dest_txt.place(x=10,y=465,height=130,width=480)

footer_txt = Label(root, text = 'Developed by:    @gupta07ayush', font=("sans serif", 9), bg='#000000', fg='#a8dadc') # creating a header label
footer_txt.place(x=0,y=660,height=30,width=500) # placing this lable on the top



root.mainloop() # this should be last line , required to show a tkinter window