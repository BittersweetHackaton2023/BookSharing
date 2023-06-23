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
                return render(request, '.html', {'message': '해당 이메일이 없습니다.'})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)


## 이메일 DB에 등록
def registeremail(request):
    if request.method == 'POST':
        form = Emailform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            member = checkemail(email)
            if member:
                return render(request, 'signup.html', {'message': '이미 가입된 메일입니다.'})
            else:
                member = Member(email = email)
                member.save()
                return render(request, 'signup.html', {'message': '가입 되었습니다.'})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)



## 신청 때 마일리지 차감
def usemileage(request):
    if request.method == 'POST':
        form = Mileageform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mileage = form.cleaned_data['mileage']
            member = checkemail(email)
            if member:
                if member.mileage < mileage:
                    return render(request, '.html', {'message': '마일리지가 부족합니다.'})
                member.mileage -= mileage
                return render(request, '.html', {'mileage': mileage})
            else:
                return render(request, '.html', {'message': '해당 이메일이 없습니다.'})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)


## 물려받기 신청
def order(request):
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            email = form.cleaned_data['email']
            mileage = form.cleaned_data['mileage']
            member = checkemail(email)
            if member:
                member.mileage -= mileage
                return render(request, '.html', {'mileage': mileage})
            else:
                return render(request, '.html', {'message': '해당 이메일이 없습니다.'})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)