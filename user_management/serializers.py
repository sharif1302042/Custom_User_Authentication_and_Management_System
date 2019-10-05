from rest_framework import serializers
from .models import User

class UserCreationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def save(self):
        username = self.validated_data['username']
        if self.validated_data['password1'] == self.validated_data['password2']:
            print("yes")
            password = self.validated_data['password1']
            user = User.objects.create_user(username==username,password=password)
            return user
        else:
            print("no")
            return None

    # def create(self, validated_data):
    #     if validated_data['password1'] and validated_data['password2'] and validated_data['password1'] ==validated_data['password2']:
    #         user = User.objects.create_user(username=validated_data['username'], password=validated_data['password1'])
    #         return user





