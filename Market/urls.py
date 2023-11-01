from django.urls import path
from .views import index, show_item, publish, get_order, show_order, payment, cancel_order, admin, admin_remove

app_name = 'Market'
urlpatterns = [
    path('', index),
    path('Market/', show_item, name='show_item'),
    path('Market/publish/', publish, name='publish'),
    path('get_order/<slug:item_id>', get_order, name='get_order'),
    path('Market/order/', show_order, name='show_order'),
    path('Market/payment/<int:order_id>/', payment, name='payment'),
    path('Market/cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('Market/admin/', admin, name='admin'),
    path('admin_remove/<slug:item_id>', admin_remove, name='admin_remove'),
]