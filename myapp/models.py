from django.db import models
# Create your models here.
class Version(models.Model):
    version = models.CharField(max_length=10)

    def __str__(self):
        return self.version
