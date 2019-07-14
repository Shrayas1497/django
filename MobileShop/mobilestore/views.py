from django.shortcuts import render,redirect
from.models import Mobile
from django .http import Http404
from .forms import MobileForm
def Homepage(request):
	return render(request,'cssintro.html')


def MobileList(request):
		mobiles =Mobile.objects.all()
		context ={'mobiles':mobiles}
		return render(request,'mobilelist.html',context)

def MobileDetail(request,id):
		try:
			mobiles =Mobile.objects.get(id=id)
			context ={'mobiles':mobiles}
			return render(request,'MobileDetail.html',context)

		except Mobile.DoesNotExist:
			raise Http404
			

def AddMobile(request):
	if request.user.is_superuser:
			
			

		if request.method=='POST':
			form=MobileForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return redirect('mobilestore:mobilelist')
		else:
			form=MobileForm()
		context={'form':form}
		return render(request,'AddMobile.html',context)
	else:
		raise Http404('you dont have permission')


def UpdateMobile(request,id):
	if request.user.is_superuser:
		try:
			mobileupdate= Mobile.objects.get(id=id)
		except Mobile.DoesNotExist:
			raise Http404

		if request.method=='POST':
			form=MobileForm(request.POST,request.FILES,instance=mobileupdate)
			if form.is_valid():
				form.save()
				return redirect('mobilestore:mobilelist')
		else:
			form=MobileForm(instance=mobileupdate)
		context={'form':form}
		return render(request,'AddMobile.html',context,)
	else:
		raise Http404('you dont have permission')

def DeleteMobile(request,id):
	try:
		mobiledelete =Mobile.objects.get(id=id)
	except Mobile.DoesNotExist:
		raise Http404
	mobiledelete.delete()
	return redirect('mobilestore:mobilelist')