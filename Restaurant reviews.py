# Importing the libraries
from tkinter import *
from tkinter import messagebox
import os
import webbrowser
import PIL
from PIL import Image,ImageTk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#re --> regular expression library
import re
#nltk--> natural language toolkit
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
#stopwords--> the words which we dont require in our data set
from nltk.corpus import stopwords

dataset = pd.read_csv('review.tsv',delimiter='\t')
clean_review = []
for i in range(1000):
    txt = re.sub('[^a-z A-Z]',' ',dataset['Review'][i]) #all punctuations will remove
    #print(txt)
    txt = txt.lower() #convert into lower case
    txt = txt.split() #convert txt into list
    txt = [ps.stem(word) for word in txt if not word in set(stopwords.words('english'))]
    # stopwords --> remove preposition,conjunction,etc
    # ps.stem(word) --> for performing stemming
    txt = ' '.join(txt) #convert into str
    clean_review.append(txt)
#select an algo --> BOW(bag of words)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=500)
X = cv.fit_transform(clean_review) # X is a Sparse matrix
X = X.toarray() # convert sparse into array
y = dataset['Liked'].values

#def executeReview():



#Now select any algorithm for predictions
#Logistic Regression
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X,y)
print(log_reg.score(X,y))
#print(y[:5])
y_pred = log_reg.predict(X)


class MainForm(Frame):
    main_Root = None

    def destroyPackWidget(self, parent):
        for e in parent.pack_slaves():
            e.destroy()
    def __init__(self,master=None):
        MainForm.main_Root = master
        super().__init__(master=master)
        root.title("Restaurant Reviews")
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.vardosa = StringVar()
        self.vardom = StringVar()
        self.varherra = StringVar()
        self.varice = StringVar()
        self.frame1 = Frame(root, bg="dark green")
        self.frame1.pack(fill='y', side="top")
        self.frame2 = Frame(root, bg="white")
        self.frame2.pack(pady=10, padx=10)
        self.frame3 = Frame(root, bg="white")
        self.frame3.pack(pady=20, padx=20)
        self.frame4 = Frame(root, bg="white")
        self.frame4.pack(padx=10, fill='y')
        self.createWidget()
    def createWidget(self):
        # ===========================================Main title and image========================================
        self.lbl1 = Label(self.frame1, text="Restaurant Reviews", bg="dark green", font=("Arial bold", 36))
        self.lbl1.grid(row=0, column=1)

        self.img_load = Image.open("restaurant_logo.png")
        self.img_load = self.img_load.resize((350, 250), Image.ANTIALIAS)
        self.image_res = ImageTk.PhotoImage(self.img_load)
        self.lbl2 = Label(self.frame1, image=self.image_res)
        self.lbl2.grid(row=0, column=0)
        # ==========================================================================================
        self.lbl1 = Label(self.frame2, text="We will analyse that your review is positive or negative", bg="dark green",
                             font=("Arial bold", 16))
        self.lbl1.grid(row=1, column=0)

        # =========================================================================================
        self.img_load = Image.open("Dosa plaza.png")
        self.img_load = self.img_load.resize((350, 250), Image.ANTIALIAS)
        self.image_dosa = ImageTk.PhotoImage(self.img_load)
        self.lbl3 = Label(self.frame3, image=self.image_dosa)
        self.lbl3.grid(row=2, column=0, padx=2)
        self.btn_dosa = Button(self.frame3, text="DOSA PLAZA", relief="groove", bg="dark green", font=("Georgia", 14),
                                  fg="white", command=self.btn_dosa_click)
        self.btn_dosa.grid(row=3, column=0, pady="2")

        self.img_load = Image.open("Dominos.png")
        self.img_load = self.img_load.resize((350, 250), Image.ANTIALIAS)
        self.image_dom = ImageTk.PhotoImage(self.img_load)
        self.lbl3 = Label(self.frame3, image=self.image_dom)
        self.lbl3.grid(row=2, column=1, padx="2")
        self.btn_dom = Button(self.frame3, text="DOMINOS", relief="groove", bg="dark green", font=("Georgia", 14),
                                 fg="white", command=self.btn_dom_click)
        self.btn_dom.grid(row=3, column=1, pady="2")

        self.img_load = Image.open("Herra Invitation.png")
        self.img_load = self.img_load.resize((350, 250), Image.ANTIALIAS)
        self.image_herra = ImageTk.PhotoImage(self.img_load)
        self.lbl3 = Label(self.frame3, image=self.image_herra)
        self.lbl3.grid(row=2, column=2, padx="2")
        self.btn_herra = Button(self.frame3, text="HERRA INVITATION", relief="groove", bg="dark green",
                                   font=("Georgia", 14), fg="white", command=self.btn_herra_click)
        self.btn_herra.grid(row=3, column=2, pady="2")

        self.img_load = Image.open("Ice parlour.png")
        self.img_load = self.img_load.resize((350, 250), Image.ANTIALIAS)
        self.image_ice = ImageTk.PhotoImage(self.img_load)
        self.lbl3 = Label(self.frame3, image=self.image_ice)
        self.lbl3.grid(row=2, column=3, padx="2")
        self.btn_ice = Button(self.frame3, text="ICE PARLOUR", relief="groove", bg="dark green", font=("Georgia", 14),
                                 fg="white", command=self.btn_ice_click)
        self.btn_ice.grid(row=3, column=3, pady="2")

        self.btn_ice = Button(self.frame4, text="Analyse", relief="groove", bg="dark green", font=("Georgia", 24),
                                 fg="white", command=self.btn_analyse)
        self.btn_ice.grid(row=6, column=2, pady="2")

    def btn_dosa_click(self):
        self.lbl1 = Label(self.frame3, text="WRITE YOUR REVIEW HERE:", bg="dark green", font=("Arial bold", 16))
        self.lbl1.grid(row=4, column=0)
        self.ent_dosa = Entry(self.frame3, textvariable=self.vardosa, bg="dark green", font=("Georgia", 20), bd=10)
        self.ent_dosa.grid(row=5, column=0)

    def btn_dom_click(self):
        self.lbl1 = Label(self.frame3, text="WRITE YOUR REVIEW HERE:", bg="dark green", font=("Arial bold", 16))
        self.lbl1.grid(row=4, column=1)
        self.ent_dom = Entry(self.frame3, textvariable=self.vardom, bg="dark green", font=("Georgia", 20), bd=10)
        self.ent_dom.grid(row=5, column=1)

    def btn_herra_click(self):
        self.lbl1 = Label(self.frame3, text="WRITE YOUR REVIEW HERE:", bg="dark green", font=("Arial bold", 16))
        self.lbl1.grid(row=4, column=2)
        self.ent_herra = Entry(self.frame3, textvariable=self.varherra, bg="dark green", font=("Georgia", 20), bd=10)
        self.ent_herra.grid(row=5, column=2)

    def btn_ice_click(self):
        self.lbl1 = Label(self.frame3, text="WRITE YOUR REVIEW HERE:", bg="dark green", font=("Arial bold", 16))
        self.lbl1.grid(row=4, column=3)
        self.ent_ice = Entry(self.frame3, textvariable=self.varice, bg="dark green", font=("Georgia", 20), bd=10)
        self.ent_ice.grid(row=5, column=3)

    def btn_analyse(self):
        self.destroyPackWidget(MainForm.main_Root)
        analyse = Analyse(MainForm.main_Root)
        analyse.pack()
