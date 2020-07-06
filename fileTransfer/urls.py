from django.urls import path, include, reverse_lazy, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'file_transfer'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.FileUpload.as_view(), name='upload'),
    path('files/', views.FileList.as_view(), name='file_list'),
    path('files/<int:pk>', views.DeleteFile.as_view(), name='delete_file'),
    re_path('files/(?P<signed_pk>[0-9]+/[A-Za-z0-9_=-]+)/$', views.SingleFile.as_view(), name='single_file'),
    path('signup/', views.SignUp.as_view(), name='sign_up'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('file_transfer:password_change_done')), name='password_change'),
    path('accounts/', include('django.contrib.auth.urls')),
]