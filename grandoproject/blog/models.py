from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

"""
Добавление только опубликованных постов
"""


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


"""
Добавление информации об обновлениях 
для пользователей
"""


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True, db_index=True)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    file = models.FileField(upload_to='uploads_post_for_users/%Y/%m/%d/', blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug, self.publish.year, self.publish.month,
                             self.publish.day])

    def __str__(self):
        return self.title


class Meta:
    ordering = ['-publish']
    indexes = [
        models.Index(fields=['-publish']),
    ]


"""
Модель для комментариев
"""


class Comment(models.Model):
    # связываем комменатрий с постом
    # с помощью ForeignKey
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=69)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

