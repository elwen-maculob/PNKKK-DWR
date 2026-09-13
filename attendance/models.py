from django.db import models

# Create your models here.
class AttendanceRecord(models.Model):
    staff_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.staff_name} - {self.date}"