"""SATP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from student import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main,name="main"),
    path('main1/',views.main1,name="main1"),
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('login1/',views.login1,name="login1"),
    path('uregister/',views.uregister,name="uregister"),
    path('facregister/',views.facregister,name="facregister"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
        name='password_reset_complete'),
    path('dashboardz/',views.dashboardz,name="dashboardz"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('search/',views.search,name="search"),
    path('dashboard_1/<str:r>',views.dashboard_1,name="dashboard_1"),
    path('dashboard_2/<str:r>',views.dashboard_2,name="dashboard_2"),
    path('dashboard_3/<str:r>',views.dashboard_3,name="dashboard_3"),
    path('dashboard0/<str:u>',views.dashboard0,name="dashboard0"),
    path('dashboard1/<str:s>',views.dashboard1,name="dashboard1"),
    path('dashboard2/<str:s>',views.dashboard2,name="dashboard2"),
    path('dashboard3/<str:s>',views.dashboard3,name="dashboard3"),
    path('dashboard4/<str:r>',views.dashboard4,name="dashboard4"),
    path('dashboard5/<str:r>',views.dashboard5,name="dashboard5"),
    path('dashboard6/<str:r>',views.dashboard6,name="dashboard6"),
    path('edit1/<str:r>',views.edit1,name="edit1"),
    path('edit2/<str:r>',views.edit2,name="edit2"),
    path('update1/<str:r>',views.update1,name="update1"),
    path('update2/<str:r>',views.update2,name="update2"),
    path('delete/<str:r>/<str:d>',views.delete,name="delete")
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
