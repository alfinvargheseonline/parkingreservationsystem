"""VehicleParking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from vehicle.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
path('about',about,name='about'),
path('contact',contact,name='contact'),
path('admin_login',admin_login,name='admin_login'),
path('admin_home',admin_home,name='admin_home'),
path('logout',Logout,name='logout'),
path('change_password',change_password,name='change_password'),
path('add_category',add_category,name='add_category'),
    path('manage_category',manage_category,name='manage_category'),
path('delete_category/<int:pid>', delete_category,name='delete_category'),
path('edit_category/<int:pid>',edit_category,name='edit_category'),
path('add_vehicle',add_vehicle,name='add_vehicle'),
path('manage_incomingvehicle',manage_incomingvehicle,name='manage_incomingvehicle'),
path('view_incomingdetail/<int:pid>',view_incomingdetail,name='view_incomingdetail'),
path('manage_outgoingvehicle',manage_outgoingvehicle,name='manage_outgoingvehicle'),
path('view_outgoingdetail/<int:pid>',view_outgoingdetail,name='view_outgoingdetail'),
    path('print/<int:pid>',print_detail,name='print'),
path('search',search,name='search'),
path('betweendate_report',betweendate_report,name='betweendate_report'),
    path('betweendate_reportdetails',betweendate_reportdetails,name='betweendate_reportdetails'),
path('user_details_add', user_details_add, name='user_details_add'),
path('user_login', user_login, name='user_login'),
path('user_home',userhome,name="userhome"),
path('edit/<int:pk>',edit),
path('user_view_outgoing/<int:pid>',user_view_outgoing,name='user_view_outgoing'),
path('user_print/<int:pid>', user_print, name='user_print'),
path('navbar',navbar,name="navbar"),
path('user_add_vehicle',user_add_vehicle,name='user_add_vehicle'),
path('user_edit/<int:pk>',user_edit),
path('all/<int:id>',all_park,name="all"),
path('slots',slots),
path('book_slot',book_slot),
path('mybook',mybook),
<<<<<<< HEAD
path('out/<int:pk>',out),
path('user_print2',user_print2,name='user_print2'),
path('payment',payment),
path('add_parkings',add_parkings),
path('add_slot',add_slot),
path('total',total),
=======
path('out/<int:pk>',out)

>>>>>>> dcdd51991e6451e5b7086f8a13edce25391b62fd

]