class Analyse(Frame):
    main_Root = None
    def destroyPackWidget(self,parent):
        for e in parent.pack_slaves():
            e.destroy()
    def __init__(self, master=None):
        Analyse.main_Root=master
        master.title("Analyse Result")
        super().__init__(master=master)
        master.title("Analyse Result")
        self.createWidget()
    def createWidget(self):
        self.lblMsg = Label(self, text="Check result of ", bg="dark green", fg="white", font=('Georgia', 34)) \
            .grid(row=0, column=0, pady=10)
        self.lblMsg = Label(self, text="your reviews ", bg="dark green", fg="white", font=('Georgia', 34)) \
            .grid(row=0, column=1, pady=10)
        self.lblMsg1 = Label(self, text="below", bg="dark green", fg="white", font=('Georgia', 34)) \
            .grid(row=0, column=2, pady=10)
        self.txt = Label(self,text="Dosa Plaza",bg="dark green",fg="white",font=('Georgia',30))\
            .grid(row=1,pady=10)
        self.txt = Label(self, text="Dominos", bg="dark green", fg="white", font=('Georgia', 30)) \
            .grid(row=2,pady=10)
        self.txt = Label(self, text="Herra Invitation", bg="dark green", fg="white", font=('Georgia', 30)) \
            .grid(row=3,pady=10)
        self.txt = Label(self, text="Ice Parlour", bg="dark green", fg="white", font=('Georgia', 30)) \
            .grid(row=4,pady=10)


root = Tk()
frmMainForm=MainForm(root)
frmMainForm.pack(fill = 'y')
root.mainloop()
