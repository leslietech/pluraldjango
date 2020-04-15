from django.contrib import admin
# Import the Meeting and Room models. 
from .models import Meeting, Room

# Register your models here.

# Meeting model is added to the admin panel.
admin.site.register(Meeting)

# Room method is added to the admin panel.
admin.site.register(Room)
