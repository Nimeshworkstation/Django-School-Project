from django.shortcuts import render, redirect
from app.models import *
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = 'login')
def HOME(request):
	if request.user.user_type =='HOD':
		student = len(Student.objects.all())
		course = Course.objects.all().count()
		teacher = Teacher.objects.all().count()
		subject = Subject.objects.all().count()

		stud_m = Student.objects.filter(gender='male').count()
		stud_f = Student.objects.filter(gender='female').count()
		print(stud_m)


		context={
		'student_count':student,
		'course_count':course,
		'teacher_count':teacher,
		'subject_count':subject,
		'stud_m':stud_m,
		'stud_f':stud_f
		}
		return render(request,'Hod/home.html',context)
	return redirect('login')

'''--------------------------STUDENT--------------------------------------'''


# Create your views here.
@login_required(login_url = 'login')
def addstudent(request):
	course = Course.objects.all()
	session = Session.objects.all()
	context = {
	'course': course,
	'session': session,
	}
	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		address = request.POST.get('address')
		gender = request.POST.get('gender')
		course = request.POST.get('course_id')
		session = request.POST.get('session_id')
		print(profile_pic,first_name,last_name,email,username,password,address,gender,course,session)
		
		if CustomUser.objects.filter(email=email):
			messages.error(request,'Email already exists ! ')
			return redirect('addstudent')
		elif CustomUser.objects.filter(username=username):
			messages.error(request,'Username ist already taken ! ')
			return redirect('addstudent')
		else:
			user = CustomUser(
				first_name=first_name,
				last_name=last_name,
				email=email,
				username=username, 
				profile_pic=profile_pic,
				user_type='STUDENT'
				)
			user.set_password(password)
			user.save()
			course_id = Course.objects.get(id = course)
			session_id = Session.objects.get(id = session)
			print('---------------', course_id, session_id)
			student = Student(
				user = user,
				address = address, 
				session_year_id= session_id, 
				course_id= course_id,
				gender=gender
				)
			student.save()
			messages.success(request,"Student Saved")
			return render(request,'Hod/studentadd.html',context)
		
	return render(request,'Hod/studentadd.html',context)

@login_required(login_url = 'login')
def viewstudent(request):
	student = Student.objects.all()
	user = CustomUser.objects.all()
	print(student)
	return render(request,'Hod/studentview.html',{'student':student,})

@login_required(login_url = 'login')
def editstudent(request,id):
	student = Student.objects.get(id=id)
	cs = Course.objects.all()
	se = Session.objects.all()
	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		address = request.POST.get('address')
		gender = request.POST.get('gender')
		course = request.POST.get('course_id')
		session = request.POST.get('session_id')

		user = CustomUser.objects.get(username=username)
		user.first_name=first_name
		user.last_name=last_name
		user.email=email
		user.username=username
		if profile_pic  != None and profile_pic != '':
			user.profile_pic = profile_pic
		if password  != None and password != '':
			user.set_password(password)

		user.save()
		course_id = Course.objects.get(id = course)
		session_id = Session.objects.get(id = session)
		student.user = user
		student.address = address
		student.session_year_id= session_id
		student.course_id= course_id
		student.gender=gender
		student.save()		
		messages.success(request,"Details are successfully Updated !")
		return render(request,'Hod/studentedit.html',{'student':student,'session':se,'course':cs})
	
	return render(request,'Hod/studentedit.html',{'student':student,'session':se,'course':cs})


@login_required(login_url = 'login')
def deletestudent(request,id):
	student = Student.objects.get(id=id)
	user = CustomUser.objects.filter(id = student.user_id)
	user.delete()
	messages.success(request,"successfully Deleted !!")
	return redirect('viewstudent')



def View_Attendance(request):

	if request.method == 'POST':
		attendance_report = None
		sessiondisplay = None
		subjectdisplay = None
		session = Session.objects.all()
		subjects = Subject.objects.all()
		session_id=request.POST.get('sessionyear_id')
		attendance_date=request.POST.get('attendance_date')
		subject = request.POST.get('subject_id')

		attendance = Attendance.objects.filter(Q(subject_id_id=subject) & Q(session_year_id_id=session_id) & Q(Attendance_date=attendance_date))
		for i in attendance:
			id = i.id 
			attendance_report = AttendanceReport.objects.filter(attendance_id_id=id)

		sessiondisplay = Session.objects.get(id=session_id)
		subjectdisplay = Subject.objects.get(id=subject)
		context = {
		'subject':subjects,
		'session':session,
		'attendance':attendance_report,
		'sessiondisplay': sessiondisplay,
		'subjectdisplay': subjectdisplay
		}


		return render(request,'Hod/viewattendance.html', context)

	else:
		attendance_report = None
		sessiondisplay = None
		subjectdisplay = None
		session = Session.objects.all()
		subjects = Subject.objects.all()
		context = {
		'subject':subjects,
		'session':session,
		'attendance':attendance_report,
		'sessiondisplay': sessiondisplay,
		'subjectdisplay': subjectdisplay
		}

		return render(request,'Hod/viewattendance.html',context)


