from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_('Category name'), max_length=20)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name=_('Post title'), max_length=255)
    body = models.TextField(verbose_name=_('Post content'))
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.CharField(verbose_name=_('Author'), max_length=60)
    body = models.TextField(verbose_name=_('Comment content'))
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'[{self.created_on}] by {self.author} on "{self.post}"'
