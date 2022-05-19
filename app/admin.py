from django.contrib import admin
from .models import Presaved_labs
from .models import Saved_labs
from .models import Lab_description

admin.site.register(Presaved_labs)
admin.site.register(Saved_labs)
admin.site.register(Lab_description)
# Register your models here.
