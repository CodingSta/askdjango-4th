from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostModelForm


# 기본 template_name : 모델명_detail.html
post_detail = DetailView.as_view(model=Post)

# 기본 template_name : 모델명_form.html
post_new = CreateView.as_view(model=Post, form_class=PostModelForm)

# 기본 template_name : 모델명_form.html
post_edit = UpdateView.as_view(model=Post, form_class=PostModelForm)

# 기본 template_name : 모델명_confirm_delete.html
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:index'))
