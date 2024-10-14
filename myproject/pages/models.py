from django.db import models

# Create your models here.
class Page(models.Model):
    titre =models.CharField(max_length=100)
    corp =models.TextField()
    lingot= models.SlugField()
    date= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='fallback.png',blank=True)
    
    def __str__(self) -> str:
        return self.titre