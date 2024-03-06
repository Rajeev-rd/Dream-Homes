from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from  . import settings
import Adminmodule.urls
import Usermodule.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include(Adminmodule.urls)),
    path('main/',include(Usermodule.urls)),
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
