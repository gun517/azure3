"""azure3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

def hello(request):
    return HttpResponse('''
        <h1>Hello, <a href="http://facebook.com/askdjango/" target="_blank">AskDjango</a></h1>
    ''')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , hello),
    url(r'^blog/$', 'blog.views.post_list'),
    url(r'^blog/(?P<pk>\d+)/$', 'blog.views.post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

