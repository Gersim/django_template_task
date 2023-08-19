from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=25, null=True, blank=True)
    fuel = models.CharField(max_length=20, null=True, blank=True)
    consumption = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.type


class Job(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    animal = models.CharField(max_length=30, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
