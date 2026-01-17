# from django.shortcuts import render
# from django.core.mail import send_mass_mail
# from django.http import HttpResponse

# # Create your views here.
# def send_bulk_email(request):
#     message1 = ('Welcome to user 1','Hello user 1,Welcome to our platform.','devshigvan28@gmail.com',['vanshi.trycatch@gmail.com'])
#     message2 = ('Welcome to user 2','Hello user 2,Welcome to our platform.','devshigvan28@gmail.com',['devesh.trycatch@gmail.com'])
#     message3 = ('Welcome to user 3','Hello user 3,Welcome to our platform.','devshigvan28@gmail.com',['devesh.trycatch1@gmail.com'])

#     send_mass_mail((message1,message2,message3),fail_silently=False)
#     return HttpResponse('Bulk emails sent successfully!')
    


# from django.core.mail import EmailMultiAlternatives
# from django.http import HttpResponse
# from django.template.loader import render_to_string


# def send_bulk_email(request):
#     subject = 'Welcome to our Blog'
#     from_email = 'devshigvan28@gmail.com'
#     recipient_list = ['devesh.trycatch@gmail.com','vanshi.trycatch@gmail.com']

#     html_content = render_to_string('welcome_email.html',{'username':'Dev'})
    
#     msg = EmailMultiAlternatives(subject,'Welcome to my platform',from_email,recipient_list)
#     msg.attach_alternative(html_content,"text/html")

#     msg.send()

#     return HttpResponse('Bulk email sent successfully!!!')



# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.conf import settings
# from .forms import RegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)

#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )

#             # Send registration email
#             subject = 'Welcome to Our Website'
#             text_content = 'Thank you for Registering.'
#             html_content = f"""
#                 <h2>Welcome {user.username}!</h2>
#                 <p>Your account has been created successfully.</p>
#             """

#             email = EmailMultiAlternatives(
#                 subject,
#                 text_content,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [user.email]
#             )
#             email.attach_alternative(html_content, "text/html")
#             email.send()

#             return redirect('success')

#     else:
#         form = RegistrationForm()

#     return render(request, 'EmailRegister.html', {'form': form})


# def success(request):
#     return render(request, 'EmailSuccess.html')
