from django.shortcuts import render,redirect

# Create your views here.

li1 = []
k = 1
def home(request):
    # data = request.POST.get('first_name')
    # print(data['first_name'])
    # print(data)
    global k

    di1 = {}
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    
    if first_name and last_name:
        di1.update({'id':k,'first_name':first_name,'last_name':last_name})
        li1.append(di1)
        k+=1
        return redirect('/home/')

    return render(request,'index.html')

def show_data(request):
    context = {'result':li1}
    return render(request,'show_data.html',context)

def data(reuqest,id):
    data  = None
    for i in li1:
        print(id)
        if i['id'] == id:
            data = i
            print(data)
            break
    context = {'data':data}
    return render(reuqest,'data.html',context)

# def clear_data(request):
#     li1.clear()
#     return redirect('/show_data/')
