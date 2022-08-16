from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Post

class PostListView(ListView):
    #1.모델 지정하기
    model = Post
    #2.변수명 지정
    context_object_name= 'posts'
    #3.templates 지정
    # template_name='blog_list.html'

class PostDetailView(DetailView):
    model=Post
    context_object_name='post'
    
    

