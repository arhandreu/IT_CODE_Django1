from rest_framework import serializers

from homew import models


class Client(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'
