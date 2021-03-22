from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView


router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include(
        'jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token', TokenRefreshView.as_view(),

         name="refresh_token"),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include('api.v1.accounts.urls')),
    path('cart/', include('api.v1.cart.urls')),
    path('carousel/', include('api.v1.carousel.urls')),
    path('category/', include('api.v1.category.urls')),
    path('orders/', include('api.v1.orders.urls')),
    path('payments/', include('api.v1.payments.urls')),
    path('products/', include('api.v1.products.urls')),
    path('stock/', include('api.v1.stock.urls')),
    path('wishlist/', include('api.v1.wishlist.urls'))




    
    
    
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]



