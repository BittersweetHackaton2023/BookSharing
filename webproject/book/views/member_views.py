from django.shortcuts import render
from models.member_models import *
from book.form import *
from django.http import HttpResponse

## email이 있는지 체크
def checkemail(email):
    try:
        member = Member.objects.get(email=email)
        return member
    except Member.DoesNotExist:
        return None


## email의 마일리지 확인
def mymileage(request):
    if request.method == 'POST':
        form = Emailform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            member = checkemail(email)
            if member:
                mileage = member.mileage
                return render(request, '.html', {'mileage': mileage})
            else:
                member = registeremail(email)
                mileage = member.mileage
                return render(request, '.html', {'mileage': mileage})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)


## 이메일 DB에 등록
def registeremail(email):
    member = Member(email = email)
    member.save()
    return member



def usemileage(request):
    if request.method == 'POST':
        form = Mileageform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mileage = form.cleaned_data['mileage']
            member = checkemail(email)
            if member:
                member.mileage -= mileage
                return render(request, '.html', {'mileage': mileage})
            else:
                member = registeremail(email)
                mileage = member.mileage
                return render(request, '.html', {'mileage': mileage})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)