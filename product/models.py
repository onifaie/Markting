from django.db import models
from django.db.models.enums import Choices

# Creat
# 
# 
# 
# 
class Test(models.Model):


    Brand = (
        ("BMW", "BMW"),
        ("Nessan", "Nessan"),
        ("Tyota", "Tyota"),
    
    )
    Proname = models.CharField(max_length=100,blank=True, null=True)
    Brand = models.CharField(max_length=8,choices=Brand,blank=True, null=True)


    def __str__(self):
        return self.Proname 

class product(models.Model):
    proname = models.CharField(max_length=100, blank=True, null=True)
    Test = models.ForeignKey(Test,max_length=100,on_delete=models.CASCADE)
    create_dt=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='phtop')
    
   
   
    def __str__(self):
       return self.proname


