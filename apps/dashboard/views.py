from django.http import request, StreamingHttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from . import models
import os
import time
from datetime import datetime
from PIL import Image
from pyzbar.pyzbar import decode

from .utils.camera_streaming import CameraStreamingWidget


# from utils.camera_streaming import CameraStreamingWidget


class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.session)
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Timelock"
        return render(request, 'menu/index.html',greeting)


def camera_feed(request):
    stream = CameraStreamingWidget()
    frames = stream.get_frames()

    # if ajax request is sent
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        barcode_data = None
        file_saved_at = None
        barcode_name = ''
        print('Ajax request received')
        time_stamp = str(datetime.now().strftime("%d-%m-%y"))
        image = os.path.join(os.getcwd(), "media",
                             "images", f"img_{time_stamp}.png")
        if os.path.exists(image):
            # open image if exists
            im = Image.open(image)
            # decode barcode
            if decode(im):
                for barcode in decode(im):
                    barcode_data = (barcode.data).decode('utf-8')
                    file_saved_at = time.ctime(os.path.getmtime(image))
                    # return decoded barcode as json response

                if models.Barcode.objects.filter(barcode=str(barcode_data)).exists():
                    barcode_name = models.Barcode.objects.filter(barcode=str(barcode_data)).first()
                    return JsonResponse(data={'barcode_data': barcode_data, 'file_saved_at': file_saved_at, 'barcode_name': barcode_name.name})
                return JsonResponse(data={'barcode_data': barcode_data, 'file_saved_at': file_saved_at, 'barcode_name': barcode_name})
            else:
                return JsonResponse(data={'barcode_data': None})
        else:
            return JsonResponse(data={'barcode_data': None})
    # else stream the frames from camera feed
    else:
        return StreamingHttpResponse(frames, content_type='multipart/x-mixed-replace; boundary=frame')


def detect(request):
    # stream = CameraStreamingWidget()
    # success, frame = stream.camera.read()
    # if success:
    #     status = True
    # else:
    #     status = False
    status = open_camera()
    return render(request, 'pages/dashboard/barcode.html', context={'cam_status': status})


def open_camera():
    stream = CameraStreamingWidget()
    success, frame = stream.camera.read()
    if success:
        status = True
    else:
        status = False
    return status


def add_product_kemasan(request):
    status = open_camera()
    return render(request, 'pages/dashboard/products/add_product_kemasan.html', context={'cam_status': status})

