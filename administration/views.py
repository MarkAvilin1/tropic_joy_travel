from joy.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render


# English
def index(request):
    return render(request, 'en/index.html')


def contact(request):
    success_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name', 'NO')
        message = request.POST.get('message', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        msg = f"""
        ==========================================
                    Full Name||     {name}
        ==========================================                    
                    Email||          {email}
        ==========================================                    
                    Phone||          {phone}
        ==========================================                    
                    Message||        {message}
            """
        send_mail('General Contact', msg, email, (EMAIL_HOST_USER,))
        success_msg = "Your message hes been sent successfully, we'll reply you shortly!"
    context = {
        'success_msg': success_msg
    }
    return render(request, 'en/contact.html', context)


# Arabic
def index_ar(request):
    return render(request, 'ar/index.html')


def contact_ar(request):
    success_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name', 'NO')
        message = request.POST.get('message', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        msg = f"""
        ==========================================
                    Full Name||     {name}
        ==========================================                    
                    Email||          {email}
        ==========================================                    
                    Phone||          {phone}
        ==========================================                    
                    Message||        {message}
            """
        send_mail('من تواصل', msg, email, (EMAIL_HOST_USER,))
        success_msg = "تم إرسال رسالتكم بنجاح , سيتم الرد عليكم قريبا!"
    context = {
        'success_msg': success_msg
    }
    return render(request, 'ar/contact.html', context)


# Russian
def index_ru(request):
    return render(request, 'ru/index.html')


def contact_ru(request):
    success_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name', 'NO')
        message = request.POST.get('message', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        msg = f"""
        ==========================================
                    Full Name||     {name}
        ==========================================                    
                    Email||          {email}
        ==========================================                    
                    Phone||          {phone}
        ==========================================                    
                    Message||        {message}
            """
        send_mail('Контакты', msg, email, (EMAIL_HOST_USER,))
        success_msg = "Спасибо за интерес, Ваше сообщение было доставлено, ожидайте ответа в ближайшее время!"
    context = {
        'success_msg': success_msg
    }
    return render(request, 'ru/contact.html', context)
