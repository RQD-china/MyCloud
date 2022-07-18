from django.contrib import admin
from app01.models import Articles
from app01.models import Tags
from app01.models import Cover

# Register your models here.

admin.site.register(Articles)
admin.site.register(Tags)
admin.site.register(Cover)