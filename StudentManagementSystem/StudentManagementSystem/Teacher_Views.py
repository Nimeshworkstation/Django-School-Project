from django.shortcuts import render,redirect
from app.models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'Teacher/home.html')

@login_required(login_url = 'login')
def notification(request):
	nots = Teacher_Notification.objects.filter(teacher_id=request.user.teacher.id)
	return render(request,'Teacher/notification.html',{'notification':nots})


@login_required(login_url = 'login')
def notificationupdate(request,id):
	notification = Teacher_Notification.objects.get(id=id)
	notification.status = 1
	notification.save()
	return redirect('teachernotification')


@login_required(login_url = 'login')
def applyleave(request):
	message = teacher_leave.objects.all()
	return render(request,'Teacher/teacherapplyleave.html',{'message':message})




def Teacher_Attendance(request):
	subjects = Subject.objects.filter(teacher__id = request.user.teacher.id)
	session = Session.objects.all()
	action = request.GET.get('action')
	get_subject = None
	get_session = None
	student = None

	if action is not None:
		if request.method == 'POST':
			subject_id = request.POST.get('subject_id')
			print(subject_id)
			session_id = request.POST.get('sessionyear_id')

			get_subject = Subject.objects.get(id=subject_id)
			get_session=Session.objects.get(id=session_id)
			student = Student.objects.filter(Q(course_id__course__id =subject_id) & Q(session_year_id_id=session_id))
			print(student)

	data={}
	data['subject'] = subjects
	data['session'] = session
	data['get_subject']=get_subject
	data['get_session'] = get_session
	data['action'] = action
	data['student'] = student
	return render(request,'Teacher/takeattendance.html', data)

def Save_Attendance(request):
	if request.method=='POST':
		session_id=request.POST.get('sessionyear_id')
		attendance_date=request.POST.get('attendance_date')
		subject = request.POST.get('subject_id')
		subject_id = Subject.objects.get(id=subject)
		session_year_id = Session.objects.get(id=session_id)
		student_id = request.POST.getlist('student_id')

		print("-------------------",session_year_id, attendance_date, student_id,student_id[0])

		attendance = Attendance(

			session_year_id=session_year_id,
			subject_id=subject_id,
			Attendance_date=attendance_date,
			)
		attendance.save()

		for i in student_id:
			id = i 
			student = Student.objects.get(id=id)
			attendancereport = AttendanceReport(
				student_id=student,
				attendance_id=attendance
				)
			attendancereport.save()

		messages.success(request,'Attendance created ')
		return redirect('teachertakeattendance')




def View_Attendance(request):

	if request.method == 'POST':
		attendance_report = None
		sessiondisplay = None
		subjectdisplay = None
		session = Session.objects.all()
		subjects = Subject.objects.filter(teacher_id = request.user.teacher.id)

		session_id=request.POST.get('sessionyear_id')
		attendance_date=request.POST.get('attendance_date')
		subject = request.POST.get('subject_id')

		attendance = Attendance.objects.filter(Q(subject_id_id=subject) & Q(session_year_id_id=session_id) & Q(Attendance_date=attendance_date))
		print("******************************************",attendance)
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


		return render(request,'Teacher/viewattendance.html', context)

	else:
		attendance_report = None
		sessiondisplay = None
		subjectdisplay = None
		session = Session.objects.all()
		subjects = Subject.objects.filter(teacher_id = request.user.teacher.id)
		context = {
		'subject':subjects,
		'session':session,
		'attendance':attendance_report,
		'sessiondisplay': sessiondisplay,
		'subjectdisplay': subjectdisplay
		}

		return render(request,'Teacher/viewattendance.html',context)






@login_required(login_url = 'login')
def apply(request):
	if request.method == 'POST':
		date = request.POST.get('leave_date')
		data = request.POST.get('leave_data')
		teacher_id = Teacher.objects.get(id=request.user.teacher.id)
		print("------------------")
		print(date, data, teacher_id)
		teacher = teacher_leave(
			teacher_id = teacher_id,
			date=date,
			data=data
			)
		teacher.save()
		messages.success(request, "Leave applied ")
		return redirect('teacherapplyleave')


@login_required(login_url = 'login')
def Feedback(request):
	teacher_feedback = Teacher_Feedback.objects.filter(teacher_id_id= request.user.teacher.id)
	return render(request,'Teacher/feedback.html',{'teacher':teacher_feedback})


def TeacherFeedbackSave(request):
	if request.method=='POST':
		msg = request.POST.get('feedback')
		teacher_id = Teacher.objects.get(id=request.user.teacher.id)


		teacher = Teacher_Feedback(

				teacher_id=teacher_id,
				feedback=msg,
				feedback_reply=''
			)
		teacher.save()
		messages.success(request,'Feedback Sent !!')
	

	return redirect("teacherfeedback")



def Add_Result(request):
	if request.method == 'POST':
		subjectdisplay=None
		sessiondisplay=None
		subject = Subject.objects.filter(teacher__id=request.user.teacher.id)
		session_year = Session.objects.all()


		subject_id = request.POST.get('subject_id')
		session_id = request.POST.get('session_year_id')
		subjectdisplay = Subject.objects.get(id = subject_id)
		sessiondisplay = Session.objects.get(id=session_id)


		students = Student.objects.filter(session_year_id__id=session_id,course_id__course__id=subject_id)
		print(students)


		context={
		'subjects':subject,
		'session_year':session_year,
		'students':students,
		'subjectdisplay':subjectdisplay,
		'sessiondisplay': sessiondisplay
		}
		return render(request,'Teacher/addresult.html',context)




	else:	
		subject = Subject.objects.filter(teacher__id=request.user.teacher.id)
		session_year = Session.objects.all()
		context={
		'subjects':subject,
		'session_year':session_year,
		'students':None
		}
		return render(request,'Teacher/addresult.html',context)



			
def Save_Result(request,id):
	print(id)
	if request.method == 'POST':
		student = request.POST.get('student_id')
		subject = id 
		assignment_mark = request.POST.get('assignment_mark')
		exam_mark = request.POST.get('Exam_mark')

		student_id = Student.objects.get(id=student)
		subject_id = Subject.objects.get(id=subject)
		
		check = StudentResult.objects.filter(student_id=student_id,subject_id=subject_id).exists()
		if check:
			
			studentresult = StudentResult.objects.get(student_id=student_id,subject_id=subject_id)
			studentresult.assignment_mark = assignment_mark
			studentresult.exam_mark = exam_mark
			studentresult.save()
			messages.success(request,'Original Result Updated')
			

		else:

			studentresult = StudentResult(
				student_id=student_id,
				subject_id=subject_id,
				assignment_mark=assignment_mark,
				exam_mark=exam_mark
				)
			studentresult.save()
			messages.success(request,'Result added !!!')
	return redirect('teacheraddresult')
 