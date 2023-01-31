from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(max_length=100)
    jamb_reg_num = serializers.CharField(max_length=20)
    generated_password = serializers.CharField(max_length=9)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["fullname", "jamb_reg_num", "generated_password", "password"]

    def validate(self, attrs):
        jamb_reg_num_exists = User.objects.filter(jamb_reg_num=attrs["jamb_reg_num"]).exists()

        if jamb_reg_num_exists:
            raise ValidationError("JAMB Registration Number already in use")
        
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.save()

        return user


class ViewUsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "fullname", "jamb_reg_num", "generated_password"]
