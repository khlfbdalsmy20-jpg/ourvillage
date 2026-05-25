from django.db import models

# 1. موديل متبرعي الدم
class BloodDonor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. موديل الصيدلة والرعاية الطبية
class MedicalService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.title

# 3. موديل المواصلات والرحلات
class TransportTrip(models.Model):
    driver_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=150)
    time = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.driver_name} - {self.destination}"

# 4. موديل خدمات الصيانة والصنايعية
class CraftService(models.Model):
    worker_name = models.CharField(max_length=100)
    craft_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    area = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.worker_name} ({self.craft_type})"