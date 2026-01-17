from django.shortcuts import render
from django.http import HttpResponse


def set_session(request):
    request.session['username'] = 'Dev'
    request.session['course'] = 'Django Course'
    return HttpResponse('Session data saved successfully.')


def get_session(request):
    username = request.session.get('username','Guest')
    course = request.session.get('course','not enrolled')

    return HttpResponse(f"Welcome : {username} , your are learning : {course}")


def delete_session(request):
    # try:
    #     del request.session['username']
    #     del request.session['course']
    # except KeyError:
    #     pass
    # return HttpResponse('Session data deleted successfully')
    request.session.flush()
    return HttpResponse('Session data deleted successfully')




# def set_cookie(request):
#     responce = HttpResponse('Cookies set successfully')
#     responce.set_cookie('username','Dev',max_age= 60*60*24) ## valid for 1 days
#     responce.set_cookie('course','Django',max_age= 60*60*24) ## valid for 1 days
#     return responce

# def get_cookie(request):
#     username = request.COOKIES.get('username','Guest')
#     course = request.COOKIES.get('course','Not Course selected')
#     if 'username' in request.COOKIES:
#         return HttpResponse(f"Username: {username}, Course {course}")
#     else:
#         return HttpResponse('No cookies found')

# def delete_cookie(request):
#     responce = HttpResponse('Cookies deleted successfully')
#     responce.delete_cookie('username')
#     responce.delete_cookie('course')
#     return responce