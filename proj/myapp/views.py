from django.shortcuts import render,redirect


from myapp.models import *

# Create your views here.
def home(request):
    data=None
    if request.method=="POST":
        n1=request.POST.get("name")
        n2=request.POST.get("address")
        im=request.FILES["imgfile"]
        data={
            "name":n1,
            "address":n2
        }
        info=Person()
        info.name=n1
        info.address=n2
        info.profileIm=im
        info.save()
    return render(request,"index.html",data)

def view_data(request):
    vi=Person.objects.all()
    return render(request,"view.html",{"view":vi})

def delt(request,id):
    de=Person.objects.get(id=id)
    de.delete()

    return redirect("v")