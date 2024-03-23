from django.shortcuts import render,redirect
from app.models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
	return render(request,'Student/home.html')



@login_required(login_url = 'login')
def notification(request):
	nots = Student_Notification.objects.filter(student_id=request.user.student.id)
	return render(request,'Student/notification.html',{'notification':nots})


@login_required(login_url = 'login')
def notificationupdate(request,id):
	notification = Student_Notification.objects.get(id=id)
	notification.status = 1
	notification.save()
	return redirect('studentnotification')


@login_required(login_url = 'login')
def applyleave(request):
	message = student_leave.objects.all()
	return render(request,'Student/studentapplyleave.html',{'message':message})




@login_required(login_url = 'login')
def apply(request):
	if request.method == 'POST':
		date = request.POST.get('leave_date')
		data = request.POST.get('leave_data')
		student_id = Student.objects.get(id=request.user.student.id)
		print("------------------")
		print(date, data, student_id)
		student = student_leave(
			student_id = student_id,
			date=date,
			data=data
			)
		student.save()
		messages.success(request, "Leave applied ")
		return redirect('studentapplyleave')


@login_required(login_url = 'login')
def Feedback(request):
	student_feedback = Student_Feedback.objects.filter(student_id_id= request.user.student.id)
	return render(request,'Student/feedback.html',{'student':student_feedback})


def StudentFeedbackSave(request):
	if request.method=='POST':
		msg = request.POST.get('feedback')
		stud_id = Student.objects.get(id=request.user.student.id)


		student = Student_Feedback(

				student_id=stud_id,
				feedback=msg,
				feedback_reply=''
			)
		student.save()
		messages.success(request,'Feedback Sent !!')
	

	return redirect("studentfeedback")



def View_Attendance(request):
	if request.method == 'POST':
		subjects = Subject.objects.filter(course_id=request.user.student.course_id)
		attendance_report = AttendanceReport.objects.filter(student_id_id=request.user.student.id, attendance_id__subject_id = request.POST.get('subject_id'))
		return render(request,'Student/attendance.html',{'subject':subjects, 'attendance':attendance_report})

	else:
		attendance = None		
		subject = Subject.objects.filter(course_id=request.user.student.course_id)
		return render(request,'Student/attendance.html',{'subject':subject,'attendance':attendance})



def View_Result(request):
	result = StudentResult.objects.filter(student_id__id=request.user.student.id)
	return render(request,'Student/viewresult.html',{'result':result})