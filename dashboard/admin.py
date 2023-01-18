from django.contrib import admin
from .models import Students, Placements, Companies, Marks, Bulletin


# Register your models here.
admin.site.register(Students)
admin.site.register(Placements)
admin.site.register(Companies)
admin.site.register(Bulletin)
admin.site.register(Marks)