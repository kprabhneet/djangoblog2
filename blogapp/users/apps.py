from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'blogapp.users'

    def ready(self):
        import blogapp.users.signals