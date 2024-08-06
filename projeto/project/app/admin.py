from django.contrib import admin
from .models import Item
from .models import Clients

# Registrando o modelo Item no admin
admin.site.register(Item)
admin.site.register(Clients)
