from rest_framework import serializers
from .models import Animal
from users.serializers import UserSerializer 

class AnimalSerializer(serializers.ModelSerializer):
    adopted_by = UserSerializer(read_only=True)  # Serialize adopted_by user

    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ['id', 'adopted_by']

