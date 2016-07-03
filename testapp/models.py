from django.db import models
from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='testapp_comment_set')
    message = models.TextField()

