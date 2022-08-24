from django.db import models

# Create your models here.

class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    lname = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    problem = models.CharField(max_length=30, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    titlexp = models.CharField(max_length=1000, default="")
    head1 = models.CharField(max_length=500, default="")
    exp0 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    exp2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    thumbnail1 = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title


