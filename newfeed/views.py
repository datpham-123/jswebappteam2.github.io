from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from newfeed.forms import CommentForm, ConfessionForm, CommentForm_1
from users. models import Profile
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
 )
from .models import Post, Comment, Post_Confession, Sent_Confession, Comment_1
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'newfeed/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'newfeed/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #change order: newest to oldest
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'newfeed/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #change order: newest to oldest
    paginate_by = 5

    #import django shortcuts get_object_or_404
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
     model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def cfs_home(request):
    context = {
        'cfss' : Post_Confession.objects.all()
    }
    return render(request,'newfeed/cfs_home.html',context)


class CfsListView(ListView):
    model = Post_Confession
    template_name = 'newfeed/cfs_home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cfss'
    #change order: newest to oldest
    ordering = ['-date_posted']
    paginate_by = 5


def user_home(request):
    context = {
        'profiles' : Profile.objects.all()
    }
    return render(request,'newfeed/user_home.html',context)

class UserListView(ListView):
    model = Profile
    template_name = 'newfeed/user_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'profiles'
    # change order: newest to oldest
    paginate_by = 5


def about(request):
    return render(request,'newfeed/about.html',{'title':'About'})
def training(request):
    return render(request,'newfeed/Training.html',{'title':'Training'})
def document(request):
    return render(request,'newfeed/Document.html',{'title':'Document'})
def Event1(request):
    return render(request,'newfeed/Event1.html',{'title':'Event1'})
def Event2(request):
    return render(request,'newfeed/Event2.html',{'title':'Event2'})
def Event3(request):
    return render(request,'newfeed/Event3.html',{'title':'Event3'})
def Event4(request):
    return render(request,'newfeed/Event4.html',{'title':'Event4'})
def JSclub(request):
    return render(request,'newfeed/main.html',{'title':'JS_club'})


class CfsDetailView(DetailView):
    model = Post_Confession


def sentconfession(request):
    form = ConfessionForm()
    if request.method == 'POST':
        form = ConfessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your confession has been sent!!!')
    return render(request,'newfeed/confession.html',{'form':form})

def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,author=request.user,post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
            # 21:
    return render(request, "newfeed/post_detail.html", {"post":post, "form":form})

def post_confession(request,pk):
    post = get_object_or_404(Post_Confession, pk=pk)
    form = CommentForm_1()
    if request.method == 'POST':
        form = CommentForm_1(request.POST,author=request.user,post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, "newfeed/cfs_detail.html", {"post":post, "form":form})