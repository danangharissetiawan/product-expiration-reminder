from django.urls import path
# TemplateView is a generic view that renders a template
from django.views.generic import TemplateView
from . import views

app_name = 'dashboard'


urlpatterns = [
    path("", views.DashboardView.as_view(), name="home"),
    path("list-prducts/", TemplateView.as_view(template_name="pages/dashboard/products/list_products.html"), name="list-products"),
]

