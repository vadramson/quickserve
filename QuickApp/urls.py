"""QuickApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from QuickServe import urls as api_urls

from QuickServe import views as quickServe_views

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^$', quickServe_views.home, name='home'),
               url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
               url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
               url(r'^create/user/$', quickServe_views.createUser, name='createUser'),
               url(r'^users/$', quickServe_views.user_list, name='user_list'),

               # Agency Urls
               url(r'^agency/$', quickServe_views.agency_list, name='agency_list'),
               url(r'^agency/create/$', quickServe_views.agency_create, name='agency_create'),
               url(r'^agency/(?P<pk>\d+)/update/$', quickServe_views.agency_update, name='agency_update'),
               url(r'^agency/(?P<pk>\d+)/delete/$', quickServe_views.agency_delete, name='agency_delete'),

               # Department Urls
               url(r'^department/$', quickServe_views.department_list, name='department_list'),
               url(r'^department/create/$', quickServe_views.department_create, name='department_create'),
               url(r'^department/(?P<pk>\d+)/update/$', quickServe_views.department_update, name='department_update'),
               url(r'^department/(?P<pk>\d+)/delete/$', quickServe_views.department_delete, name='department_delete'),

               # Menu Urls
               url(r'^menu/$', quickServe_views.menu_list, name='menu_list'),
               url(r'^menu/create/$', quickServe_views.menu_create, name='menu_create'),
               url(r'^menu/(?P<pk>\d+)/update/$', quickServe_views.menu_update, name='menu_update'),
               url(r'^menu/(?P<pk>\d+)/delete/$', quickServe_views.menu_delete, name='menu_delete'),

               # Category Urls
               url(r'^category/$', quickServe_views.category_list, name='category_list'),
               url(r'^category/create/$', quickServe_views.category_create, name='category_create'),
               url(r'^category/(?P<pk>\d+)/activate/$', quickServe_views.category_activate, name='category_activate'),
               url(r'^deactivate/(?P<pk>\d+)/deactivate/$', quickServe_views.category_deactivate,
                   name='category_deactivate'),
               url(r'^category/(?P<pk>\d+)/update/$', quickServe_views.category_update, name='category_update'),
               url(r'^category/(?P<pk>\d+)/delete/$', quickServe_views.category_delete, name='category_delete'),

               # Product Urls
               url(r'^product/$', quickServe_views.product_list, name='product_list'),
               url(r'^product/create/$', quickServe_views.product_create, name='product_create'),
               url(r'^product/(?P<pk>\d+)/update/$', quickServe_views.product_update, name='product_update'),
               url(r'^product/(?P<pk>\d+)/activate/$', quickServe_views.product_activate, name='product_activate'),
               url(r'^product/(?P<pk>\d+)/deactivate/$', quickServe_views.product_deactivate,
                   name='product_deactivate'),

               # Expense Urls
               url(r'^expense/$', quickServe_views.expense_list, name='expense_list'),
               url(r'^expense/add/$', quickServe_views.expense_create, name='expense_create'),
               url(r'^expense/(?P<pk>\d+)/update/$', quickServe_views.expense_update, name='expense_update'),
               url(r'^expense/(?P<pk>\d+)/delete/$', quickServe_views.expense_delete, name='expense_delete'),

               # Loss Urls
               url(r'^loss/$', quickServe_views.loss_list, name='loss_list'),
               url(r'^loss/add/$', quickServe_views.loss_create, name='loss_create'),
               url(r'^loss/(?P<pk>\d+)/update/$', quickServe_views.loss_update, name='loss_update'),
               url(r'^loss/(?P<pk>\d+)/delete/$', quickServe_views.loss_delete, name='loss_delete'),

               # Bonus Urls
               url(r'^bonus/$', quickServe_views.bonus_list, name='bonus_list'),
               url(r'^bonus/add/$', quickServe_views.bonus_create, name='bonus_create'),
               url(r'^bonus/(?P<pk>\d+)/update/$', quickServe_views.bonus_update, name='bonus_update'),
               url(r'^bonus/(?P<pk>\d+)/delete/$', quickServe_views.bonus_delete, name='bonus_delete'),

               # Deduction Urls
               url(r'^deduction/$', quickServe_views.deduction_list, name='deduction_list'),
               url(r'^deduction/add/$', quickServe_views.deduction_create, name='deduction_create'),
               url(r'^deduction/(?P<pk>\d+)/update/$', quickServe_views.deduction_update, name='deduction_update'),
               url(r'^deduction/(?P<pk>\d+)/delete/$', quickServe_views.deduction_delete, name='deduction_delete'),

               # Purcahse Urls
               url(r'^purchase/$', quickServe_views.purchase_list, name='purchase_list'),
               url(r'^purchase/create/$', quickServe_views.purchase_create, name='purchase_create'),
               url(r'^purchase/(?P<pk>\d+)/update/$', quickServe_views.purchase_update, name='purchase_update'),

               # Avaris Urls
               url(r'^avaris/$', quickServe_views.avaris_list, name='avaris_list'),
               url(r'^avaris/create/$', quickServe_views.avaris_create, name='avaris_create'),
               url(r'^avaris/(?P<pk>\d+)/update/$', quickServe_views.avaris_update, name='avaris_update'),

               # Stock Urls
               url(r'^stock/$', quickServe_views.stock_list, name='stock_list'),
               url(r'^stock/create/$', quickServe_views.stock_create, name='stock_create'),

               # Tabs Urls
               url(r'^tab/(?P<urs>\d+)/$', quickServe_views.tab_list, name='tab_list'),
               url(r'^tabs/(?P<urs>\d+)/$', quickServe_views.tab_list_closed, name='tab_list_closed'),
               url(r'^tab/(?P<urs>\d+)/create/$', quickServe_views.tab_create, name='tab_create'),

               # Orders Urls
               url(r'^order/(?P<pk>\d+)(?P<urs>\d+)/list/$', quickServe_views.order_list, name='order_list'),
               url(r'^orders/(?P<pk>\d+)(?P<urs>\d+)/Closed/$', quickServe_views.order_list_closed,
                   name='order_list_closed'),
               # url(r'^orders/(?P<pk>\d+)/Closed/$', quickServe_views.order_list_closed, name='order_list_closed'),
               url(r'^order/(?P<pk>\d+)/create/$', quickServe_views.order_create, name='order_create'),
               url(r'^order/(?P<pk>\d+)/delete/$', quickServe_views.order_delete, name='order_delete'),

               # Sales Urls
               url(r'^sale/(?P<pk>\d+)/list/$', quickServe_views.sale_list, name='sale_list'),
               url(r'^sale/(?P<pk>\d+)/validate/$', quickServe_views.sale_create, name='sale_create'),
               url(r'^sale/(?P<pk>\d+)/update/$', quickServe_views.sale_update, name='sale_update'),

               # Print Urls
               url(r'^print/list/$', quickServe_views.print_list, name='print_list'),
               url(r'^printed/list/$', quickServe_views.printed_list_msg, name='printed_list_msg'),
               url(r'^print/(?P<pk>\d+)/list/pdf/$', quickServe_views.print_list_pdf, name='print_list_pdf'),
               url(r'^printed/(?P<pk>\d+)/list/pdf/$', quickServe_views.printed_list_pdf, name='printed_list_pdf'),

               # Attendance Urls
               url(r'^list/attendance/$', quickServe_views.attendance_list, name='attendance_list'),
               url(r'^clockin/$', quickServe_views.attendance_clockin, name='attendance_clockin'),
               url(r'^clockout/$', quickServe_views.attendance_clockout, name='attendance_clockout'),

               # API Urls
               url(r'^quickserve/api/', include(api_urls, namespace="api")),

               # Charts Urls
               url(r'^reports/$', quickServe_views.reports, name='reports'),
               url(r'^reports/products/$', quickServe_views.product_report, name='product_stat'),
               url(r'^reports/cashFlow/$', quickServe_views.cash_out_stat, name='cash_out_statistic'),
               url(r'^reports/purchases/$', quickServe_views.purchase_statistic, name='purchase_statistic'),

               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
	To prevent url so that a user must be logged in before he can access the links with prefix login_required
    from django.contrib.auth.decorators import login_required

     url(r'^login/$', login_required(auth_views.login), {'template_name': 'auth/login.html'}, name='login'), user must be logged in before he can access this link
     url(r'^logout/$', views.logout, name='logout'),

"""
