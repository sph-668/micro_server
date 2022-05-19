from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import EntryForm
from .forms import FinalForm
from django.utils import timezone
from transliterate import translit
from django.contrib.auth.models import User
from .models import Saved_labs
from .models import Presaved_labs
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import SignUpForm


@csrf_exempt
def signup(request):
    form = SignUpForm(request.POST)
    myjson = json.loads(request.body.decode('utf-8'))
    user = User.objects.create_user(username=my_json['username'], password=my_json['password'])
    user.last_name = my_json['group']
    user.save()
    user = authenticate(username=my_json['username'], password=my_json['password'])
    login(request, user)
    return JsonResponse({'status': 'ok`'})



@csrf_exempt
def signin(request):
    form = SignInForm(request.POST)
    my_json = json.loads(request.body.decode('utf-8'))
    user = authenticate(username=my_json['username'], password=my_json['password'])
    login(request, user)
    return JsonResponse({'status': 'ok`'})



@csrf_exempt
def presave(request):
    form = EntryForm(request.POST)
    usrtxt = json.loads(request.body.decode('utf-8'))
    if Presaved_labs.objects.filter(author=request.user.username, number=usrtxt['number']).exists():
        lab_to_presave = Presaved_labs.objects.filter(author=request.user.username, number=usrtxt['number'])[0]
        lab_to_presave.delete()
    author_ = request.user.username
    created_date_ = timezone.now()
    group_ = request.user.last_name
    post = Presaved_labs(author=author_, created_date=created_date_, number=usrtxt['number'],
                         group=group_, brightness=usrtxt['brightness'], contrast=usrtxt['contrast'],
                         roughFocus=usrtxt['roughFocus'], preciseFocus=usrtxt['preciseFocus'],
                         workDistance=usrtxt['workDistance'], apertureSize=usrtxt['apertureSize'],
                         beamCurrent=usrtxt['beamCurrent'], scale=usrtxt['scale'],
                         voltage=usrtxt['voltage'])
    post.save()

    return JsonResponse({'status': 'ok`'})


@csrf_exempt
def load(request):
    my_json = json.loads(request.body.decode('utf-8'))
    lab = Presaved_labs.objects.filter(id=my_json['id'])[0]
    return JsonResponse({ 'brightness': lab.brightness, 'contrast': lab.contrast, 'roughFocus': lab.roughFocus,
                          'preciseFocus': lab.preciseFocus, 'workDistance': lab.workDistance, 'apertureSize': lab.apertureSize,
                          'beamCurrent': lab.beamCurrent, 'scale': lab.scale, 'voltage': lab.voltage } )







@csrf_exempt
def create_lab(request):
    form = EntryForm(request.POST)
    my_json = json.loads(request.body.decode('utf-8'))

    author_ = request.user.username
    created_date_ = timezone.now()
    group_ = request.user.last_name
    post = Presaved_labs(author=author_, created_date=created_date_, number=my_json['number'],
                         group=group_, brightness=0, contrast=0,
                         roughFocus=0, preciseFocus=0,
                         workDistance=3, apertureSize=1,
                         beamCurrent=0, scale=1,
                         voltage=0)
    post.save()

    my_id = Presaved_labs.objects.filter(author=request.user.username, number=my_json['number'], group=request.user.last_name)[0].id
    return JsonResponse({'id': my_id})






@csrf_exempt
def getusername(request):
    if request.user.is_authenticated == True:
        user = request.user.username
        return JsonResponse({'username': user})
    else:
        return JsonResponse({'username': None})


