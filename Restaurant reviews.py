import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import tkinter
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
root = tkinter.Tk()
root.title("Restaurant Reviews")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
vardosa = tkinter.StringVar()
vardom = tkinter.StringVar()
varherra = tkinter.StringVar()
varice = tkinter.StringVar()

import re

#for reading dataset & delimiter = \t coz it's a tab seperated values

dataset = pd.read_csv('review.tsv' , delimiter = '\t') 

########################STEPS FOR CLEANING ONE REVIEW#####################

#for first review from dataset

first = dataset['Review'][0] 

#1. Remove all the punctuations, numbers, symbols, emojis and unwanted characters.

text = re.sub('[^a-zA-Z]', ' ', first)

#2. Get all the data in lower case.

text = text.lower()

#for implementing 3rd step we need to convert text (string) into list

text = text.split()

#3. Remove unwanted words like preprositions, conjunctions , determiners, fillers, pronouns etc. 
#we import library called stopwords

from nltk.corpus import stopwords

t1 = [word for word in text if not word in set(stopwords.words('english'))]

#4. Perform stemming or lemmatization.

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

t2 = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]

clean_text = ' '.join(t2) 

###################NOW FOR COMPLETE DATASET######################

clean_reviews = []
for i in range(1000):
    text = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    text = text.lower()
    text = text.split()
    # t1 = [word for word in text if not word in set(stopwords.words('english'))]
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    clean_reviews.append(text)

#5. Represent the data using an nlp model.
# model here we use is BAG OF WORDS {BOW}

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 500)

#to convert data into sparse matrix

x = cv.fit_transform(clean_reviews)

#to convert data into array form which is visible to everyone

x = x.toarray()

#y for testing 

y = dataset['Liked'].values

#FOR SPLITTING THE DATASET INTO TRAINING & TESTING DATASET

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y)

#NOW FOR CLASSIFICATION WE USE LOGISTIC REGRESSION ALGORITHM

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()

#training the model

log_reg.fit(x_train, y_train)

#checkin accuracy of the training dataset

acc = log_reg.score(x_train,y_train)

#for checking what max features names are

feature_name = cv.get_feature_names()

#testing the model

log_reg.fit(x_test, y_test)

#for predictions 

y_pred = log_reg.predict(x_test)

#for checking the accuracy of model
 
acc_model = log_reg.score(x_test,y_pred)

#first five reviews

print(y_test[:10])

#first five predictions

print(y_pred[:10])

def btn_dosa_click():
    lbl1 = tkinter.Label(frame3,text="WRITE YOUR REVIEW HERE:",bg="dark green",font=("Arial bold",16))
    lbl1.grid(row=4,column=0)
    ent_dosa = tkinter.Entry(frame3,textvariable=vardosa,bg="dark green", font=("Georgia",20),bd=10)
    ent_dosa.grid(row=5,column=0)
    #btn_dosa = tkinter.Button(frame3,text="Analyse",relief="groove",bg="dark green", font=("Georgia",20),bd=10,command=btn_analyse())
    #btn_dosa.grid(row=6,column=0)
    
def btn_dom_click():
    lbl1 = tkinter.Label(frame3,text="WRITE YOUR REVIEW HERE:",bg="dark green",font=("Arial bold",16))
    lbl1.grid(row=4,column=1)
    ent_dosa = tkinter.Entry(frame3,textvariable=vardom,bg="dark green", font=("Georgia",20),bd=10)
    ent_dosa.grid(row=5,column=1)
    
    
def btn_herra_click():
    lbl1 = tkinter.Label(frame3,text="WRITE YOUR REVIEW HERE:",bg="dark green",font=("Arial bold",16))
    lbl1.grid(row=4,column=2)
    ent_dosa = tkinter.Entry(frame3,textvariable=varherra,bg="dark green", font=("Georgia",20),bd=10)
    ent_dosa.grid(row=5,column=2)
    
    
def btn_ice_click():
    lbl1 = tkinter.Label(frame3,text="WRITE YOUR REVIEW HERE:",bg="dark green",font=("Arial bold",16))
    lbl1.grid(row=4,column=3)
    ent_dosa = tkinter.Entry(frame3,textvariable=varice,bg="dark green", font=("Georgia",20),bd=10)
    ent_dosa.grid(row=5,column=3)
      
