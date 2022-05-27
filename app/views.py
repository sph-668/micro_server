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
import secrets
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm

tok_to_us = dict()
us_to_tok = dict()


def get_user_id(my_json):
    pass



def is_teacher(user_id):
    return User.objects.filter(id=user_id)[0].is_staff


def is_logged(my_json):
    print(my_json.keys())
    if 'token' in my_json.keys():
        if my_json['token'] in tok_to_us.keys():
            return 1
    return 0


def validation_of_work(token, id_):
    if tok_to_us.get(token) == Presaved_labs.objects.filter(id=id_)[0].user_id:
        return 1
    else:
        return 0



def initial(request):
    return JsonResponse({'status': 'ok'})


@csrf_exempt
def signin(request):  #  ИМЯ, ПАРОЛЬ, ГРУППА
    my_json = json.loads(request.body.decode('utf-8'))
    if User.objects.filter(username=my_json['username'], last_name=my_json['group']).exists():
        user = User.objects.filter(username=my_json['username'], last_name=my_json['group'])[0]
        if (check_password(my_json['password'], user.password)):
            user_id = user.id
            print(user_id)

            if user_id in us_to_tok.keys():
                tok = us_to_tok.get(user_id)
                us_to_tok.pop(user_id)
                tok_to_us.pop(tok)
            my_token = secrets.token_hex(40)

            new_id = {user_id: my_token}
            new_token = {my_token: user_id}
            us_to_tok.update(new_id)
            tok_to_us.update(new_token)


            return JsonResponse({'token': my_token, 'status': 'ok', 'isTeacher': is_teacher(user_id)})

        else:
            return JsonResponse({'status': 'fail'})
        print(tok_to_us)

    else:
        return JsonResponse({'status': 'fail'})



@csrf_exempt
def signup(request):  # ИМЯ, ПАРОЛЬ, ГРУППА
    my_json = json.loads(request.body.decode('utf-8'))
    print(User.objects.filter(username=my_json['username'], last_name=my_json['group']))
    if User.objects.filter(username=my_json['username'], last_name=my_json['group']).exists():
        return JsonResponse({'status': 'fail'})
    else:
        user = User.objects.create_user(username=my_json['username'], password=my_json['password'],
                                        last_name=my_json['group'])
        user.save()  # здесь просто сохраняем Userа
        return JsonResponse({'status': 'ok'})


@csrf_exempt
def getusername(request):
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})
    user_id = tok_to_us.get(my_json['token'])
    username = User.objects.filter(id=user_id)[0].username
    return JsonResponse({'username': username})


@csrf_exempt
def getpresavedlabs(request):
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})
    my_token = my_json['token']
    user_id_ = tok_to_us.get(my_token)
    my_labs = Presaved_labs.objects.filter(user_id=user_id_)
    all_labs = Lab_description.objects.all()
    numbers_of_lab = []
    for i in all_labs:
        numbers_of_lab.append(i.number)
    numbers_of_my_labs = []
    for i in my_labs:
        numbers_of_my_labs.append(i.number)

    numbers_of_lab.sort()
    answer = []
    for i in numbers_of_lab:
        my = dict()
        if i in numbers_of_my_labs:
            lab = Presaved_labs.objects.filter(user_id=user_id_, number=i)[0]
            my['id'] = lab.id
        else:
            my['id'] = -1
        my['number'] = i
        lab_description = Lab_description.objects.filter(number=i)[0]
        my['title'] = lab_description.title
        my['body'] = lab_description.task
        my['deadline'] = lab_description.deadline
        answer.append(my)
    return JsonResponse(answer, safe=False)



@csrf_exempt
def getsavedlabs(request):  # ТОЛЬКО ТОКЕН
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})
    my_token = my_json['token']
    user_id_ = tok_to_us.get(my_token)
    my_labs = Saved_labs.objects.filter(user_id=user_id_)
    all_labs = Lab_description.objects.all()
    numbers_of_lab = []
    for i in all_labs:
        numbers_of_lab.append(i.number)
    numbers_of_my_labs = []
    for i in my_labs:
        numbers_of_my_labs.append(i.number)

    numbers_of_lab.sort()
    answer = []
    for i in numbers_of_lab:

        if i in numbers_of_my_labs:
            labs = Saved_labs.objects.filter(user_id=user_id_, number=i)
            for j in labs:
                my = dict()
                my['number'] = i
                my['created_date'] = j.created_date
                my['score'] = j.score
                lab_description = Lab_description.objects.filter(number=i)[0]
                my['title'] = lab_description.title
                answer.append(my)
        else:
            continue

    return JsonResponse(answer, safe=False)