def lk_student_active(request):
    l1 = len(Saved_labs.objects.filter(author=request.user.username, number=1))
    l2 = len(Saved_labs.objects.filter(author=request.user.username, number=2))
    l3 = len(Saved_labs.objects.filter(author=request.user.username, number=3))
    l4 = len(Saved_labs.objects.filter(author=request.user.username, number=4))
    l5 = len(Saved_labs.objects.filter(author=request.user.username, number=5))

    print(l1, l2, l3, l4, l5)


    return render(request, 'app/lk_student_active.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'l5': l5})



def lk_student_sent(request):
    l1 = len(Saved_labs.objects.filter(author=request.user.username, number=1))
    l2 = len(Saved_labs.objects.filter(author=request.user.username, number=2))
    l3 = len(Saved_labs.objects.filter(author=request.user.username, number=3))
    l4 = len(Saved_labs.objects.filter(author=request.user.username, number=4))
    l5 = len(Saved_labs.objects.filter(author=request.user.username, number=5))
    sc1, sc2, sc3, sc4, sc5 = 0, 0, 0, 0, 0
    if l1:
        sc1 = Saved_labs.objects.filter(author=request.user.username, number=1)[0].score
    if l2:
        sc2 = Saved_labs.objects.filter(author=request.user.username, number=2)[0].score
    if l3:
        sc3 = Saved_labs.objects.filter(author=request.user.username, number=3)[0].score
    if l4:
        sc4 = Saved_labs.objects.filter(author=request.user.username, number=4)[0].score
    if l5:
        sc5 = Saved_labs.objects.filter(author=request.user.username, number=5)[0].score




    print(l1, l2, l3, l4, l5)


    return render(request, 'app/lk_student_sent.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'l5': l5,
                                                        'sc1': sc1, 'sc2': sc2, 'sc3': sc3, 'sc4': sc4, 'sc5': sc5})




@csrf_exempt
def presave(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            usrtxt = json.loads(request.body.decode('utf-8'))
            if Presaved_labs.objects.filter(author=request.user.username, number=usrtxt['number']).exists():
                lab_to_presave = Presaved_labs.objects.filter(author=request.user.username, number=usrtxt['number'])[0]
                lab_to_presave.delete()
            author_ = request.user.username
            created_date_ = timezone.now()
            group_ = request.user.last_name
            post = Presaved_labs(author=author_, created_date=created_date_, number=usrtxt['number'],
                                  group=group_, brightness=usrtxt['brightness'], contrast=usrtxt['contrast'],
                                  roughFocus=usrtxt['roughFocus'], preciseFocus=usrtxt['preciseFocus'],
                                  workDistance=usrtxt['workDistance'], apertureSize=usrtxt['apertureSize'],
                                  beamCurrent=usrtxt['beamCurrent'], scale=usrtxt['scale'],
                                  voltage=usrtxt['voltage'])
            post.save()
    else:
        form = EntryForm
    return render(request, 'app/nothing.html', {'form': form})

@csrf_exempt
def getusername(request):
    if request.method == 'GET':
        if request.user.is_authenticated == True:
            user = request.user.username
            #print("ok")
            #usrtxt = json.loads(request.body.decode('utf-8'))
            #print(json_string)
            #print(usrtxt['text'])
            return JsonResponse({'username': user})
        else:
            return JsonResponse({'username': None})
    return HttpResponse("ok")

def save(request, num):
    # сменить время создания
    message = ''
    if request.method == "POST":
        if Presaved_labs.objects.filter(author = request.user.username, number = num).exists():
            lab_to_save = Presaved_labs.objects.filter(author = request.user.username, number = num)[0]
            lab_to_save.delete()
            #print(lab_to_save)
            form = FinalForm(request.POST)
            number_ = num
            author_ = lab_to_save.author
            group_ = lab_to_save.group
            created_date_ = lab_to_save.created_date
            brightness_ = lab_to_save.brightness
            contrast_ = lab_to_save.contrast
            roughFocus_ = lab_to_save.roughFocus
            preciseFocus_ = lab_to_save.preciseFocus
            voltage_ = lab_to_save.voltage
            apertureSize_ = lab_to_save.apertureSize
            workDistance_ = lab_to_save.workDistance
            beamCurrent_ = lab_to_save.beamCurrent
            scale_ = lab_to_save.scale
            post = Saved_labs(author=author_, created_date=created_date_, number=number_,
                                  group=group_, brightness=brightness_, contrast=contrast_,
                                  roughFocus=roughFocus_, preciseFocus=preciseFocus_,
                                  workDistance=workDistance_, apertureSize=apertureSize_,
                                  beamCurrent=beamCurrent_, scale=scale_,
                                  voltage=voltage_)
            post.save()
            message = 'Отправлено'
        else:
            message = 'Нет данных для отправки'
            #print("no labs")
    return redirect('lk_student_active')

def save_1(request):
    save(request, 1)
    return redirect('lk_student_active')

def save_2(request):
    save(request, 2)
    return redirect('lk_student_active')

def save_3(request):
    save(request, 3)
    return redirect('lk_student_active')

def save_4(request):
    save(request, 4)
    return redirect('lk_student_active')

def save_5(request):
    save(request, 5)
    return redirect('lk_student_active')
