from rest_framework import serializers

from homew import models


class Client(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get("firstname", instance.firstname)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.credit_number = validated_data.get("credit_number", instance.credit_number)
        instance.privilege = validated_data.get("privilege", instance.privilege)
        instance.save()

        return instance
