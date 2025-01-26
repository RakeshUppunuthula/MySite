from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    First_Name =models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email_Address =models.EmailField()
    
    def Full_Name(self):
        return f"{self.First_Name} {self.Last_Name}"
        

    def __str__(self):
        return self.Full_Name()
        

class Tag(models.Model):
    caption=models.CharField(max_length=20) 

    def TagName(self):
        return f"{self.caption}" 

    def __str__(self):
        return self.TagName()


class post(models.Model):
    title = models.CharField(max_length=150)
    Excerpt = models.CharField(max_length=200)
    image_Feild = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
    slug =models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    Author =models.ForeignKey(Author,on_delete=models.SET_NULL, null=True,related_name="posts")
    Tags=models.ManyToManyField(Tag)

    def Title(self):
        return f"{self.title}" 

    def __str__(self):
        return self.Title()



    
 