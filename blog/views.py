from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import post

# Create your views here.






def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts =post.objects.all().order_by("-Date")[:3]
    
    # sorted_posts=sorted(all_post,key=get_date)
    # latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html", {"posts":latest_posts})

def posts(request):
    all_posts= post.objects.all()
    return render(request,"blog/all-posts.html", {"all_posts":all_posts})

def post_detail(request,slug):
    # all_post= post.objects.all()
    # identitfied_post =  next(post for post in all_post if post.slug==slug) --first
   # identitfied_post =post.objects.get(slug=slug) -- second

    identitfied_post =get_object_or_404(post,slug=slug)
    return render(request,"blog/post-detail.html" , {"post":identitfied_post,"post_Tags":identitfied_post.Tags.all()})
    
