from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
import smtplib, ssl
from datetime import datetime
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred=credentials.Certificate(r'C:\django\django_app\todo\todo_list\prosc-87c7d-firebase-adminsdk-ar1cv-7352968967.json')

firebase_admin.initialize_app(cred)


db=firestore.client()


config =  {
    'apiKey': "AIzaSyDJVrePVygDrMZjbL46gtk6Ixvbn160Og4",
    'authDomain': "prosc-87c7d.firebaseapp.com",
    'databaseURL': "https://prosc-87c7d.firebaseio.com",
    'projectId': "prosc-87c7d",
    'storageBucket': "prosc-87c7d.appspot.com",
    'messagingSenderId': "919355352719",
    'appId': "1:919355352719:web:f2dec346ebb42e395c72fa"
        }
firebase=pyrebase.initialize_app(config)

authe=firebase.auth()

# Create your views here.

def signin(request):
 	return render(request, "signin.html")

def postsign(request):
    email=request.POST.get("email")
    passw=request.POST.get("pass")
#     user = authe.sign_in_with_email_and_password(email,passw)
    try:
        user = authe.sign_in_with_email_and_password(email,passw);   
    except:
        message="Invalid Credentials"
        return render(request,"signin.html",{"messg":message})

    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    n=email.split("@")
    return render(request, "home.html",{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'signin.html')

def createpro(request):
    pid=request.POST.get("pid")
    name=request.POST.get("name")
    desc=request.POST.get("desc")
    num=request.POST.get("num")
    mem=request.POST.get("mem")
    n=[]
    n.append(num)
    n.append(mem)

    

    doc_ref1 = db.collection(u'projects').document(name)
    doc_ref1.set({
    u'Project_Name': name,
    u'Project_Id': pid,
    u'Description': desc,
    u'Status': "Just Started",
    })


    for i in n:
        dr = db.collection(u'users').document(str(x))
        doc = dr.get()
        d=dict()
        if doc.exists:
            d=doc.to_dict()
            d['Project_Id']=pid
            d['emailnotifications']:"true"
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "aiattendance2020@gmail.com"  # Enter your address
            receiver_email =d["EmailID"]   # Enter receiver address
            password = "0"
            message = """\
Subject: Project
You got a new project."""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)




