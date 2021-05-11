from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
	path('',views.under_maintenance, name="under_maintenance"),
    path('master_trs',views.master_trs, name="master_trs"),
    path('ajaxcall_master_trs',views.ajaxcall_master_trs),
    path('ajaxcall_append',views.ajaxcall_append),
    path('ajaxcall_appendprs',views.ajaxcall_appendprs),
    ]