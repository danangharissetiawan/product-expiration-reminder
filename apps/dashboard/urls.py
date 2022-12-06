from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# TemplateView is a generic view that renders a template
from django.views.generic import TemplateView
from . import views

app_name = 'dashboard'


urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="home"),
    # path("barcode/", views.detect, name="barcode"),
    path("camera_feed/", views.camera_feed, name="camera_feed"),
    path("open_camera_view/", views.open_camera_view, name="open_camera_view"),
    path("add-product-non-kemasan/", views.ProductNonPackagingCreateView.as_view(), name="add-product-non-kemasan"),
    path("add-product-kemasan/", views.ProductPackagingCreateView.as_view(), name="add-product-kemasan"),
    path("list-products/", views.ProductPackagingListView.as_view(), name="list-products"),
    path("list-products-nonkemasan/", views.ProductNonPackagingListView.as_view(), name="list-products-nonkemasan"),
    path("edit-product-kemasan/<int:pk>/", views.ProductPackagingUpdateView.as_view(), name="edit-product-kemasan"),
    path("edit-product-nonkemasan/<int:pk>/", views.ProductNonPackagingUpdateView.as_view(), name="edit-product-nonkemasan"),
    path("delete-product-kemasan/", views.ProductPackagingDelete.as_view(), name="delete-product-kemasan"),
    path("delete-product-nonkemasan/", views.ProductNonPackagingDelete.as_view(), name="delete-product-nonkemasan"),
    path("add-barcode/", views.BarcodeCreateView.as_view(), name="add-barcode"),
    path("list-barcode/", views.BarcodeListView.as_view(), name="list-barcode"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("edit-profile/<int:pk>/", views.ProfileUpdateView.as_view(), name="edit-profile"),
    path("notifications/", views.NotificationView.as_view(), name="notifications"),
    path("image-upload/", views.image_upload, name="image-upload"),
]

