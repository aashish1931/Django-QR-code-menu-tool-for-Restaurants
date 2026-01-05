from django.shortcuts import render,redirect
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings
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
            file_path=os.path.join(settings.MEDIA_ROOT,file_name)#media/ashish_menu.png
            qr.save(file_path)

            # create image url
            qr_url = settings.MEDIA_URL + file_name
            print(qr_url)
            context={
                'res_name':res_name,
                'qr_url':qr_url,
                'file_name':file_name,
            }
            return render(request,'qr_result.html',context)
    else:
        form=QRCodeForm()
        context={
            'form':form,
        }
        return render(request,'generate_qr_code.html',context)
    