from django.contrib import admin
#from django.contrib import master
from django.urls import path

from . import views
#from . import master


urlpatterns = [
	path('',views.under_maintenance, name="under_maintenance"),
    path('master_trs',views.master_trs, name="master_trs"),
    path('countrycode',views.countrycode, name="countrycode"),
    path('chaptermaster',views.chaptermaster, name="chaptermaster"),
    path('comparison_mrs',views.comparison_mrs, name="comparison_mrs"),
    path('ajaxcall_master_trs',views.ajaxcall_master_trs),
    path('ajaxcall_append',views.ajaxcall_append),
    path('ajaxcall_append_select',views.ajaxcall_append_select),
    path('ajaxcall_append_selectcountrycode',views.ajaxcall_append_selectcountrycode),
    path('ajaxcall_appendprs',views.ajaxcall_appendprs),
    path('ajaxcall_country',views.ajaxcall_country),
    path('ajaxcall_countrycode',views.ajaxcall_countrycode),
    path('get_chaptercode',views.get_chaptercode),
    path('hsncode_chapter_master_count',views.hsncode_chapter_master_count),
    path('hsncode_length_data',views.hsncode_length_data),
    path('ajaxcall_append_selectcountrycodesing',views.ajaxcall_append_selectcountrycodesing),
    path('product_code_data',views.product_code_data),
    path('hsn_product_code_data',views.hsn_product_code_data),
    path('ajaxcall_chaptermaster',views.ajaxcall_chaptermaster),

    path('ajaxcall_chapterlengthdata',views.ajaxcall_chapterlengthdata),
    path('ajaxcall_append_selectcountrycode_hsncode',views.ajaxcall_append_selectcountrycode_hsncode),
    path('ajaxcall_chapterlengthall',views.ajaxcall_chapterlengthall),
    path('ajaxcall_append_selectchapterlength_all',views.ajaxcall_append_selectchapterlength_all),
    path('compardesign',views.compardesign),
    path('multiplecountry_chapter_hsncode_productcode',views.multiplecountry_chapter_hsncode_productcode),
    path('get_hsncode_description',views.get_hsncode_description),
    ]