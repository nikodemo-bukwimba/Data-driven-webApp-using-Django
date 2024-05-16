from django.contrib.auth.models import AbstractUser
from django.db import models

#Model for identifying users
class user(AbstractUser):
    is_student = models.BooleanField(default="Faulse")
    is_mentor = models.BooleanField(default="False")
    is_superuser = models.BooleanField(default="False")

#StudentProfile Model
class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.DateField()
    skills = models.TextField()
    goals = models.TextField()
    progress = models.TextField()
    skills_status = models.TextField()

#Mentors profile model
class MentorProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.DateField()
    expertise_area = models.TextField()
    assigned_student = models.ManyToManyField(StudentProfile)

#SkillsProfile Model
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    description = models.TextField()

#ProgressTracking Model
class ProgressTracking(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete = models.CASCADE)
    skills = models.ForeignKey(Skills,on_delete = models.CASCADE)
    date = models.DateField()
    progress_status = models.TextField()
    progress_note = models.TextField()

#MentorshipSession Model
class MentorshipSession(models.Model):
    mentor = models.ForeignKey(MentorProfile,on_delete = models.CASCADE)
    student = models.ForeignKey(StudentProfile,on_delete = models.CASCADE)
    session_date = models.DateField()
    topics_covered = models.TextField()
    feedback = models.TextField()


