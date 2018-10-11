from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import student
# Create your views here.

def loginview( request ):
    print ( request.method, request.FILES)
    if request . method == 'POST' and len ( request.FILES) == 0 :
            if request.POST['uid'] == 'litindia' and request.POST['password'] == 'litindia':
                return render (request, 'askexcelfile.html')
            else:
                return render ( request, 'index.html', {'error': 'Invalid Login'})
    elif request.method == 'POST' and len ( request.FILES) != 0 :
            fileobj = open ('data.csv', 'wb')
            fileobj . write ( request.FILES ['studfile'] . read() )
            fileobj . close ()
            df = pd . read_csv ('data.csv')
            i = 0
            successmsg = []
            msg = ''
            while i < len (df):
                name = df . loc [ i ] . Name
                cource = df . loc [ i ] . Cource
                reg = df . loc [ i ] . RegNo
                mid = df . loc [ i ] . Mailid
                if len ( student . objects .  filter ( name = name , cource = cource , regno = reg, mid = mid )) == 0:
                    obj = student ( name = name , cource = cource , regno = reg, mid = mid )
                    obj . save ()
                    from PIL import Image
                    from PIL import ImageFont
                    from PIL import ImageDraw

                    img = Image.open("cer.jpg")
                    draw = ImageDraw.Draw(img)
                    # font = ImageFont.truetype(<font-file>, <font-size>)
                    font = ImageFont.truetype("./arial.ttf", 25);
                    # draw.text((x, y),"Sample Text",(r,g,b))
                    draw.text((80, 160),name,(0,0,0),font=font)
                    draw.text((80, 215),cource,(0,0,0),font=font)
                    img.save(name + cource + '.jpg')

                    successmsg . append (  name + cource + '.jpg' )
                else :
                    msg = msg + name + ' Allready taken Certificate on ' + cource + ' having REGNo ' + str(reg) +'<br>'
                i += 1
            if not msg :
                msg = str ( successmsg )
                    
            return HttpResponse ( str ( msg )   )
    return render ( request, 'index.html')
