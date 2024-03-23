from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = (
		('HOD','HOD'),
		('TEACHER','TEACHER'),
		('STUDENT','STUDENT'),

	)

class CustomUser(AbstractUser):
	user_type = models.CharField(choices=STATUS_CHOICES, max_length = 50)
	profile_pic = models.ImageField(upload_to = 'pic', blank = True, null = True)


class Course(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.name



class Session(models.Model):
	session_start = models.CharField(max_length=100)
	session_end = models.CharField(max_length=100) 
	def __str__(self):
		return self.session_start



class Student(models.Model):
	user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name='student')
	address = models.TextField()
	gender = models.CharField(max_length=10)
	course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
	session_year_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=	True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.first_name + "-" + self.user.last_name



class Teacher(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="teacher")
	address = models.CharField(max_length=100)
	gender = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.user.username


class Subject(models.Model):
	subject_name = models.CharField(max_length = 100)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course')
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject_name

		

class Teacher_Notification(models.Model):
	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_not')
	message = models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(null=True,default=0)
	
	def __str__(self):
	 	return self.teacher_id.user.first_name



class Student_Notification(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	message = models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(null=True,default=0)

	
	def __str__(self):
	 	return self.student_id.user.first_name


class teacher_leave(models.Model):
	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	date = models.CharField(max_length=100)
	data=models.TextField()
	status=models.IntegerField(default=0)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add =True)


	def __str__(self):
		return self.teacher_id.user.first_name + self.teacher_id.user.last_name


class student_leave(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	date = models.CharField(max_length=100)
	data=models.TextField()
	status=models.IntegerField(default=0)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add =True)


	def __str__(self):
		return self.student_id.user.first_name + self.student_id.user.last_name

class Teacher_Feedback(models.Model):
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='teacher_feedback')
	feedback = models.TextField()
	feedback_reply = models.TextField( blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)



	def __str__(self):
		return self.teacher_id.user.first_name


class Student_Feedback(models.Model):
	student_id = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='student_feedback')
	feedback = models.TextField()
	feedback_reply = models.TextField( blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)



	def __str__(self):
		return self.teacher_id.user.first_name


class Attendance(models.Model):
	subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendance')
	Attendance_date = models.DateField()
	session_year_id = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject_id.subject_name



class AttendanceReport(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
	attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='attendance')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.student_id.user.first_name


class StudentResult(models.Model):
	student_id = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='result')
	subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
	assignment_mark = models.IntegerField()
	exam_mark = models.IntegerField()
	created_at= models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now_add=True)
	def str__(self):
		return self.student_id.user.first_name