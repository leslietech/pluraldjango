from django.db import models
from datetime import time

# Create your models here.

# Rooms model
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor}"

# Meetings model
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    # Foreign key that links the room to a meeting. The 'on_delete=models.CASCADE' ensures that
    # all meetings tied to a room are deleted when a room is deleted.
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # This functions defines a room's display name.
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
