from django.contrib import admin
from app_pet.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from app_pet.forms import *


# Register your models here.
admin.site.register(MyUser, UserAdmin)
admin.site.register(PetModel)
#admin.site.register([CreatedOntology,Triplets,RoleRestrictions,SimpleRulesForOntology])