'''--------------------------STUDENT END-------------------------------------'''
@login_required(login_url = 'login')
def addcourse(request):
	if request.method == 'POST':
		course = request.POST.get('course_name')
		print(course)

		c=Course(name=course)
		c.save()
		messages.success(request,"Course Added !")
		return redirect('viewcourse')

	return render(request,'Hod/courseadd.html')


@login_required(login_url = 'login')
def viewcourse(request):
	course = Course.objects.all()
	return render(request,'Hod/courseview.html',{'course':course})

@login_required(login_url = 'login')
def editcourse(request,id):
	course = Course.objects.get(id=id)
	if request.method == 'POST':
		course_name =request.POST.get('course_name')
		course.name = course_name
		course.save()
		messages.success(request,' Course Updated successfully!')





		return redirect('viewcourse')

	return render(request,'Hod/courseedit.html',{'course':course})
@login_required(login_url = 'login')
def deletecourse(request,id):
	course = Course.objects.filter(id=id)
	course.delete()
	messages.success(request,"Course deleted successfully")
	return redirect('viewcourse')


'''-----------------------------------------------------------------'''
@login_required(login_url = 'login')
def addteacher(request):
	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		address = request.POST.get('address')
		gender = request.POST.get('gender')
		
		if CustomUser.objects.filter(email=email):
			messages.error(request,'Email already exists ! ')
			return redirect('addteacher')
		elif CustomUser.objects.filter(username=username):
			messages.error(request,'Username ist already taken ! ')
			return redirect('addteacher')
		else:
			user = CustomUser(
				first_name=first_name,
				last_name=last_name,
				email=email,
				username=username, 
				profile_pic=profile_pic,
				user_type='TEACHER'
				)
			user.set_password(password)
			user.save()
			teacher = Teacher(
				user = user,
				address = address, 
				gender=gender
				)
			teacher.save()
			messages.success(request,"Teacher Saved")
			return redirect('viewteacher')
		
	return render(request,'Hod/teacheradd.html')



@login_required(login_url = 'login')
def viewteacher(request):
	teacher = Teacher.objects.all()
	return render(request,'Hod/teacherview.html',{'teacher':teacher})

@login_required(login_url = 'login')
def editteacher(request,id):
	teacher = Teacher.objects.get(id=id)
	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		address = request.POST.get('address')
		gender = request.POST.get('gender')

		user = CustomUser.objects.get(id=teacher.user_id)
		user.first_name=first_name
		user.last_name=last_name
		user.email=email
		user.username=username
		if profile_pic  != None and profile_pic != '':
			user.profile_pic = profile_pic
		if password  != None and password != '':
			user.set_password(password)

		user.save()

		teacher.user = user
		teacher.address = address
		teacher.gender=gender
		teacher.save()

		messages.success(request,' Teacher  Updated successfully!')
		return redirect('viewteacher')

	return render(request,'Hod/teacheredit.html',{'teacher':teacher})
@login_required(login_url = 'login')
def deleteteacher(request,id):
	teacher = Teacher.objects.get(id=id)
	user = CustomUser.objects.filter(id = teacher.user_id)
	user.delete()
	messages.success(request,"successfully Deleted !!")
	return redirect('viewteacher')



'''----------------------------------------------'''
@login_required(login_url = 'login')
def addsubject(request):
	teacher = Teacher.objects.all()
	course = Course.objects.all()
	context={
	'teacher':teacher,
	'course':course
	}
	if request.method == 'POST':
		subject_name = request.POST.get('subject_name')
		course = request.POST.get('course_id')
		teacher= request.POST.get('teacher_id')
		course_name = Course.objects.get(id=course)
		teacher_name = Teacher.objects.get(id =teacher)
		sub = Subject(
			subject_name=subject_name,
			course=course_name,
			teacher=teacher_name
			)
		sub.save()
		messages.success(request,'Subject Added successfully')
		return redirect('viewsubject')
	return render(request,'Hod/subjectadd.html',context)


@login_required(login_url = 'login')
def viewsubject(request):

	subject = Subject.objects.all()
	return render(request,'Hod/subjectview.html',{'subject':subject})

@login_required(login_url = 'login')
def editsubject(request, id):
	teacher = Teacher.objects.all()
	course = Course.objects.all()
	subject = Subject.objects.get(id=id)
	context={
	'teacher':teacher,
	'course':course,
	'subject':subject
	}
	if request.method == 'POST':
		subject_name = request.POST.get('subject_name')
		course = request.POST.get('course_id')
		teacher= request.POST.get('teacher_id')
		course_name = Course.objects.get(id=subject.course_id)
		teacher_name = Teacher.objects.get(id =subject.teacher_id)
		subject.subject_name=subject_name
		subject.teacher=teacher_name
		subject.course =course_name
		subject.save()
		messages.success(request,'Update Successfull ')
		return redirect('viewsubject')
	return render(request,'Hod/subjectedit.html',context)

