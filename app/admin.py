from django.contrib import admin
from app.models import Pedido, Produto


admin.site.register(Produto)
admin.site.register(Pedido)

# Register your models here.
