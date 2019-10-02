from django.db import models
from django.utils import timezone

class Events(models.Model): 
    #event_id will store spreadsheet link for unique identification of event 
    event_id = models.CharField(max_length=500, unique=True) 
    event_name = models.CharField(max_length=100) 
    total_attendees = models.IntegerField(default=0) 
    check_in_count = models.IntegerField(default=0) 
    created_at = models.DateTimeField(blank=True, null=True) 
    updated_at = models.DateTimeField(blank=True, null=True) 
    
    def create(self): 
        self.created_at = timezone.now() 
        self.save() 
    
    def update(self): 
        self.updated_at = timezone.now() 
        self.save() 
    
    def __str__(self): 
        return self.event_name
