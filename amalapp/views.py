from django.shortcuts import render

def amallar(request):

    if request.method=='GET':
        try:
            a=int(request.GET.get('first_number'))
            b=int(request.GET.get('second_number'))
            amal=request.GET.get('amal')
            if amal=='qushish':
                contex={
                    'natija': f"{a}+{b}={a+b}"
                }
            if amal=='ayirish':
                contex={
                    'natija':f"{a}-{b}={a-b}"
                }
            if amal=='kupaytirish':
                contex={
                    'natija':f"{a}*{b}={a*b}"
                }
            if amal=='bolish':
                contex={
                    'natija':f"{a}/{b}={a/b}"
                }
        except:
            contex={
                'xatolik':'son kiritilmagan'
            }

    return render(request,'amalapp/amallar.html',contex)
