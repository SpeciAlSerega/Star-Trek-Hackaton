from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

from django.views import View
from django.urls import reverse


from django.http import HttpResponseRedirect
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

# class Index(View):
#     def get(self, request):

#         return render(request, "app_pet/index.html")

def index(request):
    return render(request, 'app_pet/index.html')

def about(request):
    return render(request, 'app_pet/about.html')

def contacts(request):
    return render(request, 'app_pet/contacts.html')

def service(request):
    return render(request, 'app_pet/service.html')

def add(request):
    return render(request, 'app_pet/add.html')

def cabinet(request):
    return render(request, 'app_pet/add.html')

def card(request):
    return render(request, 'app_pet/card.html')

def news_portal(request):
    n = ['DOOOOg_1__is_awesome']
    return render(request, 'app_pet/news_portal.html', context={'news': n })


# ############################################################################################
#                                 # ПОСТЫ
# ############################################################################################
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'app_pet/posts_list.html', context={'posts': posts })


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'app_pet/post_detail.html'

class PostCreate(ObjectCreateMixin, View):

    model_form = PostForm
    template = 'app_pet/post_create_form.html'

class PostUpdate(View):
    raise_exception = True

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'app_pet/post_update.html', {'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('post_list')
        return render(request, 'app_pet/post_update.html', {'form': bound_form, 'post': post})

# class PostDelete(View):
#     raise_exception = True

#     def get(self, request, slug):
#         post = Post.objects.get(slug__iexact=slug)
#         return render(request, 'app_pet/post_delete.html', {'post': post})

#     def post(self, request, slug):
#         post = Post.objects.get(slug__iexact=slug)
#         post.delete()
#         return redirect('posts_list_url')


# ############################################################################################
#                                 # ТЕГИ
# ############################################################################################

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'app_pet/tags_list.html', context={'tags': tags })

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'app_pet/tag_detail.html'

class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'app_pet/tag_create.html'

class TagUpdate(View):
    raise_exception = True

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'app_pet/tag_update.html', {'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tags_list')
        return render(request, 'app_pet/tag_update.html', {'form': bound_form, 'tag': tag})

# class TagDelete(View):
#     raise_exception = True

#     def get(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         return render(request, 'app/tag_delete.html', {'tag': tag})

#     def post(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         tag.delete()
#         return redirect(reverse('tags_list_url'))