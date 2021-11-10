from django.urls import path
from .  import  views

urlpatterns = [
    #path('homepage', views.pageLoad),
    path('', views.loginPage),
    path('register', views.registerPage),
    path('forgot-password', views.forgetPage),
    path('userData', views.login),
    path('logout', views.logoutUser),
    path('userRegister', views.userRegister),
    path('all-members', views.allMembers),
    path('about-college', views.aboutCollege),
    path('software', views.software),
    path('hardware', views.hardware),
    path('docSoftware', views.docSoftware),
    path('docHardware', views.docHardware),
       
]
