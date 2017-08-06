from django.shortcuts import render, get_object_or_404
from .models import Post, Topic
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

@login_required
def topic_list(request):
	topics = Topic.objects.all()
	return render(request, 'blog/topic_list.html', {'topics': topics})

@login_required
def post_list(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = Post.objects.filter(topic_id=pk).order_by('-updated_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'topic': topic})

@login_required
def post_detail(request, pk):    
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user            
            post.save()
            messages.success(request, 'Blog was posted.')
            return redirect('post_detail', pk=post.pk)
    else:        
        form = PostForm()        
    return render(request, 'blog/post_edit.html', {'form': form, 'title': 'New Post'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user            
            post.save()
            messages.success(request, 'Blog was updated successfully.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'title': 'Edit Post'})

@login_required
def post_remove(request, pk):    
    post = get_object_or_404(Post, pk=pk)
    topic = get_object_or_404(Topic, pk=post.topic_id) 
    post.delete()
    messages.success(request, 'Blog was deleted.')
    return redirect('post_list', pk=topic.id)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print("Your account is disabled.")
        else:
            print("Invalid login details:", username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'blog/login.html', {})

def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')
