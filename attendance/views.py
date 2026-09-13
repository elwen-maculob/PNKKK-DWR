from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import AttendanceRecord
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import AttendanceRecordSerializer


class AttendanceRecordListView(ListView):
    model = AttendanceRecord
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'records'
    #ordering = ['-date', '-time_in']  # Order by date and time_in in descending order

class AttendanceRecordCreateView(CreateView):
    model = AttendanceRecord
    template_name = 'attendance/attendance_form.html'
    fields = ['staff_name', 'time_in', 'time_out', 'job_title', 'remarks']
    success_url = reverse_lazy('attendance_list')

class AttendanceRecordListAPIView(generics.ListCreateAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer