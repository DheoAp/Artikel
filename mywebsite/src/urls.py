from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from artikel.views import(cv,loginPage,LogoutPage,Artikel,DetailArtikel,KategoriArtikel,
                        manage,create,update,delete,detail)
urlpatterns = [
    path('',cv,name='cv'),

    path('login',loginPage,name='login'),
    path('logout',LogoutPage,name='logout'),

    path('artikel/<str:page>',Artikel.as_view(),name='artikel'),
    path('artikel/<str:kategori>/<str:page>',KategoriArtikel.as_view(), name='kategori-artikel'),
    path('artikel-post/<str:slug>',DetailArtikel.as_view(),name='artikel-post'),
    path('manage-artikel',manage,name='manage'),
    # crud
    path('manage/create',create,name='create'),   
    path('manage/upadate/<str:update_id>',update,name='update'),
    path('manage/delete/<str:delete_id>',delete,name='delete'),
    path('manage/detail/<str:detail_id>',detail,name='detail'),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


