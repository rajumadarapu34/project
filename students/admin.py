from django.contrib import admin
from .models import Student, Subject, Marks, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'phone', 'admission_date')
    search_fields = ('user__username', 'course')
    list_filter = ('course', 'admission_date')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score')
    list_filter = ('subject',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('status', 'date')
