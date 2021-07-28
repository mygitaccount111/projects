from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
# Create your views here.

def home(request):
	return HttpResponse("hi sravani....!")
def htmltag(r):
	return HttpResponse("<h2>good morning..!</h2>")
def usernameprint(request,uname):
	return HttpResponse("<h2>iam <span style='color:green'>{}</span></h2>".format(uname))
def usernameage(request,un,age):
	return HttpResponse("<h3 style='text-align:center;background-color:green'>hi user <span style='color:yellow'>{}</span> and your age is:<span style='color:blue'>{}</span></h3>".format(un,age))
def empdetails(request,eid,ename,eage):
	return HttpResponse("<h3>hi welcome {} and your age is: {} and your id is: {}</h3>".format(ename,eage,eid))
def htm(request):
	return render(request,'html/sample.html')
def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})
def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)
def studentdeatails(request):
	return render(request,'html/std.html')
def internaljs(request):
	return render(request,'html/internaljs.html')
def myform(req):
	if req.method == "POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get(email)
		data = {'username':uname,'rno':rollno,'emailId':email}
		return render(req,'html/display.html',data)
	return render(req,'html/myform.html')
def btregi(request):
	return render(request,'html/btregst.html')
def gform(request):
	return render(request,'html/gform.html')
def register1(request):
	#name = "sravani"
	#email = "sravs@gmail.com"
	reg = Register(name = "sravani",email = "sravs@gmail.com")
	reg.save()
	return HttpResponse("row inserted succesfully...")
def register2(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name, email = email)
		reg.save()
		return HttpResponse("Record inserted sucesfully...")
	return render(request,"html/register2.html")
def display(request):
	dat = Register.objects.all()
	return render(request,'html/display1.html',{'data' :data})


	
	
