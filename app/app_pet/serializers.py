from rest_framework import serializers
from app_pet.models import *
class PetModelSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = ['card_pet', 'type_pet', 'breed_of_dog', 'nickname', 'sex']