@csrf_exempt
def check_dict(request):
    print(tok_to_us)
    print(us_to_tok)
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def createlab(request):
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})

    user_id_ = tok_to_us.get(my_json['token'])

    #print(len(Presaved_labs.objects.filter(user_id=user_id_, number=my_json['number'])))
    #print(Presaved_labs.objects.filter(user_id=user_id_, number=my_json['number']))
    if len(Presaved_labs.objects.filter(user_id=user_id_, number=my_json['number'])) > 0:  # если существует уже лаба
        return JsonResponse({'status': 'failed'})
    created_date_ = timezone.now()
    post = Presaved_labs(user_id=user_id_, created_date=created_date_, number=my_json['number'], brightness=0,
                         contrast=0,
                         roughFocus=0, preciseFocus=0,
                         workDistance=3, apertureSize=1,
                         beamCurrent=0, scale=1,
                         voltage=0)
    post.save()

    my_id = Presaved_labs.objects.filter(user_id=user_id_, number=my_json['number'])[0].id
    return JsonResponse({'id': my_id, 'status': 'ok'})



@csrf_exempt
def presave(request):  #  ВСЕ ПАРАМЕТРЫ, ID ЛАБЫ,
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})
    lab_to_presave = Presaved_labs.objects.filter(id=my_json['id'])[0]
    lab_to_presave.brightness = my_json['brightness']
    lab_to_presave.contrast = my_json['contrast']
    lab_to_presave.roughFocus = my_json['roughFocus']
    lab_to_presave.preciseFocus = my_json['preciseFocus']
    lab_to_presave.workDistance = my_json['workDistance']
    lab_to_presave.apertureSize = my_json['apertureSize']
    lab_to_presave.beamCurrent = my_json['beamCurrent']
    lab_to_presave.scale = my_json['scale']
    lab_to_presave.voltage = my_json['voltage']

    print(lab_to_presave)
    print(lab_to_presave.brightness)

    lab_to_presave.save()

    return JsonResponse({'status': 'ok'})


@csrf_exempt
def load(request):  # ТОКЕН, ID ЛАБЫ
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})
    if validation_of_work(my_json['token'], my_json['id']):
        lab = Presaved_labs.objects.filter(id=my_json['id'])[0]
        return JsonResponse({'brightness': lab.brightness, 'contrast': lab.contrast, 'roughFocus': lab.roughFocus,
                             'preciseFocus': lab.preciseFocus, 'workDistance': lab.workDistance,
                             'apertureSize': lab.apertureSize,
                             'beamCurrent': lab.beamCurrent, 'scale': lab.scale, 'voltage': lab.voltage,
                             'status': 'ok'})
    else:
        return JsonResponse({'status': 'fail'})


@csrf_exempt
def loadteacher(request):  # ТОКЕН, ID ЛАБЫ
    my_json = json.loads(request.body.decode('utf-8'))
    user_id_ = tok_to_us.get(my_json['token'])
    if not is_teacher(user_id_):
        return JsonResponse({'status': 'authorization error'})
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})

    lab = Saved_labs.objects.filter(id=my_json['id'])[0]
    return JsonResponse({'brightness': lab.brightness, 'contrast': lab.contrast, 'roughFocus': lab.roughFocus,
                         'preciseFocus': lab.preciseFocus, 'workDistance': lab.workDistance,
                         'apertureSize': lab.apertureSize,
                         'beamCurrent': lab.beamCurrent, 'scale': lab.scale, 'voltage': lab.voltage,
                         'status': 'ok'})





@csrf_exempt
def save(request):
    my_json = json.loads(request.body.decode('utf-8'))
    if not is_logged(my_json):
        return JsonResponse({'status': 'authorization error'})
    id_lab = my_json['id']
    user_id_ = tok_to_us.get(my_json['token'])

    if Presaved_labs.objects.filter(id = id_lab).exists():
        lab_to_save = Presaved_labs.objects.filter(id = id_lab)[0]
        print(lab_to_save)
        lab_to_save.delete()
        created_date_ = timezone.now()

        post = Saved_labs(user_id=user_id_, created_date=created_date_, number=lab_to_save.number,
                          brightness=lab_to_save.brightness, contrast=lab_to_save.contrast,
                              roughFocus=lab_to_save.roughFocus, preciseFocus=lab_to_save.preciseFocus,
                              workDistance=lab_to_save.workDistance, apertureSize=lab_to_save.apertureSize,
                              beamCurrent=lab_to_save.beamCurrent, scale=lab_to_save.scale,
                              voltage=lab_to_save.voltage)
        post.save()
    else:
        return JsonResponse({'status': 'fail'})
    return JsonResponse({'status': 'ok'})


