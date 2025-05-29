from django.db import models

class Herb(models.Model):
    local_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    common_use = models.TextField()
    preparation = models.TextField()
    precautions = models.TextField()
    image = models.ImageField(upload_to='herb_images/', blank=True, null=True)
    location = models.CharField(max_length=255, help_text="Where this herb is commonly found")
    

    def __str__(self):
        return self.local_name
