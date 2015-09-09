from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from gallery import views

urlpatterns = [
    url(r'^$', views.index, name='photolab.index'),
    url(r'^upload/', views.upload, name='photolab.upload'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
