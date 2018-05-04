from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'reviews'

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /product/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /product/
    url(r'^product$', views.product_list, name='product_list'),
    # ex: /product/5/
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^product/(?P<product_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    # ex: /review/user - get reviews for the user passed in the url
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
