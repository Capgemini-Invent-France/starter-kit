from django.db import models


# Create your models here.
class Image(models.Model):
    
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    selected_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        name = f"{self.title}_id_{self.pk}"
        return name
