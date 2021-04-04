from django.shortcuts import render,HttpResponse,redirect
from .models import laboratoryDetails
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        logins = laboratoryDetails.objects.filter(emailid=email)
        if logins:
            if password == logins[0].password:
                request.session['ID'] = logins[0].Labid
                ID=   request.session['ID']
                return redirect('home')
            else:
                return HttpResponse('Password Do not Match')

        else:
            return HttpResponse("wrong email id")

    return render(request,'login.html')