from django.db import models

# Create your models here.
class Entry(models.Model):
    message = models.CharField(max_length=200)
    user_name = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.message}=>{self.user_name}'
