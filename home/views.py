from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post, Blog
# Create your views here.
#html pages
def home(request):
    # joks= Blog.objects.order_by('-list_date').filter(is_published=True) 
    return render(request,'home/home.html')

def get_blog(request, blog_type):
    if request.method == "GET":
        if blog_type == "jokes":
            blog_type_id = Blog.objects.filter(field="joke")
            # print(blog_type_id[0].id)
            # print(blog_type_id.sno)

            data= Post.objects.filter(field=blog_type_id[0].id)
        elif blog_type == "LoveStory":
            blog_type_id = Blog.objects.filter(field="love story")
            data= Post.objects.filter(field=blog_type_id[0].id)
        elif blog_type == "News":
            blog_type_id = Blog.objects.filter(field="sports")
            data= Post.objects.filter(field=blog_type_id[0].id)
        
        context=  {
            "data":data
        }
        
        return render(request,'home/home.html', context=context)
    return render(request,'home/home.html')

def about(request): 
     return render(request,'home/about.html')

def contact(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def news(request): 
    return render(request,'types/news.html')



def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)



#Authentication APIs
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        #user name should be under 10 characters
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        #username should be alphamumeric
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        #password should match
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')

        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Blog has been successfully created")
        return redirect('home') 

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
  