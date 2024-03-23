"""StudentManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import Student_Views, Teacher_Views, Hod_Views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name = 'base'),

    #Login
    path('', views.LOGIN, name = 'login'),
    path('dologin/', views.doLogin, name='dologin'),
    path('dologout/', views.doLogout, name = 'dologout'),

#profile Update

    path('profile/',views.profile, name='profile'),
    path('profileupdate/',views.profile_update, name = 'profileupdate'),


    #This is hod panel url 
    path('hod/home', Hod_Views.HOME, name = 'hodhome'),
    path('hod/addstudent/', Hod_Views.addstudent, name = 'addstudent'),
    path('hod/viewstudent/', Hod_Views.viewstudent, name = 'viewstudent'),
    path('hod/editstudent/<int:id>/', Hod_Views.editstudent, name = 'editstudent'),
    path('hod/deletestudent/<int:id>', Hod_Views.deletestudent, name = 'deletestudent'),
    path('hod/addcourse/', Hod_Views.addcourse, name = 'addcourse'),
    path('hod/viewcourse/', Hod_Views.viewcourse, name = 'viewcourse'),
    path('hod/editcourse/<int:id>/', Hod_Views.editcourse, name = 'editcourse'),
    path('hod/deletecourse/<int:id>/', Hod_Views.deletecourse, name = 'deletecourse'),
    path('hod/addteacher/', Hod_Views.addteacher, name= 'addteacher'),
    path('hod/viewteacher/',Hod_Views.viewteacher, name = 'viewteacher'),
    path('hod/editteacher/<int:id>/', Hod_Views.editteacher, name = 'editteacher'),
    path('hod/deleteteacher/<int:id>/', Hod_Views.deleteteacher, name = 'deleteteacher'),
    path('hod/addsubject/', Hod_Views.addsubject, name= 'addsubject'),
    path('hod/viewsubject/',Hod_Views.viewsubject, name = 'viewsubject'),
    path('hod/editsubject/<int:id>/', Hod_Views.editsubject, name = 'editsubject'),
    path('hod/deletesubject/<int:id>/', Hod_Views.deletesubject, name = 'deletesubject'),
    path('hod/addsession/', Hod_Views.addsession, name= 'addsession'),
    path('hod/viewsession/',Hod_Views.viewsession, name = 'viewsession'),
    path('hod/editsession/<int:id>/', Hod_Views.editsession, name = 'editsession'),
    path('hod/deletesession/<int:id>/', Hod_Views.deletesession, name = 'deletesession'),
    
    path('hod/teacher/Send_Notification/',Hod_Views.Teacher_Send_Notification, name= 'teachersendnotification'),
    path('hod/teacher/save_notification/<int:id>/', Hod_Views.Save_Teacher_Notification, name= 'teachersavenotification'),
    path('hod/teacher/leaveview/', Hod_Views.TeacherLeave_View,name='teacherleaveview'),
    path('hod/teacher/leaveaccept/<int:id>/',Hod_Views.TeacherLeaveAccept,name='teacherleaveaccept'),
    path('hod/teacher/leavereject/<int:id>/',Hod_Views.TeacherLeaveReject,name='teacherleavereject'),
    path('hod/teacher/teacherfeedback/', Hod_Views.teacherfeedback, name='teacherfeedbackreply'),
    path('hod/teacher/teacherfeedbacksave/<int:id>/', Hod_Views.teacherfeedbacksave, name='teacherfeedbacksave'),
    


    path('hod/student/Send_Notification/',Hod_Views.Student_Send_Notification, name= 'studentsendnotification'),
    path('hod/student/save_notification/<int:id>/', Hod_Views.Save_Student_Notification, name= 'studentsavenotification'),
    path('hod/student/leaveview/', Hod_Views.StudentLeave_View,name='studentleaveview'),
    path('hod/student/leaveaccept/<int:id>/',Hod_Views.StudentLeaveAccept,name='studentleaveaccept'),
    path('hod/student/leavereject/<int:id>/',Hod_Views.StudentLeaveReject,name='studentleavereject'),
    path('hod/student/studentfeedback/', Hod_Views.studentfeedback, name='studentfeedbackreply'),
    path('hod/student/studentfeedbacksave/<int:id>/', Hod_Views.studentfeedbacksave, name='studentfeedback'),
    path('hod/student/studentviewattendance/', Hod_Views.View_Attendance, name = 'hodviewattendance'),
    


#this is teacher urls 
    path('teacher/home',Teacher_Views.home, name='teacherhome'),
    path('teacher/notification/', Teacher_Views.notification,name = 'teachernotification'),
    path('teacher/notification/update/<int:id>/',Teacher_Views.notificationupdate,name='teacherstatusupdate'),
    path('teacher/applyleave/', Teacher_Views.applyleave,name='teacherapplyleave'),
    path('teacher/apply/leave/', Teacher_Views.apply,name='teacherleave'),
    path('teacher/feedback/', Teacher_Views.Feedback, name='teacherfeedback'),
    path('teacher/teacherfeedbacksave/', Teacher_Views.TeacherFeedbackSave, name="teacherfeebacksave"),
    path('teacher/takeattendance/', Teacher_Views.Teacher_Attendance, name = 'teachertakeattendance'),
    path('teacher/saveattendance/', Teacher_Views.Save_Attendance, name= 'teachersaveattendance'),
    path('teacher/addresult/', Teacher_Views.Add_Result, name='teacheraddresult'),
    path('teacher/saveresult/<int:id>/', Teacher_Views.Save_Result, name='teachersaveresult'),
    path('teacher/viewattendance/',Teacher_Views.View_Attendance, name = 'teacherviewattendance'),
#this is studebt urls

    path('student/home',Student_Views.home, name='studenthome'),
    path('student/notification/', Student_Views.notification,name = 'studentnotification'),
    path('student/notification/update/<int:id>/',Student_Views.notificationupdate,name='studentstatusupdate'),
    path('student/applyleave/', Student_Views.applyleave,name='studentapplyleave'),
    path('student/apply/leave/', Student_Views.apply,name='studentleave'),
    path('student/feedback', Student_Views.Feedback, name='studentfeedback'),
    path('student/Studentfeedbacksave', Student_Views.StudentFeedbackSave, name="studentfeebacksave"),
    path('student/viewattendance/', Student_Views.View_Attendance,name = 'studentviewattendance'),
    path('student/viewresult/',Student_Views.View_Result, name='studentviewresult'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
