from django.urls import path
# TemplateView is a generic view that renders a template
from django.views.generic import TemplateView
from . import views

app_name = 'dashboard'


urlpatterns = [
    path("", views.DashboardView.as_view(), name="home"),
    # path("barcode/", views.detect, name="barcode"),
    path("camera_feed/", views.camera_feed, name="camera_feed"),
<<<<<<< HEAD
<<<<<<< HEAD
    path("list-products/", TemplateView.as_view(template_name="pages/dashboard/products/list_products.html"), name="list-products"),
    path("edit-product/", TemplateView.as_view(template_name="pages/dashboard/products/edit_product.html"), name="edit-product"),
    path("add-product-kemasan/", TemplateView.as_view(template_name="pages/dashboard/products/add_product_kemasan.html"), name="add-product-kemasan"),
    path("add-product-non-kemasan/", TemplateView.as_view(template_name="pages/dashboard/products/add_product_non_kemasan.html"), name="add-product-non-kemasan"),
=======
=======
>>>>>>> a86cf4855e5984bb8d39e3d5f2e2a08e11a6c43a
    path("add-product-kemasan", views.add_product_kemasan, name="add-product-kemasan"),
    path("list-prducts/", TemplateView.as_view(template_name="pages/dashboard/products/list_products.html"), name="list-products"),
    path("edit-product/", TemplateView.as_view(template_name="pages/dashboard/products/edit_product.html"), name="edit-product"),
    path("add-barcode/", views.BarcodeCreateView.as_view(), name="add-barcode"),
    path("list-barcode/", views.BarcodeListView.as_view(), name="list-barcode"),

<<<<<<< HEAD
>>>>>>> a86cf4855e5984bb8d39e3d5f2e2a08e11a6c43a
=======
>>>>>>> a86cf4855e5984bb8d39e3d5f2e2a08e11a6c43a
]

