from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import index

urlpatterns = [
    # path('', index),
    re_path(r'^(?!static)', index),
] + static('static', document_root=settings.SPA_IMAGES_ROOT)