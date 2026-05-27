from django.conf import settings
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name='Текст')
    preview = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name='Автор'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'
        permissions = [
            ('can_manage_blog', 'Can manage blog'),
        ]
