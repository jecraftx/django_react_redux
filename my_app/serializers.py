from rest_framework import serializers
from my_app import models

class TextmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextModel
        fields = "__all__"