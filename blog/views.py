from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # we can handle user by this model
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.core.paginator import Paginator
from .models import Blog_categories, Cantact, BlogPost
# from django.utils.safestring import mark_safe
# Create your views here.

def index(request):
    fetch = Blog_categories.objects.all()
    # username = request.GET.get('name2')
    return render(request, 'index.html', {'items': fetch})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method=='GET':
        return render(request, 'contact.html')
    else:
        postData = request.POST
        full_name = postData['full_name']
        email = postData.get('email')
        password = postData.get('password')
        c_password = postData.get('c_password')

        contact_obj = Cantact()
        contact_obj.full_name = full_name
        contact_obj.email_address = email
        contact_obj.password = password
        contact_obj.save()

        # return redirect('/?name2='+full_name)

def blogmg(request):
    return render(request, 'blog.html')

def handlesignup(request):
    
    # username1 = userData['username']
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        
        # print(firstname, lastname, email, password)
        # form validation
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists")
        elif len(username) > 10:
            messages.warning(request, "Username must be under 10 characters")
        elif not username.isalnum():
            messages.warning(request, "Username should only contain letters and number")
        elif password != c_password:
            messages.warning(request, "Password do not match")
        else:
            # create the user
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            messages.success(request, "Account created")
            return redirect('login')

    return render(request, 'signup.html')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid creadentials, Please try again")

    return render(request, 'login.html')
    # return HttpResponse("404 - Not Found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

    return HttpResponse("logout")

import string
def blogPost(request, slug):
    cat_slg = slug
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     desc = request.POST['desc']

    #     question_obj = Blog()
    #     question_obj.blg_title = title
    #     question_obj.blg_desc = desc
    #     question_obj.cat_slug = slug
    #     question_obj.save()
    
    cat = Blog_categories.objects.filter(slug=slug)
    if cat.exists():
        cat = cat.first()
        que = BlogPost.objects.filter(cat_slug=slug).order_by('id')
        total_que = que.count()
        paginator = Paginator(que, 2, orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # print(page_obj)
        # print(page_obj.has_previous())
        # print(page_obj.has_next())
        # print(page_obj.previous_page_number())
        # print(page_obj.next_page_number())
        # print(page_obj.number)
            
    else:
        return HttpResponse('<h1>Page Not Found</h1>')
    
    return render(request, 'questions.html', {'cat':cat, 'page_obj': page_obj, 'total_que': total_que, 'cat_slg': cat_slg})

def ask(request):
    return render(request, 'ask.html')

# from .forms import AnswerForm
def blogPostDetails(request, cat, slug):
    mk = request.build_absolute_uri()
    print(mk)
    que = BlogPost.objects.filter(slug=slug)
    if que.exists():
        que = que.first()
        # ans = Answer.objects.filter(que_slug=slug)
        # num_answer = ans.count()
        # fm = AnswerForm()
    else:
        return HttpResponse("<h1>Page Not Found</h1>")

    # if request.method == 'POST':
    #     answer = request.POST['answers']
    #     print(answer)
    #     ans_obj = Answer()
    #     ans_obj.answer = answer
    #     ans_obj.que_slug = slug
    #     ans_obj.save()

    return render(request, 'answer.html', {'que': que, 'fetchOnUrl':mk})