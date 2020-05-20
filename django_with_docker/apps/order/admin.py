from django.contrib import admin

from django_with_docker.apps.order.models import Order

admin.site.register(Order)
