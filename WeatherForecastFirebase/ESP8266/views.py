from django.shortcuts import render
import  pyrebase
# Create your views here.

firebaseConfig = {
    'apiKey': "AIzaSyCj_hP9EehgCKz5S7xSA1Y2JrfJJWfY70Q",
    'authDomain': "ashishfirebase-c098f.firebaseapp.com",
    'databaseURL': "https://ashishfirebase-c098f-default-rtdb.firebaseio.com",
    'projectId': "ashishfirebase-c098f",
    'storageBucket': "ashishfirebase-c098f.appspot.com",
    'messagingSenderId': "106423897394",
    'appId': "1:106423897394:web:d61f7904dd2f6201259b2b",
    'measurementId': "G-7KV56MWVQF"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


# def loadHome(request):
#     return render(request, 'ESP8266/esp8266.html')

# def signUp(request):
#     email = request.POST.get('email')
#     passw = request.POST.get('password')
#     try:
#         user = auth.sign_in_with_email_and_password(email,passw)
#     except:
#         msg = "Invalid credentials"
#         return render(request,"ESP8266/esp8266.html",{"m":msg})
#     return render(request,"ESP8266/welcome.html",{"e":email})

# def logOut(request):
#     auth.current_user = None
#     msg = "logout bye !!!"
#     return render(request,'ESP8266/esp8266.html',{"m":msg})