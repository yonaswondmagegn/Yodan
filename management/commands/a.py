from django.contrib.auth.models import User

if not User.objects.filter(is_superuser=True).exists():
    user = User.objects.create_superuser('yonas', 'yonas@1996', 'yonas@1996')

