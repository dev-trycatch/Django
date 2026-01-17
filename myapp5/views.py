# from django.shortcuts import render
# from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
# from django.urls import reverse_lazy
# from .models import Posts


# # list view
# class PostListView(ListView):
#     model = Posts
#     template = 'blogs/post_list.html'
#     context_object_name = 'posts'

# # detail view
# class PostDetailView(DetailView):
#     model = Posts
#     template_name = 'blogs/post_detail.html'
#     context_object_name = 'post'


# # create view
# class PostCreateView(CreateView):
#     model = Posts
#     template_name = 'blogs/post_form.html'
#     fields = ['title','content']

# # Update view
# class PostUpdateView(UpdateView):
#     model = Posts
#     template_name = 'blogs/post_form.html'
#     fields = ['title','content']

# # delete view
# class PostDeleteView(DeleteView):
#     method = Posts
#     template_name = 'blogs/post_confirm_delete.html'
#     success_url = reverse_lazy('post_list')



from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Posts


class PostListView(ListView):
    model = Posts
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Posts
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Posts
    fields = ['title', 'content']
    template_name = 'blogs/post_form.html'

class PostUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'content']
    template_name = 'blogs/post_form.html'

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')