from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, correo=None, contraseña=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=correo)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(contraseña):
                return user
        return None