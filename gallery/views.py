from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from logging import getLogger
from os import walk

LOG = getLogger(__name__)

def _find_all_photos(path):
    result = cache.get('photos')
    if not result is None:
        LOG.debug('CACHE HIT')
        return result

    result = []
    _, _, filenames = next(walk(path), (None, None, []))
    for filename in filenames:
        result.append(''.join([settings.MEDIA_URL, filename]))

    cache.set('photos', result)
    LOG.debug('CACHE MISS')
    return result

def _save_photo(photo):
    path = "%s/%s-%s" % (settings.MEDIA_ROOT, photo.size, photo.name)
    with open(path, 'wb+') as destination:
        for chunk in photo.chunks():
            destination.write(chunk)
    cache.delete('photos')

def index(request):
    context = {'photos': _find_all_photos(settings.MEDIA_ROOT)}
    return render(request, 'index.html', context)

@require_http_methods(['POST'])
def upload(request):
    _save_photo(request.FILES['photo'])
    return redirect('photolab.index')
