from django.shortcuts import render,redirect
from .forms import QRCodeForm
import qrcode
def generate_qr_code(request):
    if request.method=='POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            res_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']

            #generate qr code
            qr=qrcode.make(url)
           # print(qr)#<qrcode.image.pil.PilImage object at 0x0000015D8D228D70> qr code
            file_name=res_name.replace(" ","_").lower() + "_menu.png"
            qr.save(file_name)
    else:
        form=QRCodeForm()
        context={
            'form':form,
        }
        return render(request,'generate_qr_code.html',context)
    