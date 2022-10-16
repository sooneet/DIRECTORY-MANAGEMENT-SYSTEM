from django.contrib import admin
from django.urls import path
from directory import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('login/', views.Login,name='login'),
    path('dashboard/', views.dashboard,name='dashboard'),


    path('add-directory/', views.add_directory,name='add-directory'),
    path('manage-directory/', views.manage_directory,name='manage-directory'),
    path('edit-directory/<int:pid>/', views.edit_directory,name='edit-directory'),
    path('delete-directory/<int:pid>/', views.delete_directory,name='delete-directory'),
    path('search-directory/', views.search_directory,name='search-directory'),

    path('all-record/', views.all_record,name='all-record'),
    path('private-record/', views.private_record,name='private-record'),
    path('public-record/', views.public_record,name='public-record'),
    path('view-all-record/', views.view_all_record,name='view-all-record'),
    path('view-search-data/', views.view_search_data,name='view-search-data'),

    path('change-password/', views.change_password,name='change-password'),

    path('logout/', views.Logout,name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
