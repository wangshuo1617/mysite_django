from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
from fangtan import views as fangtan_views
from data import views as data_views
from poem import views as poem_views
admin.autodiscover()

urlpatterns =[
    # Examples:
    # url(r'^$', 'mywebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$',blog_views.index,name='index'),
    url(r'^detail/$', blog_views.detail,name='detail'),
    url(r'^fangtan/$',fangtan_views.all_duixiang,name='all_duixiang'),
    url(r'^fangtan/report/(?P<duixiang_id>[0-9]+)/',fangtan_views.report_list,name='report_list'),
    url(r'^fangtan/report_detail/(?P<report_id>[0-9]+)/',fangtan_views.report_detail,name='report_detail'),
    url(r'^fangtan/report/empty/$',fangtan_views.report_empty,name='report_empty'),
    url(r'^data/$',data_views.user,name='user'),
    url(r'^poem/random/$',poem_views.random_poem,name='random_poem'),
    url(r'^poem/test/$',poem_views.test,name='test'),
]
