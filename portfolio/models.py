from django.db import models

class portfolio(models.Model):
    name = models.CharField(max_length=40)
    link=models.CharField(max_length=30,blank=False)
    image=models.ImageField(upload_to='portfolio')
    def __str__(self):
        return self.name
    
