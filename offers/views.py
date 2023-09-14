from django.shortcuts import render


# English
def trips(request):
    return render(request, 'en/trips.html')


def other(request):
    return render(request, 'en/other.html')


def pickup(request):
    return render(request, 'en/pickup.html')


def city(request):
    return render(request, 'en/trips/town.html')


def safari(request):
    return render(request, 'en/trips/safari.html')


def kawasan(request):
    return render(request, 'en/trips/kawasan.html')


def hopping(request):
    return render(request, 'en/trips/hopping.html')


# Arabic
def trips_ar(request):
    return render(request, 'ar/trips.html')


def other_ar(request):
    return render(request, 'ar/other.html')


def pickup_ar(request):
    return render(request, 'ar/pickup.html')


def city_ar(request):
    return render(request, 'ar/trips/town.html')


def safari_ar(request):
    return render(request, 'ar/trips/safari.html')


def kawasan_ar(request):
    return render(request, 'ar/trips/kawasan.html')


def hopping_ar(request):
    return render(request, 'ar/trips/hopping.html')


# Russian
def trips_ru(request):
    return render(request, 'ru/trips.html')


def other_ru(request):
    return render(request, 'ru/other.html')


def pickup_ru(request):
    return render(request, 'ru/pickup.html')


def city_ru(request):
    return render(request, 'ru/trips/town.html')


def safari_ru(request):
    return render(request, 'ru/trips/safari.html')


def kawasan_ru(request):
    return render(request, 'ru/trips/kawasan.html')


def hopping_ru(request):
    return render(request, 'ru/trips/hopping.html')
