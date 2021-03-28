from django.db import models

# Create your models here.
class Facility(models.Model):
    facility_ID = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

class Equipment(models.Model):
    equipment_ID = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=500)
    purpose = models.CharField(max_length=1500)

class Mass_spectrometer(models.Model):
    num_of_people_trained = models.IntegerField()
    num_of_researchers = models.IntegerField()
    num_of_publications = models.IntegerField()
    num_of_samples = models.IntegerField()
    equipment_ID = models.CharField(max_length=200, primary_key=True)
    facility_ID = models.ForeignKey(Facility, on_delete=models.CASCADE)

class Confocal_microscope(models.Model):
    num_of_people_trained = models.IntegerField()
    num_of_researchers = models.IntegerField()
    num_of_publications = models.IntegerField()
    num_of_samples = models.IntegerField()
    equipment_ID = models.CharField(max_length=200, primary_key=True)
    facility_ID = models.ForeignKey(Facility, on_delete=models.CASCADE)

class Flow_cytometer(models.Model):
    num_of_people_trained = models.IntegerField()
    num_of_researchers = models.IntegerField()
    num_of_publications = models.IntegerField()
    num_of_samples = models.IntegerField()
    equipment_ID = models.CharField(max_length=200, primary_key=True)
    facility_ID = models.ForeignKey(Facility, on_delete=models.CASCADE)

class Centrifuge(models.Model):
    num_of_people_trained = models.IntegerField()
    num_of_researchers = models.IntegerField()
    num_of_publications = models.IntegerField()
    num_of_samples = models.IntegerField()
    equipment_ID = models.CharField(max_length=200, primary_key=True)
    facility_ID = models.ForeignKey(Facility, on_delete=models.CASCADE)

class Fluorometer(models.Model):
    num_of_people_trained = models.IntegerField()
    num_of_researchers = models.IntegerField()
    num_of_publications = models.IntegerField()
    num_of_samples = models.IntegerField()
    equipment_ID = models.CharField(max_length=200, primary_key=True)
    facility_ID = models.ForeignKey(Facility, on_delete=models.CASCADE)