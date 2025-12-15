from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact, BlogPost, Newsletter

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        un=request.POST.get('uname')
        p1=request.POST.get('pass1')
        user=auth.authenticate(username=un,password=p1)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login Successful!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('/login/')
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        company = request.POST.get('company', '')
        service = request.POST.get('service', '')
        message = request.POST.get('message', '')
        
        if full_name and email and service:
            Contact.objects.create(
                full_name=full_name,
                email=email,
                company=company if company else None,
                service=service,
                message=message if message else None
            )
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('/contact/')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    return render(request,'contact.html')

def pricing(request):
    return render(request,'pricing.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        uname = request.POST.get('uname', '')
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')
        
        # Validation
        if not all([fname, lname, email, uname, pass1, pass2]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('/register/')
        
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match!')
            return redirect('/register/')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists!')
            return redirect('/register/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('/register/')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=uname,
                email=email,
                password=pass1,
                first_name=fname,
                last_name=lname
            )
            messages.success(request, 'Registration successful! Please login.')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return redirect('/register/')
    
    return render(request,'register.html')

def blog(request):
    posts = BlogPost.objects.filter(published=True)[:6]
    return render(request,'blog.html', {'posts': posts})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('/')


