from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-created_at')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])

        if obj.views_count == 100:
            send_mail(
                subject='Поздравляем! Статья набрала 100 просмотров',
                message=f'Статья «{obj.title}» (ID: {obj.pk}) достигла 100 просмотров!',
                from_email=None,  # берётся из DEFAULT_FROM_EMAIL
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )

        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')