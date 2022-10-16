from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def Login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error = 'yes'    
        except:
            error = 'yes' 
    return render(request,'login.html',locals())

def dashboard(request):
    return render(request,'dashboard.html')

def add_directory(request):
    return render(request,'add_directory.html')

def manage_directory(request):
    return render(request,'manage_directory.html')

def edit_directory(request):
    return render(request,'edit_directory.html')

def delete_directory(request):
    pass

def search_directory(request):
    return render(request,'search_directory.html')

def view_search_data(request):
    return render(request,'view_search_data.html')

def all_record(request):
    return render(request,'all_record.html')

def private_record(request):
    return render(request,'private_record.html')

def public_record(request):
    return render(request,'public_record.html')

def view_all_record(request):
    return render(request,'view_all_record.html')

def change_password(request):
    return render(request,'change_password.html')

def Logout(request):
    logout(request)
    return redirect('index')