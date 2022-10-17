from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from directory.models import UserDetails
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    userdetail = UserDetails.objects.filter(status='public')           
    return render(request,'index.html',locals())

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
    if not request.user.is_authenticated:
        return redirect('admin-login')   
    sd = None
    if request.method == 'POST':
        sd = request.POST.get('searchdata')
        try:
            userdetail = UserDetails.objects.filter(
                                        Q(FirstName__icontains=sd)|
                                        Q(LastName=sd)|
                                        Q(Contact=sd)
                                    )
        except:
            userdetail = ''
    return render(request,'search_directory.html',locals())

def view_search_data(request,pid):
    userdetail = UserDetails.objects.get(id=pid)
    return render(request,'view_search_data.html',locals())

def all_record(request):
    if not request.user.is_authenticated:
        return redirect('admin-login') 
    userdetail = UserDetails.objects.all()             
    return render(request,'all_record.html',locals())

def private_record(request):
    if not request.user.is_authenticated:
        return redirect('admin-login') 
    userdetail = UserDetails.objects.filter(status='private')             
    return render(request,'private_record.html',locals())

def public_record(request):
    if not request.user.is_authenticated:
        return redirect('admin-login') 
    userdetail = UserDetails.objects.filter(status='public')         
    return render(request,'public_record.html',locals())

def view_all_record(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin-login') 
    userdetail = UserDetails.objects.get(id=pid)         
    return render(request,'view_all_record.html',locals())

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''   
    user = request.user     
    if request.method == 'POST':
        # print(request.POST)
        o = request.POST.get('oldpassword')
        n = request.POST.get('newpassword')
        u = User.objects.get(id=request.user.id)
        try:
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'    
        except:
            error = 'yes'        
    return render(request,'change_password.html',locals())

def Logout(request):
    logout(request)
    return redirect('index')