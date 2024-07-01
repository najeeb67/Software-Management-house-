from django.db import models


class Employee(models.Model):
    profile_picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    department = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    location = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    
    def __str__(self):
        return self.email
    
    
class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    
    def __str__(self):
        return self.project_name

