from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from os import remove
from django.conf import settings
from boto3 import resource
DOWNLOAD_PATH = getattr(settings, "DOWNLOAD_LOC", None)
MEDIA_ROOT_DIR = getattr(settings, "MEDIA_ROOT", None)
APP_URL = getattr(settings, "APP_MEDIA_URL", None)

s3 = resource('s3')


def index(request):
    return render(request, "filesnow/index.html")

@csrf_exempt

def deleteData(request):
    file_name1 = request.GET['Sstring']
    try:
        remove(DOWNLOAD_PATH+file_name1)

        error_string = "File Removed"
    except:
        error_string = "Something went Wrong, File still exist"

    delete_data_output = {'item': error_string}
    return JsonResponse(delete_data_output, safe=False)

@csrf_exempt
def sendData(request):

    file_name1 = request.GET['Sstring']
    server_protocol = request.GET['proto']
    server_root = request.GET['url']

    file_list = []
    try:

        my_bucket = s3.Bucket("randombkt")
        for file in my_bucket.objects.all():
            file_list.append(file.key)

        if file_name1 in file_list:
            my_bucket.download_file(file_name1, DOWNLOAD_PATH+file_name1)
            media_url = server_protocol+'//'+server_root+APP_URL+file_name1
            print(media_url)
        else:
            media_url = 4
        data = {'item': media_url}
        return JsonResponse(data['item'], safe=False)


    except:
        media_url = 5
        data = {'item': media_url}
        return JsonResponse(data['item'], safe=False)

