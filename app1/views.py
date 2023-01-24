from django.shortcuts import render,redirect
from .models import Display,Orders,Feedbacks
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django .contrib .auth .decorators import login_required

# Create your views here.

def home(request):
    n = Display.objects.all()
    context = {
        'items': n
    }
    return render(request,'home.html',context)
@login_required
def order(request,id):
    d = Display.objects.get(id=id)
    
    context = {
        'items': d
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        ph_number = request.POST.get('ph_number')
        qty = request.POST.get('qty')
        user = request.user                        # get the username
        Orders.objects.create(
            user = user,
            name = name,
            place = place,
            ph_number = ph_number,
            qty = qty
        )
        return redirect('home')
    return render(request,'order.html',context)

def signup(request):

      if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmpassword')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                 messages.error(request,'Email already taken')
                 return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print("user created")
            
        else:
            messages.error(request,'password does not match')
            return redirect('signup')

        return redirect('login')
  
      return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request,'invalid credentials')
            return redirect("login")

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("home")

@login_required
def myorder(request):
    my_order = Orders.objects.filter(user = request.user)
    return render(request,'myorder.html',{'my_order':my_order})

def feedback(request):
    if request.method == 'POST':
        f = request.POST.get('feedback')
        user = request.user
        if len(f)==0:
            messages.error(request,'invalid credentials')
            return redirect("feedback")
        else:
            Feedbacks.objects.create(feedback=f,user=user)
            return redirect('feedback')

    read = Feedbacks.objects.all()


    return render(request,'feedback.html',{'read':read})

def account(request):
    person = {
        'user':request.user
        }
    return render(request,'account.html',person)
