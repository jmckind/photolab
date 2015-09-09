from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from os import walk

def _find_all_photos(path):
    result = []
    _, _, filenames = next(walk(path), (None, None, []))
    for filename in filenames:
        result.append(''.join([settings.MEDIA_URL, filename]))
    return result

def _save_photo(photo):
    path = "%s/%s-%s" % (settings.MEDIA_ROOT, photo.size, photo.name)
    with open(path, 'wb+') as destination:
        for chunk in photo.chunks():
            destination.write(chunk)

def index(request):
    context = {'photos': _find_all_photos(settings.MEDIA_ROOT)}
    return render(request, 'index.html', context)

@require_http_methods(['POST'])
def upload(request):
    _save_photo(request.FILES['file'])
    return redirect('photolab.index')
