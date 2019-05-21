from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'posts/$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^profile/$',views.edit_profile_info, name='edit_profile_info'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)