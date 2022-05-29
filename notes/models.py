from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class notes(models.Model):
    notes_id = models.AutoField(primary_key=True)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=50, default="")
    year = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to = "notes/image",default = "")
    
    def __str__(self):
        return self.subject
class DBMS(models.Model):
    chapter_id = models.ForeignKey(notes, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=500)
    teacher_name = models.CharField(max_length=500)
    file = models.FileField(upload_to = "notes/images",default="")
    

    def __str__(self):
        return self.topic_name 

class Contact(models.Model):
   msg_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length = 30)
   email = models.EmailField(max_length = 50)
   message = models.CharField(max_length = 500)
   def __str__(self):
        return self.name 

class Notice(models.Model):
    notice_name = models.CharField(max_length = 500)
    date = models.DateTimeField()
    notice_file = models.FileField(upload_to = "notes/notices",default="")
    def __str__(self):
        return self.notice_name 