from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this 'cause we need confirm password field in our Registratin Request
    confirm = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "password", "confirm", "country"]
        extra_kwargs = {
                "password": {
                    "write_only": True
                }
            }

    # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
        password = attrs.get("password")
        confirm = attrs.get("confirm")
        if password != confirm:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match"
            )
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name", "country"]
