from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

from directory.models import UserDetails

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
    if not request.user.is_authenticated:
        return redirect('admin-login')
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        Contact = request.POST.get('Contact')
        Gender = request.POST.get('Gender')

        Hobbies = ','.join(request.POST.getlist('Hobbies'))

        placeofBirth = request.POST.get('placeofBirth')
        placeofWork = ','.join(request.POST.getlist('placeofWork'))

        profession = request.POST.get('profession')
        Address = request.POST.get('Address')
        try:
            
            userdetail = UserDetails.objects.create(
                                                FirstName=FirstName,LastName=LastName,
                                                Email=Email,
                                                Contact=Contact,Gender=Gender,
                                                Hobbies=Hobbies,
                                                placeofBirth=placeofBirth,
                                                placeofWork=placeofWork,
                                                Address=Address,status='public'
                                                )
            error = 'no'                                    
            try:
                image = request.FILES['image']
                userdetail.image = image
                userdetail.save()
                # error = 'no'
            except:
                pass
                # error = 'yes'                                    
        except:
            error = 'yes'
    return render(request,'add_directory.html',locals())

def manage_directory(request):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    userdetail = UserDetails.objects.all()    
    return render(request,'manage_directory.html',locals())

def edit_directory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    userdetail = UserDetails.objects.get(id=pid)    

    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        Contact = request.POST.get('Contact')
        Gender = request.POST.get('Gender')
        status = request.POST.get('status')

        Hobbies = ','.join(request.POST.getlist('Hobbies'))

        placeofBirth = request.POST.get('placeofBirth')

        placeofWork = ','.join(request.POST.getlist('placeofWork'))

        profession = request.POST.get('profession')
        Address = request.POST.get('Address')
        try:
            userdetail.FirstName = FirstName
            userdetail.LastName = LastName
            userdetail.Email = Email
            userdetail.Contact = Contact
            userdetail.Gender = Gender
            userdetail.status = status

            if Hobbies !='':
                userdetail.Hobbies = Hobbies


            if placeofWork !='':
                userdetail.placeofWork = placeofWork                
 
            error = 'no'                                    
            try:
                image = request.FILES['image']
                userdetail.image = image
                userdetail.save()
            except:
                pass                                
        except:
            error = 'yes'    
    return render(request,'edit_directory.html',locals())

def delete_directory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    userdetail = UserDetails.objects.get(id=pid)  
    userdetail.delete()
    return redirect('manage-directory')    


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