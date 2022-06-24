from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Content
# Create your views here.

class ContentListView(ListView):
    model = Content
    context_object_name = "contents"
    template_name = 'blog/content_list.html'

class ContentDetailView(DetailView):
    model = Content
    context_object_name = "content"
    template_name = 'blog/content_detail.html'