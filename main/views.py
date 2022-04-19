
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Short, Visit
from .forms import ShortForm
import string
import random
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
import qrcode
import qrcode.image.svg
from io import BytesIO


def qr_generator(qr_text):
    context = {}
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(qr_text,
                      image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)
    qr_code = stream.getvalue().decode()
    return qr_code


def short_url_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def analysis(request):
    user = request.user
    site = get_current_site(request)
    if user.is_authenticated:
        shorts = Short.objects.filter(user=request.user)
    else:
        shorts = Short.objects.all()
    return render(request, 'analysis.html', {'shorts': shorts, 'site': site})


def get_visits(request):
    short = request.POST['short']
    visits = Visit.objects.filter(short=short)
    return render(request, 'visits.html', {'shorts': visits})


def index(request):
    form = ShortForm()
    return render(request, 'index.html', {'form': form})


def shorten(request):
    if request.method == 'POST':
        try:
            form = ShortForm(request.POST)
            site = get_current_site(request)
            if (site == 'shorty.heartmantalent.com'):
                messages.add_message(
                    request, messages.INFO, "Already short")
                return redirect('index')
            long_url = request.POST['long_url']
            user = request.user
            short_url = short_url_generator()
            if user.is_authenticated:
                short = Short(long_url=long_url,
                              short_url=short_url, user=user)
            else:
                short = Short(long_url=long_url,
                              short_url=short_url)

            short.save()
            qr_code = qr_generator(str(site)+short_url)
            return render(request, 'index.html', {'form': form,
                                                  'short_url': short_url,
                                                  'long_url': long_url,
                                                  'site': str(site),
                                                  'qr_code': qr_code})
        except IntegrityError:
            messages.add_message(request, messages.ERROR, "URL already exists")
            return render(request, 'index.html', {'form': form})
    else:
        messages.add_message(request, messages.INFO, "Wrong method")
        return redirect('index')


def lengthen(request, slug):
    if request.method == 'GET':
        try:
            short = Short.objects.get(short_url=slug)
            long_url = short.long_url
            # browser = request.META('HTTP_USER_AGENT', 'Default')
            # referrer = request.META.get('HTTP_REFERER', 'Referrer')
            # country = request.geolocation
            # print(country)
            visit = Visit(short=short)
            visit.save()
            return redirect(long_url)
        except Short.DoesNotExist:
            messages.add_message(request, messages.ERROR, "URL does not exist")
            return redirect('index')
    else:
        messages.add_message(request, messages.INFO, "Wrong method")
        return redirect('index')


def delete(request, id):
    if request.method == 'GET':
        try:
            short = Short.objects.get(id=id)
            short.delete()
            messages.add_message(request, messages.SUCCESS, "URL Deleted")
            return redirect('analysis')
        except Short.DoesNotExist:
            messages.add_message(request, messages.ERROR, "URL does not exist")
            return redirect('analysis')
    else:
        messages.add_message(request, messages.INFO, "Wrong method")
        return redirect('analysis')


def login(request):
    return render(request, 'login.html')
