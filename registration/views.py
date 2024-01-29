from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            error_message = 'Passwords not matched!'
            return render(request, 'signup.html', {'error_message': error_message})
        elif User.objects.filter(email=email):
            error_message = 'Email Already Exists!'
            return render(request, 'signup.html', {'error_message': error_message})



        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login') #url name

        
    return render(request, 'signup.html')
def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')


        if not username:
            error_message = 'Enter username...'
            return render(request, 'login.html', {'error_message':error_message})

        elif not pass1:
            error_message = 'Enter password...'
            return render(request, 'login.html', {'error_message':error_message})
        
            
        else:
            user = authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Incorrect Password"
                return render(request, 'login.html', {'error_message':error_message})

                

    return render(request, 'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')
