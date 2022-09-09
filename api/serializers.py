from rest_framework import serializers

from .models import Coder


class CoderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    domain = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()

    def create(self,validate_data):
        return Coder.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.domain=validate_data.get('domain',instance.domain)
        instance.compnay=validate_data.get('compnay',instance.domain)
        instance.salary=validate_data.get('salary',instance.salary)
        instance.save()
        return instance
         

