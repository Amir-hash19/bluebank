from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os



def show_user_page(request, name):
    return HttpResponse(f"this is user page -->{name}<--")



def show_info(request):
    file_info = os.path.join("/home/amirykta/Desktop/BlueBank/bluebank/account/info.pdf")
    return FileResponse(
        open(file_info, "rb"),
        as_attachment=True
    )
   