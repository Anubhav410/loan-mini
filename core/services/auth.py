from django.contrib.auth.models import User


class AuthService:
    @staticmethod
    def sign_up(name, email, password, is_staff):
        user = User.objects.create(first_name=name, email=email, username=email, is_staff=is_staff)
        user.set_password(password)
        user.save()

        return user
