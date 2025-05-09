from rest_framework import serializers
from .models import Todo    

class TodoSerializer(serializers.ModelSerializer):            #Defining a serializer for the Todo model using ModelSerializer
    class Meta:
        model = Todo
        fields = '__all__'                                    #Using '__all__' to include all fields in the model