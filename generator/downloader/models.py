from django.db import models

class Resume(models.Model):
    # Basic Information
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField()
    leetcode = models.URLField(default='')
    github = models.URLField(default='')

    # Objective
    objective = models.TextField()

    # Education
    education1 = models.TextField()
    education2 = models.TextField()

    # Skills
    technical_skills = models.TextField()
    soft_skills = models.TextField()
    other_skills = models.TextField()

    # Experience
    experience1 = models.TextField()

    # Projects
    project1 = models.TextField()
    project2 = models.TextField()

    # Extra-Curricular Activities
    activities = models.TextField()

    # Leadership
    leadership = models.TextField()

    def __str__(self):
        return self.name

