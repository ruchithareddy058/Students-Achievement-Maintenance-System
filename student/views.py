from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from student.models import studregister,register,details,adetails,Document
# Create your views here.
def home(request):
	return render(request,'home.html')
def login(request):
	if request.COOKIES.get("cid1"):
		return render(request,"login.html",{'cookie1':request.COOKIES['cid1'],
			'cookie2':request.COOKIES['cid2']})
	return render(request,"login.html")
def login1(request):
	if request.COOKIES.get("cid3"):
		return render(request,"login1.html",{'cookie3':request.COOKIES['cid3'],
			'cookie4':request.COOKIES['cid4']})
	return render(request,"login1.html")
def uregister(request):
	if request.method=='POST':
		uname=request.POST['uname']
		email=request.POST['email']
		password=request.POST['password']
		user=User.objects.create_user(username=uname,password=password,email=email)
		user.save()
		data=studregister(uname=uname,email=email,password=password)
		data.save()
		messages.success(request,"Registration Successful!!!")
		return render(request,'uregister.html')
	else:
		return render(request,'uregister.html')
def facregister(request):
	if request.method=='POST':
		uname=request.POST['uname']
		email=request.POST['email']
		password=request.POST['password']
		user=User.objects.create_user(username=uname,password=password,email=email)
		user.save()
		data=register(uname=uname,email=email,password=password)
		data.save()
		messages.success(request,"Registration Successful!!!")
		return render(request,'facregister.html')
	else:
		return render(request,'facregister.html')
def main(request):
	if request.method=='POST':
		uname=request.POST['uname']
		password=request.POST['password']
		user=authenticate(request,username=uname,password=password)
		if user is not None:
			if user.is_active:
				if request.POST.get("remember"):
					response=HttpResponse("<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><center><b>Your username and password will be remembered!!!<br/></br>Go back and uncheck remember me and login.")
					response.set_cookie('cid1',request.POST["uname"])
					response.set_cookie('cid2',request.POST["password"])
					return response
				p=studregister.objects.get(uname=uname)
				p.password=password
				p.save()
				return render(request,'dashboard0.html',{'u':uname})
			else:
				messages.info(request,"Invalid username/password!")
				return render(request,'login.html')
		else:
			messages.info(request,"Invalid username/password!")
			return render(request,'login.html')
	messages.info(request,"Invalid username/password!")
	return render(request,'login.html')

def main1(request):
	if request.method=='POST':
		uname=request.POST['uname']
		password=request.POST['password']
		user=authenticate(request,username=uname,password=password)
		if user is not None:
			if user.is_active:
				if request.POST.get("remember"):
					response=HttpResponse("<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><center><b>Your username and password will be remembered!!!<br/></br>Go back and uncheck remember me and login.")
					response.set_cookie('cid3',request.POST["uname"])
					response.set_cookie('cid4',request.POST["password"])
					return response
				p=register.objects.get(uname=uname)
				p.password=password
				p.save()
				return render(request,'dashboardz.html',{'u':uname})
			else:
				messages.info(request,"Invalid username/password!")
				return render(request,'login1.html')
		else:
			messages.info(request,"Invalid username/password!")
			return render(request,'login1.html')
	messages.info(request,"Invalid username/password!")
	return render(request,'login1.html')

def dashboard1(request,s):
	if request.method=='POST':
		name=request.POST['name']
		registered_number=request.POST['registered_number']
		branch=request.POST['branch']
		section=request.POST['section']
		mail=request.POST['mail']
		domain_mail=request.POST['domain_mail']
		mobile_number=request.POST['mobile_number']
		aadhar_number=request.POST['aadhar_number']
		gender=request.POST['gender'],
		dob=request.POST['dob']
		address=request.POST['address']
		city=request.POST['city']
		pincode=request.POST['pincode']
		state=request.POST['state']
		country=request.POST['country']
		detail=details(name=name,registered_number=registered_number,branch=branch,section=section,
			mail=mail,domain_mail=domain_mail,mobile_number=mobile_number,aadhar_number=aadhar_number,
			gender=gender,dob=dob,address=address,city=city,pincode=pincode,state=state,country=country)
		detail.save()
		messages.info(request,"Details uploaded successfully!")
		return render(request,'dashboard1.html',{'s':s})
	else:
		return render(request,'dashboard1.html',{'s':s})
