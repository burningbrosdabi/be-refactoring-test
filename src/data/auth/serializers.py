from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework import exceptions
from django.utils.translation import gettext as _

UserModel = get_user_model()

class LoginSerializer(serializers.Serializer):
    """Serializer to support to log in by user id.
    
    We use dj_rest_auth's LoginView with our custom serializer
    Docs: https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#configuration

    """

    user_id = serializers.IntegerField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        password = attrs.get('password')
        user = self.get_auth_user(user_id, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        attrs['user'] = user
        return attrs

    def get_auth_user(self, user_id, password):
        # We need this intermediate step
        # as Django built-in User model set USERNAME_FIELD = "username"
        try:
            username = UserModel.objects.get(pk=user_id).get_username()
        except UserModel.DoesNotExist:
            pass
        else:
            return self._validate_username(username, password)

        return

    def _validate_username(self, username, password):
        return authenticate(username=username, password=password)