@csrf_exempt
def getnumberedlabtocheck(request):
    my_json = json.loads(request.body.decode('utf-8'))
    user_id_ = tok_to_us.get(my_json['token'])
    if not is_teacher(user_id_):
        return JsonResponse({'status': 'authorization error'})

    labs = Saved_labs.objects.filter(number=my_json['number'], score=0)
    answer = []
    for lab in labs:
        my_dict = {'brightness': lab.brightness, 'contrast': lab.contrast, 'roughFocus': lab.roughFocus,
         'preciseFocus': lab.preciseFocus, 'workDistance': lab.workDistance,
         'apertureSize': lab.apertureSize,
         'beamCurrent': lab.beamCurrent, 'scale': lab.scale, 'voltage': lab.voltage,
         'status': 'ok'}
        user_id = lab.user_id
        student = User.objects.filter(id=user_id)[0]
        my_dict['student'] = student.username
        my_dict['group'] = student.last_name
        my_dict['id'] = lab.id
        my_dict['created_date'] = lab.created_date
        answer.append(my_dict)
    return JsonResponse(answer, safe=False)


@csrf_exempt
def getcheckednumberedlab(request):
    my_json = json.loads(request.body.decode('utf-8'))
    user_id_ = tok_to_us.get(my_json['token'])
    if not is_teacher(user_id_):
        return JsonResponse({'status': 'authorization error'})

    q = Saved_labs.objects.exclude(score=0)
    labs = q.filter(number=my_json['number'])
    answer = []
    for lab in labs:
        my_dict = {'brightness': lab.brightness, 'contrast': lab.contrast, 'roughFocus': lab.roughFocus,
         'preciseFocus': lab.preciseFocus, 'workDistance': lab.workDistance,
         'apertureSize': lab.apertureSize,
         'beamCurrent': lab.beamCurrent, 'scale': lab.scale, 'voltage': lab.voltage,
         'status': 'ok'}
        user_id = lab.user_id
        student = User.objects.filter(id=user_id)[0]
        my_dict['student'] = student.username
        my_dict['group'] = student.last_name
        my_dict['id'] = lab.id
        my_dict['created_date'] = lab.created_date
        answer.append(my_dict)
    return JsonResponse(answer, safe=False)






@csrf_exempt
def getlabtocheck(request):  # ТОКЕН
    my_json = json.loads(request.body.decode('utf-8'))
    user_id_ = tok_to_us.get(my_json['token'])
    if not is_teacher(user_id_):
        return JsonResponse({'status': 'authorization error'})

    answer = labtocheck(0)

    return JsonResponse(answer, safe=False)


@csrf_exempt
def getcheckedlab(request):  # ТОКЕН
    my_json = json.loads(request.body.decode('utf-8'))
    user_id_ = tok_to_us.get(my_json['token'])
    if not is_teacher(user_id_):
        return JsonResponse({'status': 'authorization error'})

    answer = labtocheck(1)

    return JsonResponse(answer, safe=False)



def labtocheck(sc):
    if sc == 0:
        labs = Saved_labs.objects.filter(score=0)
    else:
        labs = Saved_labs.objects.exclude(score=0)
    all_labs = Lab_description.objects.all()
    numbers_of_lab = []
    for i in all_labs:
        numbers_of_lab.append(i.number)
    answer = []
    for i in numbers_of_lab:
        my = dict()
        my['number'] = i
        lab_description = Lab_description.objects.filter(number=i)[0]
        my['title'] = lab_description.title
        my['body'] = lab_description.task
        my['deadline'] = lab_description.deadline
        if sc == 0:
            my['count'] = len(Saved_labs.objects.filter(score=0, number=i))
        else:
            q = Saved_labs.objects.exclude(score=0)
            print(q)
            my['count'] = len(q.filter(number=i))
            #print(q.filter(number=i))
        answer.append(my)
    return answer






@csrf_exempt
def setscore(request):
    my_json = json.loads(request.body.decode('utf-8'))
    print(is_logged(my_json))
    id_lab = my_json['id']
    score = my_json['score']
    lab = Saved_labs.objects.filter(id=id_lab)[0]
    lab.score = score
    lab.save()
    return JsonResponse({'status': 'ok'})