@login_required(login_url = 'login')
def deletesubject(request, id):
	subject = Subject.objects.get(id=id)
	subject.delete()
	messages.success(request,' Record Deleted ')
	return redirect('viewsubject')


@login_required(login_url = 'login')
def addsession(request):
	if request.method == 'POST':
		session_start = request.POST.get('session_start')
		session_end = request.POST.get('session_end')

		session = Session(

			session_start=session_start,
			session_end=session_end


			)

		session.save()

		
		messages.success(request,'Record added !')
		return redirect('viewsession')
	return render(request,'Hod/sessionadd.html') 


@login_required(login_url = 'login')
def viewsession(request):
	session = Session.objects.all()
	return render(request,'Hod/sessionview.html',{'session':session})


@login_required(login_url = 'login')
def editsession(request,id):
	session = Session.objects.get(id=id)
	if request.method == 'POST':
		session_start = request.POST.get('session_start')
		session_end = request.POST.get('session_end')
		session.session_start=session_start
		session.session_end = session_end
		session.save()
		messages.success(request,'Update Successfull')
		return redirect('viewsession')
	return render(request,'Hod/sessionedit.html',{'session':session})

@login_required(login_url = 'login')
def deletesession(request,id):
	session = Session.objects.get(id=id)
	session.delete()
	messages.success(request,'Record Deleted !')
	return redirect('viewsession')

@login_required(login_url = 'login')
def Student_Send_Notification(request):
	notification = Student_Notification.objects.all()
	students = Student.objects.all()
	return render(request,'Hod/student_notification.html',{'student':students,'notification':notification})


@login_required(login_url = 'login')
def Teacher_Send_Notification(request):
	notification = Teacher_Notification.objects.all()
	teacher = Teacher.objects.all()
	return render(request,'Hod/teacher_notification.html',{'teacher':teacher,'notification':notification})


@login_required(login_url = 'login')
def Save_Student_Notification(request,id):
	if request.method == 'POST':
		message = request.POST.get('message')
		student = Student.objects.get(id=id)

		notification = Student_Notification(

			student_id = student,
			message = message
			)
		notification.save()
		messages.success(request,"Notification sent !!")

		return redirect('studentsendnotification') 

@login_required(login_url = 'login')
def Save_Teacher_Notification(request,id):
	if request.method == 'POST':
		message = request.POST.get('message')
		teacher = Teacher.objects.get(id=id)

		notification = Teacher_Notification(

			teacher_id = teacher,
			message = message
			)
		notification.save()
		messages.success(request,"Notification sent !!")

		return redirect('teachersendnotification')



@login_required(login_url = 'login')
def TeacherLeave_View(request):
	teacher = teacher_leave.objects.all()
	return render(request,'Hod/teacherleave.html',{'teacher':teacher})

@login_required(login_url = 'login')
def TeacherLeaveAccept(request,id):
	teacher = teacher_leave.objects.get(id=id)
	teacher.status = 1
	teacher.save()
	messages.success(request,'Approved !')
	return redirect('teacherleaveview')

@login_required(login_url = 'login')
def TeacherLeaveReject(request,id):
	teacher = teacher_leave.objects.get(id=id)
	teacher.status = 2
	teacher.save()
	messages.success(request,'Rejected !')
	return redirect('teacherleaveview')


def teacherfeedback(request):
	teacherfeedback = Teacher_Feedback.objects.all()
	return render(request,'Hod/teacherfeedbackreply.html',{'teacher':teacherfeedback})


def teacherfeedbacksave(request,id):
	if request.method == 'POST':
		message = request.POST.get('message')
		teacherfeedback = Teacher_Feedback.objects.get(id=id)
		teacherfeedback.feedback_reply = message
		teacherfeedback.save()
		messages.success(request,'Feedback Sent')
		return redirect('teacherfeedbackreply')
	


def studentfeedback(request):
	studentfeedback = Student_Feedback.objects.all()
	return render(request,'Hod/studentfeedbackreply.html',{'student':studentfeedback})


def studentfeedbacksave(request,id):
	if request.method == 'POST':
		message = request.POST.get('message')
		studentfeedback = Student_Feedback.objects.get(id=id)
		studentfeedback.feedback_reply = message
		studentfeedback.save()
		messages.success(request,'Feedback Sent')
		return redirect('studentfeedbackreply')



@login_required(login_url = 'login')
def StudentLeave_View(request):
	student = student_leave.objects.all()
	return render(request,'Hod/studentleave.html',{'student':student})

@login_required(login_url = 'login')
def StudentLeaveAccept(request,id):
	student = student_leave.objects.get(id=id)
	student.status = 1
	student.save()
	messages.success(request,'Approved !')
	return redirect('studentleaveview')

@login_required(login_url = 'login')
def StudentLeaveReject(request,id):
	student = student_leave.objects.get(id=id)
	student.status = 2
	student.save()
	messages.success(request,'Rejected !')
	return redirect('studentleaveview')
