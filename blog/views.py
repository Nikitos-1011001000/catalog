from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-created_at')

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published', 'views_count']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published', 'views_count']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
