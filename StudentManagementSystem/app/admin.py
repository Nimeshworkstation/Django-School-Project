from django.contrib import admin
from .models import CustomUser, Course, Session, StudentResult, Student, Teacher, Subject, Teacher_Notification, Student_Notification, teacher_leave, Teacher_Feedback, AttendanceReport, Attendance
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	list_display = ['username','user_type','profile_pic']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['id','name','created_at','updated_at']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
	list_display = ['id','session_start','session_end']

@admin.register(Student)
class SessionAdmin(admin.ModelAdmin):
	list_display = ['id','address','gender']


@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['id','address','gender','created_at','updated_at']

@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['id','teacher','course','created_at','updated_at']


@admin.register(Teacher_Notification)
class TeacherNotificationAdmin(admin.ModelAdmin):
	list_display=['id','teacher_id','message','created_at']


@admin.register(Student_Notification)
class TeacherNotificationAdmin(admin.ModelAdmin):
	list_display=['id','student_id','message','created_at']

@admin.register(teacher_leave)
class StaffleaveAdmin(admin.ModelAdmin):
	list_display=['id','teacher_id','date','status']


@admin.register(Teacher_Feedback)
class Teacher_FeedbackAdmin(admin.ModelAdmin):
	list_display=['id','teacher_id','feedback','feedback_reply']


@admin.register(AttendanceReport)
class AttendanceReportAdmin(admin.ModelAdmin):
	list_display=['id','student_id']



admin.site.register(Attendance)
admin.site.register(StudentResult)
