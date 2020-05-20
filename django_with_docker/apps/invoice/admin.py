from django.contrib import admin
from django_with_docker.apps.invoice.models import Invoice

admin.site.register(Invoice)
