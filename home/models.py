from django.db import models

# Create your models here.
class course(models.Model):
    courseCode = models.CharField(max_length=20,primary_key=True,blank=False)
    courseName = models.CharField(max_length=100,blank=False)
    courseTeacher = models.CharField(max_length=50,blank=False)
    courseSeason = models.CharField(max_length=10,blank=False)
    courseKey = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.courseCode