def dashboard(request):
	d=adetails.objects.all().order_by('reg_no')
	return render(request,'dashboard.html',{'d':d})
def search(request):
	q=request.GET.get('search')
	d=adetails.objects.filter(reg_no__registered_number__contains=q)
	if d:
		return render(request,'dashboard.html',{'d':d})
	d=adetails.objects.filter(reg_no__name__contains=q)
	if d:
		return render(request,'dashboard.html',{'d':d})
	d=adetails.objects.all()
	return render(request,'dashboard.html',{'d':d})
def dashboard_1(request,r):
	s=details.objects.get(registered_number=r)
	return render(request,'dashboard_1.html',{'s':s})
def dashboard_2(request,r):
	s=adetails.objects.get(reg_no=r)
	return render(request,'dashboard_2.html',{'s':s})
def dashboard_3(request,r):
	s=Document.objects.filter(registered_no=r)
	p=details.objects.get(registered_number=r)
	return render(request,'dashboard_3.html',{'s':s,'p':p})
def dashboardz(request):
	return render(request,'dashboardz.html')
def dashboard0(request,u):
	return render(request,'dashboard0.html',{'u':u})
def dashboard2(request,s):
	data1=details.objects.all()
	if request.method=='POST':
		reg_no=request.POST['reg_no']
		tenth_score=request.POST['tenth_score']
		intermediate_score=request.POST['intermediate_score']
		btech_score=request.POST['btech_score']
		backlogs=request.POST['backlogs']
		one_one_SGPA=request.POST['one_one_SGPA']
		one_two_SGPA=request.POST['one_two_SGPA']
		two_one_SGPA=request.POST['two_one_SGPA']
		two_two_SGPA=request.POST['two_two_SGPA']
		three_one_SGPA=request.POST['three_one_SGPA']
		three_two_SGPA=request.POST['three_two_SGPA']
		four_one_SGPA=request.POST['four_one_SGPA']
		four_two_SGPA=request.POST['four_two_SGPA']
		certifications=request.POST['certifications']
		workshops=request.POST['workshops']
		mini_projects=request.POST['mini_projects']
		projects=request.POST['projects']
		job_internships=request.POST['job_internships']
		rno=details.objects.get(registered_number=reg_no)
		data=adetails(reg_no=rno,tenth_score=tenth_score,intermediate_score=intermediate_score,btech_score=btech_score,
			backlogs=backlogs,one_one_SGPA=one_one_SGPA,one_two_SGPA=one_two_SGPA,
			two_one_SGPA=two_one_SGPA,two_two_SGPA=two_two_SGPA,three_one_SGPA=three_one_SGPA,
			three_two_SGPA=three_two_SGPA,four_one_SGPA=four_one_SGPA,four_two_SGPA=four_two_SGPA,
			workshops=workshops,certifications=certifications,mini_projects=mini_projects,
			projects=projects,job_internships=job_internships)
		data.save()
		messages.success(request,"Details uploaded successfully!")
		return render(request,'dashboard2.html',{'data1':data1,'s':s})
	return render(request,'dashboard2.html',{'data1':data1,'s':s})

def dashboard3(request,s):
	data2=details.objects.all()
	if request.method=='POST':
		registered_no=request.POST['registered_no']
		document_type=request.POST['document_type']
		doc=request.FILES['doc']
		r=details.objects.get(registered_number=registered_no)
		upload=Document(registered_no=r,document_type=document_type,doc=doc)
		upload.save()
		messages.info(request,"Document uploaded successfully!")
		return render(request,'dashboard3.html',{'data2':data2,'s':s})
	return render(request,'dashboard3.html',{'data2':data2,'s':s})