def btn_analyse():
    dosa = vardosa.get()
    dominos = vardom.get()
    herra = varherra.get()
    ice = varice.get()
    #taking review from user
        
    review = dosa

    #applying same steps(1-5) on the inputted review

    new_review = []
    text = re.sub('[^a-zA-Z]', ' ', review)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    new_review.append(text)
    x_new = cv.transform(new_review)
    x_new = x_new.toarray()
    
    #getting the prediction from model

    new_pred = log_reg.predict(x_new)

    #analysing the prediction
    new_pred
    if(new_pred == [1]):
        messagebox.showinfo("DOSA PLAZA","Positive Review")
    else:
        messagebox.showinfo("DOSA PLAZA","Negative Review") 
        
    
    

#=============================================================================================

frame1 = tkinter.Frame(root,bg="dark green")
frame1.pack(fill='y',side="top")
frame2 = tkinter.Frame(root,bg="white")
frame2.pack(pady=10,padx=10)
frame3 = tkinter.Frame(root,bg="white")
frame3.pack(pady=20,padx=20)
frame4 = tkinter.Frame(root,bg="white")
frame4.pack(padx=10,fill='y')
#===========================================Main title and image========================================
lbl1 = tkinter.Label(frame1,text="Restaurant Reviews",bg="dark green",font=("Arial bold",36))
lbl1.grid(row=0,column=1)


img_load = Image.open("restaurant_logo.png")
img_load = img_load. resize((350, 250), Image. ANTIALIAS)
image_res = ImageTk.PhotoImage(img_load)
lbl2 = tkinter.Label(frame1,image=image_res)
lbl2.grid(row=0,column=0)
#==========================================================================================
lbl1 = tkinter.Label(frame2,text="We will analyse that your review is positive or negative",bg="dark green",font=("Arial bold",16))
lbl1.grid(row=1,column=0)

#=========================================================================================
img_load = Image.open("Dosa plaza.png")
img_load = img_load. resize((350, 250), Image. ANTIALIAS)
image_dosa = ImageTk.PhotoImage(img_load)
lbl3 = tkinter.Label(frame3,image=image_dosa)
lbl3.grid(row=2,column=0,padx=2)
btn_dosa = tkinter.Button(frame3,text = "DOSA PLAZA",relief="groove",bg="dark green", font=("Georgia",14),fg="white",command=btn_dosa_click)
btn_dosa.grid(row=3,column=0,pady="2")


img_load = Image.open("Dominos.png")
img_load = img_load. resize((350, 250), Image. ANTIALIAS)
image_dom = ImageTk.PhotoImage(img_load)
lbl3 = tkinter.Label(frame3,image=image_dom)
lbl3.grid(row=2,column=1,padx="2")
btn_dom = tkinter.Button(frame3,text = "DOMINOS",relief="groove",bg="dark green", font=("Georgia",14),fg="white",command=btn_dom_click)
btn_dom.grid(row=3,column=1,pady="2")


img_load = Image.open("Herra Invitation.png")
img_load = img_load. resize((350, 250), Image. ANTIALIAS)
image_herra = ImageTk.PhotoImage(img_load)
lbl3 = tkinter.Label(frame3,image=image_herra)
lbl3.grid(row=2,column=2,padx="2")
btn_herra = tkinter.Button(frame3,text = "HERRA INVITATION",relief="groove",bg="dark green", font=("Georgia",14),fg="white",command=btn_herra_click)
btn_herra.grid(row=3,column=2,pady="2")


img_load = Image.open("Ice parlour.png")
img_load = img_load. resize((350, 250), Image. ANTIALIAS)
image_ice = ImageTk.PhotoImage(img_load)
lbl3 = tkinter.Label(frame3,image=image_ice)
lbl3.grid(row=2,column=3,padx="2")
btn_ice = tkinter.Button(frame3,text = "ICE PARLOUR",relief="groove",bg="dark green", font=("Georgia",14),fg="white",command=btn_ice_click)
btn_ice.grid(row=3,column=3,pady="2")


btn_ice = tkinter.Button(frame4,text = "Analyse",relief="groove",bg="dark green", font=("Georgia",24),fg="white",command = btn_analyse)
btn_ice.grid(row=6,column=2,pady="2")



root.mainloop()
