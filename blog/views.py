from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    """
    Obsolete
    :param request:
    :return:
    """
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'}
    return render(
        request=request,
        template_name='blog/home.html',
        context=context)


class PostListView(ListView):
    """
    List view with pagination
    """
    model = Post
    template_name = 'blog/home.html'  # <app> / <model>_<viewtype>.html

    context_object_name = 'posts'
    ordering = ['-date_posted', 'title']
    paginate_by = 6


class UserPostListView(ListView):
    """
    List view with pagination
    """
    model = Post
    template_name = 'blog/user_posts.html'  # <app> / <model>_<viewtype>.html

    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content']


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        """
        Only authenticated users can update existing posts
        :return:
        """
        post = self.get_object().author
        if self.request.user == post:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Attach the user name to the form before
        is validated.
        :param form:
        :return:
        """
        form.instance.author = self.request.user
        return super().form_valid(form=form)

    def test_func(self):
        """
        Only authenticated users can update existing posts
        :return:
        """
        post = self.get_object().author
        if self.request.user == post:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Attach the user name to the form before
        is validated.
        :param form:
        :return:
        """
        form.instance.author = self.request.user
        return super().form_valid(form=form)


def about(request: HttpRequest) -> HttpResponse:
    context = {'title': 'about'}
    return render(
        request=request,
        template_name='blog/about.html',
        context=context
    )