def dashboard4(request,r):
	try:
		s=details.objects.get(registered_number=r)
		if s:
			return render(request,'dashboard4.html',{'s':s})
		return render(request,'default.html',{'r':r})
	except Exception:
		return render(request,'default.html',{'r':r})
def dashboard5(request,r):
	try:
		s=adetails.objects.get(reg_no=r)
		if s:
			return render(request,'dashboard5.html',{'s':s})
		return render(request,'default.html',{'r':r})
	except Exception:
		return render(request,'default.html',{'r':r})
def dashboard6(request,r):
	s=Document.objects.filter(registered_no=r)
	u=details.objects.get(registered_number=r)
	return render(request,'dashboard6.html',{'s':s,'u':u})
def edit1(request,r):
	s=details.objects.get(registered_number=r)
	return render(request,'edit1.html',{'s':s})
def edit2(request,r):
	s=adetails.objects.get(reg_no=r)
	return render(request,'edit2.html',{'s':s})
def edit3(request,r,d):
	s=Document.objects.get(registered_no=r,document_type=d)
	return render(request,'edit3.html',{'s':s})
def update1(request,r):
	s=details.objects.get(registered_number=r)
	if request.method=="POST":
		n=request.POST['name']
		reg=s.registered_number
		b=request.POST['branch']
		sec=request.POST['section']
		ma=request.POST['mail']
		d=request.POST['domain_mail']
		mobile=request.POST['mobile_number']
		aadhar=request.POST['aadhar_number']
		g=request.POST['gender'],
		dofb=request.POST['dob']
		a=request.POST['address']
		c=request.POST['city']
		p=request.POST['pincode']
		st=request.POST['state']
		cou=request.POST['country']
		s.name=n
		s.registered_number=reg
		s.branch=b
		s.section=sec
		s.mail=ma
		s.domain_mail=d
		s.mobile_number=mobile
		s.aadhar_number=aadhar
		s.gender=g
		s.dob=dofb
		s.address=a
		s.city=c
		s.pincode=p
		s.state=st
		s.country=cou
		s.save()
		return render(request,'dashboard4.html',{'s':s})
	return render(request,'edit1.html',{'s':s})
def update2(request,r):
	s=adetails.objects.get(reg_no=r)
	if request.method=="POST":
		rg=s.reg_no
		tenth=request.POST['tenth_score']
		inter=request.POST['intermediate_score']
		btech=request.POST['btech_score']
		b=request.POST['backlogs']
		one_one=request.POST['one_one_SGPA']
		one_two=request.POST['one_two_SGPA']
		two_one=request.POST['two_one_SGPA']
		two_two=request.POST['two_two_SGPA']
		three_one=request.POST['three_one_SGPA']
		three_two=request.POST['three_two_SGPA']
		four_one=request.POST['four_one_SGPA']
		four_two=request.POST['four_two_SGPA']
		c=request.POST['certifications']
		w=request.POST['workshops']
		m=request.POST['mini_projects']
		p=request.POST['projects']
		j=request.POST['job_internships']
		s.reg_no=rg
		s.tenth_score=tenth
		s.intermediate_score=inter
		s.btech_score=btech
		s.backlogs=b
		s.one_one_SGPA=one_one
		s.one_two_SGPA=one_two
		s.two_one_SGPA=two_one
		s.two_two_SGPA=two_two
		s.three_one_SGPA=three_one
		s.three_two_SGPA=three_two
		s.four_one_SGPA=four_one
		s.four_two_SGPA=four_two
		s.certifications=c	    
		s.workshops=w
		s.mini_projects=m
		s.projects=p
		s.job_internships=j
		s.save()
		return render(request,'dashboard5.html',{'s':s})
	return render(request,'edit2.html',{'s':s})
def delete(request,r,d):
    if request.method == 'POST':
        f= Document.objects.filter(registered_no=r,document_type=d)
        f.delete()
    s=Document.objects.filter(registered_no=r)
    u=details.objects.get(registered_number=r)
    return render(request,'dashboard6.html',{'s':s,'u':u})

