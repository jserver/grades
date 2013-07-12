from django.db import models

# Create your models here.
class Action(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    code = models.CharField(max_length=1)
    desc = models.CharField(max_length=255)

    def __unicode__(self):
        return self.code

class Cuisine(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    desc = models.CharField(max_length=255)

    def __unicode__(self):
        return self.desc

class Violation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    critical = models.BooleanField()
    code = models.CharField(max_length=1)
    desc = models.CharField(max_length=255)

    def __unicode__(self):
        return self.code

class WebExtract(models.Model):
    BORO_CHOICES = (
        (1, 'Manhattan'),
        (2, 'The Bronx'),
        (3, 'Brooklyn'),
        (4, 'Queens'),
        (5, 'Staten Island'),
    )
    camis = models.IntegerField()
    dba = models.CharField(max_length=255)
    boro = models.IntegerField(choices=BORO_CHOICES)
    building = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    cuisine_code = models.ForeignKey(Cuisine, null=True)
    insp_date = models.DateTimeField()
    action = models.CharField(max_length=1)
    viol_code = models.CharField(max_length=3)
    score = models.CharField(max_length=1)
    current_grade = models.CharField(max_length=1)
    grade_date = models.DateTimeField(blank=True, null=True)
    record_date = models.DateTimeField()

    def __unicode__(self):
        return self.dba
