from django.db import models

# Create your models here.
class studregister(models.Model):
	uname=models.CharField(max_length=100)
	email=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100)
	class Meta:
		db_table="studregister"
class register(models.Model):
	uname=models.CharField(max_length=100)
	email=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100)
	class Meta:
		db_table="register"
class details(models.Model):
	name=models.CharField(max_length=100)
	registered_number=models.CharField(max_length=100,primary_key=True)
	branch=models.CharField(max_length=100)
	section=models.IntegerField()
	mail=models.CharField(max_length=100)
	domain_mail=models.CharField(max_length=100)
	mobile_number=models.CharField(max_length=100)
	aadhar_number=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	dob=models.DateField()
	address=models.TextField(max_length=400)
	city=models.CharField(max_length=100)
	pincode=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	class Meta:
		db_table="details"
class adetails(models.Model):
	reg_no=models.ForeignKey(details,on_delete=models.CASCADE)
	tenth_score=models.DecimalField(max_digits=10, decimal_places=5)
	intermediate_score=models.DecimalField(max_digits=10, decimal_places=5)
	btech_score=models.DecimalField(max_digits=10, decimal_places=5)
	backlogs=models.IntegerField()
	one_one_SGPA=models.DecimalField(max_digits=10,decimal_places=5)
	one_two_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	two_one_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	two_two_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	three_one_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	three_two_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	four_one_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	four_two_SGPA=models.DecimalField(max_digits=10, decimal_places=5)
	certifications=models.TextField(max_length=400)
	workshops=models.TextField(max_length=400)
	mini_projects=models.TextField(max_length=400)
	projects=models.TextField(max_length=400)
	job_internships=models.TextField(max_length=400)
	class Meta:
		db_table="adetails"
class Document(models.Model):
	registered_no=models.ForeignKey(details,on_delete=models.CASCADE)
	document_type=models.CharField(max_length=100)
	doc=models.FileField()
	class Meta:
		db_table="document"