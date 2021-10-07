from App_Login.models import UserProfile
from typing import List
from django.db import models
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView , ListView, DeleteView ,View ,TemplateView ,DeleteView
from .forms import CommentForm
from .models import Blog , Comment , Like
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.core.paginator import Paginator

# Create your views here.


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ['blog_title' , 'blog_content', 'blog_image' ]
    
    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author= self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" " , "-") + "-" +str(uuid.uuid4()) 
        blog_obj.save()
        return HttpResponseRedirect(reverse('Index'))


# class BlogList(LoginRequiredMixin, ListView ):
#     model = Blog
#     context_object_name = 'blogs'
#     template_name = 'App_Blog/blog_list.html'
    
#     def get_context_data(self,**kwargs):
#         context = super(BlogList,self).get_context_data(**kwargs)
#         context['latest_blogs'] = Blog.objects.order_by('-published')[:2]
        
        return context

@login_required
def BlogList(request):
    #setup pagination
        latest_blogs = Blog.objects.order_by('-published')[:2]
        p = Paginator(Blog.objects.all() , 8)
        page = request.GET.get('page')
        blogs = p.get_page(page)
        return render(request , 'App_Blog/blog_list.html' , context={'latest_blogs' : latest_blogs , 'paginated_blogs' : blogs})

@login_required
def blog_details(request , slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Like.objects.filter(blog=blog , user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    total_likes = Like.objects.filter(blog=blog)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:BlogDetails' , kwargs={'slug':slug}))
    suggested_blogs = Blog.objects.order_by('-published')[:3]
    return render(request , 'App_Blog/blog_details.html',context={'blog':blog , 'suggested_blogs' : suggested_blogs ,'form':comment_form , 'liked' : liked , 'total_likes':total_likes})


@login_required
def like(request, pk):
    blog  = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog , user=user)
    if not already_liked:
        liked_post = Like(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:BlogDetails', kwargs={'slug':blog.slug}))

@login_required
def unlike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(user=user , blog=blog)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:BlogDetails', kwargs={'slug':blog.slug}))

@login_required
def author_profile(request , author):
    author_profile = UserProfile.objects.get(username = author)
    return render(request , 'App_Blog/author_profile.html' , context={'profile' : author_profile})