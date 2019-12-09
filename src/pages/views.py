
from posts.forms import CommentForm
from django.shortcuts import render
from posts.models import Post
from subscriptions.models import Signup

def home(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    
    context = {
        'object_list': featured, 
        'latest': latest
       
    }
    return render(request, 'home.html', context)

