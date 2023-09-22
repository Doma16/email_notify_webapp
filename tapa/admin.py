from django.contrib import admin
from .models import Tap, Day
from django_q import models as q_models

# Register your models here.
admin.site.register(Tap)
admin.site.register(Day)
#admin.site.register(q_models.Schedule)