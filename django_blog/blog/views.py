from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserCreationForm
from django.contrib import messages
# from django.contrib.auth.models import User

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.
"""
def home(request):
    # Optional: pass data to the template
    context = {
        'title': 'Welcome to My Django Blog',
        'message': 'Hello! This is your home page.',
        'current_year': 2025
    }
    
    return render(request, 'blog/base.html', context)
"""
def home(request):

    return render(request, 'blog/home.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})

# def register(request):
#     form = RegisterForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponse("<p> suucess full regi</p>")
#     # else:
#     #     form = RegisterForm()
#     return render(request, 'blog/register.html', {'form': form})  


@login_required
def profile(request):
    return render(request, 'blog/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
        return redirect('profile')

    return render(request, 'blog/profile_update.html')



# 1️⃣ LIST VIEW (Public)
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


# 2️⃣ DETAIL VIEW (Public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context


# 3️⃣ CREATE VIEW (Authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# 4️⃣ UPDATE VIEW (Only author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# 5️⃣ DELETE VIEW (Only author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs["post_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.id})
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Comment
        form_class = CommentForm
        template_name = "blog/comment_form.html"

        def test_func(self):
           comment = self.get_object()
           return self.request.user == comment.author

        def get_success_url(self):
            return reverse_lazy("post-detail", kwargs={"pk": self.object.post.id})
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Comment
        template_name = "blog/comment_confirm_delete.html"

        def test_func(self):
            comment = self.get_object()
            return self.request.user == comment.author

        def get_success_url(self):
            return reverse_lazy("post-detail", kwargs={"pk": self.object.post.id})


from django.shortcuts import get_object_or_404
from django.db.models import Q

class PostByTagView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag_slug'])

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()
