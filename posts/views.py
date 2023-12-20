from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from .models import Post, PostComment, Tag, Category
from .forms import PostCommentForm
from django.http import HttpResponseRedirect



class PostListView(TemplateView):
    queryset = Post.objects.all()
    template_name = "posts/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.queryset
        return context
    
class PostDetailView(TemplateView):
    model = Post
    template_name = "posts/post.html"
    form_class = PostCommentForm

    def get_object(self, **kwargs):
        return get_object_or_404(self.model, slug=kwargs.get("post_slug"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object(**kwargs)
        context['form'] = self.form_class()
        return context
    
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = self.get_object(**kwargs)
            instance.post.save()
            instance.save()
            form.save()
            return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))
    


