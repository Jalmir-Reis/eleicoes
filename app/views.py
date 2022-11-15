from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import News, Timer, Typed, Music, Images, Default, Home
from .forms import NewsForm, ImagesForm
from django.core.files.storage import FileSystemStorage


# FRONTEND
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def frontend(request):
    timer = Timer.objects.all()
    typed = Typed.objects.all()
    music = Music.objects.all()
    slide = Images.objects.all()
    default = Default.objects.all()
    home = Home.objects.all()
    context = {
        'timer':timer,
        'typed':typed,
        'music':music,
        'slide':slide,
        'default':default,
        'home':home
    }
    return render(request, 'frontend.html', context)

def newsletter(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        email = request.POST['email']
        if News.objects.filter(email=email).exists():
            messages.error(request, 'Esse email já está cadastrado !')
            return HttpResponseRedirect('/')
        elif form.is_valid():
            form.save()
            messages.success(request, 'Notificações ativadas')
            return HttpResponseRedirect('/')
    else:
        form = NewsForm()
        return render(request, 'frontend.html', {'form':form})


# BACKEND
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    news = News.objects.all().order_by('-create_at')
    total = News.objects.all().count()
    timer = Timer.objects.all()
    typed = Typed.objects.all()
    music = Music.objects.all()
    slide = Images.objects.all()
    home = Home.objects.all()
    context = {
        'news':news,
        'total':total,
        'timer':timer,
        'typed':typed,
        'music':music,
        'slide':slide,
        'home':home
    }
    return render(request, 'backend.html', context)

# Edit Timer
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_timer(request):
    if request.method == 'POST':
        timer = Timer.objects.get(id = request.POST.get('id'))
        if timer != None:
            timer.timer = request.POST.get('timer')
            timer.save()
            messages.success(request, 'Editado com sucesso')
            return HttpResponseRedirect('/backend')


# Edit Typed
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_typed(request):
    if request.method == 'POST':
        typed = Typed.objects.get(id = request.POST.get('id'))
        if typed != None:

            typed.fixo = request.POST.get('fixo')
            typed.txt_01 = request.POST.get('txt_01')
            typed.txt_02 = request.POST.get('txt_02')
            typed.txt_03 = request.POST.get('txt_03')
            typed.txt_04 = request.POST.get('txt_04')

            typed.save()
            messages.success(request, 'Editado com sucesso')
            return HttpResponseRedirect('/backend')


# Edit Music
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_music(request):
    if request.method == 'POST':
        song = Music.objects.get(id= request.POST.get('id'))
        song.title_music = request.POST.get('title_music')
        if request.FILES.get('music') != None:
            file = request.FILES['music']
            st = FileSystemStorage()
            x = st.save(file.name, file)
        else: x = None
        if x != None: song.music = x
        song.save()
        messages.success(request, 'Editado com sucesso !')
        return HttpResponseRedirect('/backend')


# ADD Images (Usar apenas para manutenção)
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Adicionado com sucesso !')
            return HttpResponseRedirect('/backend')
        else:
            return render(request, 'add_img.html', {'form':form})
    else:
        form = ImagesForm()
        return render(request, 'add_img.html', {'form':form})

# EDIT Images
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update(request, id):
    s = Images.objects.get(pk=id)
    d = Default.objects.all()
    form = ImagesForm(request.POST or None, request.FILES or None, instance=s)
    if form.is_valid():
        s = form.save()
        s.save()
        messages.success(request, 'Editado com sucesso !')
        return HttpResponseRedirect('/backend')
    context = {
        's':s,
        'd':d,
        'form':form
    }
    return render(request, 'edit_img.html', context)


# EDIT Homepage
@ login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_home(request):
    if request.method == 'POST':
        home = Home.objects.get(id = request.POST.get('id'))
        if home != None:
            # Titulo
            home.home_title = request.POST.get('home_title')
            home.icon_title = request.POST.get('icon_title')
            home.horario = request.POST.get('horario')
            # Card 01 Verde
            home.card_title01 = request.POST.get('card_title01')
            home.card_color01 = request.POST.get('card_color01')
            home.card_icon01 = request.POST.get('card_icon01')
            home.txt_card_a1 = request.POST.get('txt_card_a1')
            home.txt_card_b1 = request.POST.get('txt_card_b1')
            home.txt_card_c1 = request.POST.get('txt_card_c1')
            # Card 02 Vermelho
            home.card_title02 = request.POST.get('card_title02')
            home.card_color02 = request.POST.get('card_color02')
            home.card_icon02 = request.POST.get('card_icon02')
            home.txt_card_a2 = request.POST.get('txt_card_a2')
            home.txt_card_b2 = request.POST.get('txt_card_b2')
            home.txt_card_c2 = request.POST.get('txt_card_c2')

            home.btn_color = request.POST.get('btn_color')
            home.icon_type = request.POST.get('icon_type')

            # Modal
            home.modal_title = request.POST.get('modal_title')
            home.modal_card_title = request.POST.get('modal_card_title')
            home.modal_card_color = request.POST.get('modal_card_color')
            home.modal_card_icon = request.POST.get('modal_card_icon')
            home.cargo01 = request.POST.get('cargo01')
            home.cargo02 = request.POST.get('cargo02')
            home.cargo03 = request.POST.get('cargo03')
            home.cargo04 = request.POST.get('cargo04')
            home.cargo05 = request.POST.get('cargo05')

            # Save all
            home.save()
            messages.success(request, 'Editado com sucesso !')
            return HttpResponseRedirect('/backend')

