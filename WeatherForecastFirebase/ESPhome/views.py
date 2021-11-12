from django.shortcuts import render
import pyrebase

# Create your views here.
#chnage it 
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

db = firebase.database()

# def pageLoad(request):
# return render(request, 'ESPhome/index.html')
    
def loginPage(request):
    return render(request, 'ESPhome/login.html')

def registerPage(request):
    return render(request, 'ESPhome/register.html')
    
def forgetPage(request):
    return render(request, 'ESPhome/forgot-password.html')

def login(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
        uid = user['localId']
        userId = db.child("user").child(uid).child("details/firstName").get().val()
        # print(userId.val(),"..................data......................")
        currentC = db.child("WF/currentC").get().val()
        currentF = db.child("WF/currentF").get().val()
        humidity = db.child("WF/humidity").get().val()
        # db.child("user").child(uid).child("details").set(data)
        obj = {
            "c":currentC,
            "f":currentF,
            "h":humidity,
            "u":userId
            }
        #print(userId.val(), wfdata.val(),"..................data......................")
    except:
        msg = "Invalid credentials"
        print("error...................")
        return render(request,"ESPhome/404.html",{"m":msg})
    print("sucess......................")
    return render(request, "ESPhome/index.html", {"e": obj})

def logoutUser(request):
    auth.current_user = None
    msg = "logout bye !!!"
    return render(request,'ESPhome/login.html',{"m":msg})


def userRegister(request):
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    passw1 = request.POST.get('password')
    passw2 = request.POST.get('re-password')
    passw = request.POST.get('password')
    try:
        user = auth.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        print(uid,"...........................")
        data = {"firstName": first_name, "lastName": last_name,
                "email": email, "password": passw1}
        db.child("user").child(uid).child("details").set(data)
    except:
        msg = "Invalid credentials"
        return render(request, "ESPhome/404.html", {"m": msg})
    return render(request, "ESPhome/login.html", {"e": email})


def allMembers(request):
    result = []
    C = []
    F = []
    H = []
    TIME = []
    # currentC = db.child("WF/currentC").get().val()
    ref = db.child('Final/currentData/2021-5-17')
    snapshot = ref.order_by_key().get()
    #print(snapshot.val())
    for key in snapshot:
        result.append(key.val())
    for onedata in result:
        C.append(onedata['C'])
        TIME.append(onedata['Time'])
    print(TIME,"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    #for key, val in snapshot.items():
        #print('The {0} dinosaur\'s score is {1}'.format(key, val))
    #print(snapshot.val(),"sssssssssssssssssssssssssssssssssssssss...................")
    return render(request, 'ESPhome/all-members.html', {"val": result})


def aboutCollege(request):
    return render(request, 'ESPhome/about-college.html')


def software(request):
    return render(request, 'ESPhome/software.html')


def hardware(request):
    return render(request, 'ESPhome/hardware.html')


def docSoftware(request):
    return render(request, 'ESPhome/doc-software.html')


def docHardware(request):
    return render(request, 'ESPhome/doc-hardware.html')
