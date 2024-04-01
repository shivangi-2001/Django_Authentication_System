from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    re_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('re_password')
        return super().create(validated_data)

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ('re_password',)