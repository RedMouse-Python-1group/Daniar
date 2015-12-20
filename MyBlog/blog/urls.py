from django.conf.urls import  url




urlpatterns = [
    url(r'^$','blog.views.home', name='index_page'),
    url(r'^about/$','blog.views.about', name='about'),
    url(r'^contact/$','blog.views.contact', name ='contact'),
    url(r'^articles/(?P<article_id>[0-9]+)/$','blog.views.show_article', name='article'),

]