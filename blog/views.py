from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import post
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def get_date(post):
    return post["date"]


class staring_page(ListView):
    template_name = "blog/index.html"
    model = post
    ordering = ["-Date"]
    context_object_name = "posts"

    def get_queryset(self):
        querySet = super().get_queryset()
        data = querySet[:3]
        return data


# def starting_page(request):
#     latest_posts =post.objects.all().order_by("-Date")[:3]

#     # sorted_posts=sorted(all_post,key=get_date)
#     # latest_posts=sorted_posts[-3:]
#     return render(request,"blog/index.html", {"posts":latest_posts})


# def posts(request):
#     all_posts= post.objects.all()
#     return render(request,"blog/all-posts.html", {"all_posts":all_posts})


class allPostListView(ListView):
    model = post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"


# def post_detail(request,slug):
#     # all_post= post.objects.all()
#     # identitfied_post =  next(post for post in all_post if post.slug==slug) --first
#    # identitfied_post =post.objects.get(slug=slug) -- second

#     identitfied_post =get_object_or_404(post,slug=slug)
#     return render(request,"blog/post-detail.html" , {"post":identitfied_post,"post_Tags":identitfied_post.Tags.all()})


class post_detail(View):
    def saved_for_later(self,request,post_id):
        stored_posts=request.session.get("stored_posts")

        if stored_posts is not None:
            is_saved_for_later =post_id in stored_posts
        else:
                is_saved_for_later =False

        return    is_saved_for_later      

  

    def get(self, request, slug):


        Post = post.objects.get(slug=slug)

        

       
        context = {
            "post": Post,
            "post_tags": Post.Tags.all(),
            "comment_form":CommentForm(),
            "comments":Post.comments.all().order_by("-id"),
            "saved_for_later":self.saved_for_later(request,Post.id)
        }
        return render(request, "blog/post-detail.html",context)

    def post(self, request,slug):
        comment_form=CommentForm(request.POST)
        Post = post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment =comment_form.save(commit=False)
            comment.post=Post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        context = {
            "post": Post,
            "post_tags": Post.Tags.all(),
            "comment_form":comment_form,
            "comments":Post.comments.all().order_by("-id"),
            "saved_for_later":self.saved_for_later(request,post.id)
        }
        return render(request, "blog/post-detail.html",context)

class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context ={}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"] =False
        else :
            Posts =post.objects.filter(id__in=stored_posts)
            context["posts"]=Posts
            context["has_posts"] =True
        return render(request,"blog/stored-posts.html",context)    
  
    def post(self,request):
        stored_posts=request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts=[]

        post_id =int(request.POST['post_id'])


        if post_id not in stored_posts:
            stored_posts.append(post_id) 
           
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts']=stored_posts
        return HttpResponseRedirect("/")      
             
            
         


      

    
