from rest_framework import serializers
from .models import Gpio, GpioR1, GpioR2

class GpioR1Serializer(serializers.ModelSerializer):
    class Meta:
        model = GpioR1

    def create(self, validated_data):
        return GpioR1.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pin = validated_data.get('pin', instance.pin)
        instance.command = validated_data.get('command', instance.command)
        instance.param = validated_data.get('param', instance.param)
        instance.save()
        return instance

class GpioR2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GpioR2
        
    def create(self, validated_data):
        return GpioR2.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pin = validated_data.get('pin', instance.pin)
        instance.command = validated_data.get('command', instance.command)
        instance.param = validated_data.get('param', instance.param)
        instance.save()
        return instance
