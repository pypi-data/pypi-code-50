"Views for a python package index"
import functools
import base64
from django.http import (HttpResponse, HttpResponseBadRequest,
    HttpResponseForbidden, HttpResponseNotFound, FileResponse)
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from . import models


class IndexView(ListView):
    template_name = 'djmypypi/index.html'
    queryset = models.Package.objects.order_by('name')


class PackageView(DetailView):
    template_name = 'djmypypi/package.html'
    model = models.Package
    slug_field = 'name'
    slug_url_kwarg = 'package_name'


def basic_authentication(func):
    "Decorator for http basic authentication on views."
    @functools.wraps(func)
    def _basic_authentication(request, *args, **kwargs):
        header_value = request.META.get('HTTP_AUTHORIZATION')
        if not header_value:
            return func(request, *args, **kwargs)
        if not header_value.startswith('Basic '):
            return func(request, *args, **kwargs)
        decoded_value = base64.b64decode(header_value[6:]).decode('utf8')
        value_items = decoded_value.split(':')
        if len(value_items) != 2:
            return func(request, *args, **kwargs)
        username, password = value_items
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return func(request, *args, **kwargs)
    return _basic_authentication


@csrf_exempt
@basic_authentication
@login_required
@permission_required('djmypypi.add_package', raise_exception=True)
def upload_package(request):
    "Handle uploading a package."
    package_file = request.FILES['content']
    # validates the archive doesnot exist
    if models.Version.version_archive_exist(package_file.name):
        return HttpResponseBadRequest("This package archive already exist: {}".format(
            package_file.name))
    # get or create the package
    try:
        package = models.Package.objects.get(name=request.POST['name'])
        if package.user.pk != request.user.pk:
            return HttpResponseForbidden("You are not the owner of this package")
    except models.Package.DoesNotExist:
        package = models.Package()
        package.name = request.POST['name']
        package.user = request.user

    version = models.Version(package=package)

    package.version = version.version = request.POST['version']
    package.author = version.author = request.POST.get('author')
    package.author_email = version.author_email = request.POST.get('author_email')
    package.maintainer = version.maintainer = request.POST.get('maintainer')
    package.maintainer_email = version.maintainer_email = request.POST.get('maintainer_email')
    package.summary = version.summary = request.POST.get('summary')
    package.description = version.description = request.POST.get('description')
    package.home_page = version.home_page = request.POST.get('home_page')
    package.license = version.license = request.POST.get('license')
    package.classifiers = version.classifiers = "\n".join(request.POST.getlist('classifiers', []))
    version.md5_digest = request.POST.get('md5_digest')
    version.archive_name = package_file.name

    package.save()
    version.save()

    version.archive.save(package_file.name, package_file, save=True)

    return HttpResponse("ok")


def download_package(request, package_name):
    version = get_object_or_404(models.Version, archive_name=package_name)
    version.archive.open()
    return FileResponse(version.archive, as_attachment=True, filename=package_name)
