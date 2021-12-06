from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=300)
  date = models.DateTimeField()
  text = models.TextField()
  image = models.ImageField(upload_to='event_images')

  def get_summary(self):
    return ''.join(self.text[:70] + '...') if len(self.text) > 70 else self.text

  def __str__(self):
    return self.title