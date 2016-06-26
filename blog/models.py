from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = models.TextField()
    photo = models.ImageField()
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags.all(),
        }



class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
