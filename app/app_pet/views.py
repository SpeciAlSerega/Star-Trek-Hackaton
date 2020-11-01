from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

from django.views import View
from django.urls import reverse


from django.http import HttpResponseRedirect
from django.views.generic import View

from .models import *
from .utils import *
from .forms import TagForm, PostForm

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from app_pet.serializers import PetModelSerializerModel 

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view




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
    return redirect('http://185.205.210.114:8888/admin/')   

def card(request):
    return render(request, 'app_pet/card.html')

def news_portal(request):
    return redirect('https://www.mos.ru/dgkh/news/')             
    
def news_depart(request):
    return redirect('https://www.mos.ru/dgkh/news/') 

def news_prefect(request):
    return redirect('https://szao.mos.ru/presscenter/news/') 

def news_pitomnics(request):
    return redirect('https://www.rbc.ru/rbcfreenews/5ecbc91a9a794729712062b5') 

def news_calendar(request):##################
    return redirect('https://www.mos.ru/dgkh/news/') 
    
def help_answers(request):#############
    return render(request, 'app_pet/help_answers.html')

def  advice(request):#################
    return render(request, 'app_pet/advice.html')

def  lenta(request):#################
    return render(request, 'app_pet/lenta.html')

def  ii(request):#################
    return render(request, 'app_pet/ii.html')
    


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

#########################       REST        ##############
@api_view(['GET', 'POST'])
def rest_pets(request):
    if request.method == 'GET':
        pets = PetModel.objects.all()
        serializer = PetModelSerializerModel(pets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PetModelSerializerModel(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rest_pets_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        pets = PetModel.objects.all()[pk]
        
    except PetModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PetModelSerializerModel(pets)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PetModelSerializerModel(pets, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


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
class Filing(View):
    def get(self, reqest):
        listOfPets = list(PetModel.objects.values_list("nickname", 'sex', 'breed_of_dog', 'card_pet')) #здесь получаем список объектов питомцев
        
        listOfPrefectures = list(Prefecture.objects.values_list("name", flat=True))
        return render(reqest, 'app_pet/filing/filing.html', {"listOfPets": listOfPets, "listOfPrefectures": listOfPrefectures})
class GetPets(View):
    def get(self,request):
        print(request.GET.get("text"))
        if(request.GET.get("text")!=""):
            listOfPets = list(PetModel.objects.filter(nickname__contains=request.GET.get("text")).values_list("nickname", 'sex', 'breed_of_dog', 'card_pet'))
            
        else:
            listOfPets = list(PetModel.objects.values_list("nickname", 'sex', 'breed_of_dog', 'card_pet'))
        print(len(listOfPets))
        return JsonResponse(listOfPets, safe=False)

# class TagDelete(View):
#     raise_exception = True

#     def get(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         return render(request, 'app/tag_delete.html', {'tag': tag})

#     def post(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         tag.delete()
#         return redirect(reverse('tags_list_url'))

# ############################################################################################
#                                 # ПИТОМЦЫ
# ############################################################################################



class Filing(View):
    def get(self, reqest):
        listOfPets = list(PetModel.objects.values_list("nickname", 'sex', 'breed_of_dog', 'card_pet')) #здесь получаем список объектов питомцев
        
        listOfPrefectures = list(Prefecture.objects.values_list("name", flat=True))
        return render(reqest, 'app_pet/filing/filing.html', {"listOfPets": listOfPets, "listOfPrefectures": listOfPrefectures})
class GetPets(View):
    def get(self,request):
        print(request.GET.get("text"))
        if(request.GET.get("text")!=""):
            listOfPets = list(PetModel.objects.filter(nickname__contains=request.GET.get("text")).values_list("nickname", 'sex', 'breed_of_dog', 'card_pet'))
            
        else:
            listOfPets = list(PetModel.objects.values_list("nickname", 'sex', 'breed_of_dog', 'card_pet'))
        print(len(listOfPets))
        return JsonResponse(listOfPets, safe=False)