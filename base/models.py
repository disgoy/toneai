from django.db import models

# Create your models here.
class Texts(models.Model):
    text_input=models.TextField()
    classification=models.TextField(null=True)
    text_response=models.TextField(null=True)
    created_at= models.DateTimeField()
    
    def __str__(self):
        if (len(self.text_input) > 10):
            return self.text_input[:10]
        return self.text_input