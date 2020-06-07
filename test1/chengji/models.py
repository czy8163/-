from django.db import models

# Create your models here.
class chengji(models.Model):
    bId=models.CharField(max_length=18)
    bname=models.CharField(max_length=10,default='无')
    bgoal=models.DecimalField(max_digits=4,decimal_places=1)
    btime=models.CharField(max_length=8)

    def __str__(self):
        return self.bname