from django.urls import path
from .views import AttendanceRecordListView, AttendanceRecordCreateView, AttendanceRecordListAPIView

urlpatterns = [
    path('', AttendanceRecordListView.as_view(), name='attendance_list'),
    path('add/', AttendanceRecordCreateView.as_view(), name='attendance_add'),
    path('api/', AttendanceRecordListAPIView.as_view(), name='attendance_api'),
]