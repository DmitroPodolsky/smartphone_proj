from django.contrib import admin
from .models import AirPods, Phones, Phone_comments, Bascet_products, AirPods_comments

admin.site.register(Phones)
admin.site.register(Phone_comments)
admin.site.register(AirPods)
admin.site.register(Bascet_products)
admin.site.register(AirPods_comments)
