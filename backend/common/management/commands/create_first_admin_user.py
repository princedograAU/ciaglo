from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
        create first admin user for admin login
        """
        User = get_user_model()
        admin_email = "admin@example.com"
        if not User.objects.count():
            print("Creating admin user ...")
            User.objects.create_superuser(admin_email, admin_email, "admin@1234#")
        else:
            print("Skip create admin user as it already exists")
