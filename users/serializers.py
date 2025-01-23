from rest_framework import serializers
from .models import Users
import re

def validate_password(password):
    if len(password) < 8:
        raise serializers.ValidationError("password should at leat 8 char long")
    if len(re.findall(r'\d',password)) < 1:
        raise serializers.ValidationError("password should at leat one digit")
    if len(re.findall(r'[A-Z]', password)) > 3 or len(re.findall(r'[A-Z]', password)) < 1:
        raise serializers.ValidationError("password should have atleast 1 and atmost 2 cap letter")
    if len(re.findall(r'[^a-zA-Z\d]', password)) < 1:
        raise serializers.ValidationError("password should at leat one special character")
    return password



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Users
        fields = ['id','email','phone','name', 'password']

    def create(self, validated_data):
        user = Users(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

