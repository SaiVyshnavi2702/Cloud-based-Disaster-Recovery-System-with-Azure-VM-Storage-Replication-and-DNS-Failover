from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    mailid = models.EmailField(max_length=100)
    college = models.TextField()
    contact = models.BigIntegerField()
    loc = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} from {self.college}"