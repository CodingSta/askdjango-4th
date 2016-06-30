from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.signals import pre_save


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = models.TextField()
    photo = models.ImageField()
    thumbnail = models.ImageField()
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

    # https://docs.djangoproject.com/en/1.9/ref/signals/#django.db.models.signals.post_save
    @staticmethod
    def on_pre_save(sender, **kwargs):
        # if kwargs['created']: pass
        post = kwargs['instance']
        # post.photo
        # post.thumbnail

pre_save.connect(Post.on_pre_save, sender=Post)


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
