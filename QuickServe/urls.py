from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views as rest_framework_views
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth import views as auth_views

from .views import ProductAll, my_drf_login, my_drf_logout, TabsDetailView, get_tabs, TabsAdd, TabsGetOpen, \
    TabsGetClosed, OrdersGet, OrdersAdd, OrdersDel, OrdersGetParticular, ClockIn, ClockOut, Sale, ProductStats, \
    CashOutStats, ExpenseStats, AvarisStats, PurchasesStats, get_all_my_open_tabs, my_open_tabs, my_closed_tabs, \
    ProductViewSet, AttendStats

router = SimpleRouter()
router.register("products", ProductViewSet)
# router.register("tabs", TabsDetailView)
# router.register("login", login)

# urlpatterns = router.urls
# # url(r'^login', login)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^jwt-auth/', obtain_jwt_token),
    url(r'^login', my_drf_login),
    url(r'^logout', my_drf_logout),
    url(r'^tabs/get/all', get_all_my_open_tabs),
    url(r'^tabs/gets/$', get_tabs),
    url(r'^tabs/(?P<pk>[0-9]+)/$', TabsDetailView.as_view()),
    url(r'^tabs/myOpen/$', my_open_tabs),
    url(r'^tabs/myClosed/$', my_closed_tabs),
    url(r'^tabs/add/$', TabsAdd.as_view()),
    url(r'^tabs/get/open/$', TabsGetOpen.as_view()),
    url(r'^tabs/get/closed/$', TabsGetClosed.as_view()),
    url(r'^orders/get/$', OrdersGet.as_view()),
    url(r'^orders/add/$', OrdersAdd.as_view()),
    url(r'^orders/del/$', OrdersDel.as_view()),
    url(r'^orders/get/particular/$', OrdersGetParticular.as_view()),
    url(r'^clockin/$', ClockIn.as_view()),
    url(r'^clockout/$', ClockOut.as_view()),
    url(r'^sale/$', Sale.as_view()),
    url(r'^product/$', ProductAll.as_view()),
    url(r'^reports/products/$', ProductStats.as_view()),
    url(r'^outflow/cashOut/$', CashOutStats.as_view()),
    url(r'^expense/$', ExpenseStats.as_view()),
    url(r'^avaris/$', AvarisStats.as_view()),
    url(r'^reports/purchases/$', PurchasesStats.as_view()),
    url(r'^reports/purchases/$', PurchasesStats.as_view()),
    url(r'^reports/attendance/$', AttendStats.as_view()),
    # url(r'^tabs/$', TabsDetailView),
]