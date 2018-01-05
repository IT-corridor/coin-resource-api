from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from mutualcoin.users.views import null_view, confirm_email
from mutualcoin.users.views import ( UserModelViewSet,
                                     AdminUserModelViewSet,
                                    UserLoginHistoryModelViewSet,)
from deposit.views import (DepositModelViewSet,
                            UserDepositModelViewSet,
                            PublicUserDepositModelViewSet,)


from assets.views import AssetModelViewSet, SoldAssetsModelViewSet
from rest_framework import routers
router = routers.DefaultRouter()

# app routes
# Admin Routes
router.register(r'users', UserModelViewSet)
router.register(r'admin-users', AdminUserModelViewSet)
router.register(r'logins', UserLoginHistoryModelViewSet, base_name='logins')
router.register(r'deposits', DepositModelViewSet)
router.register(r'user-deposits', UserDepositModelViewSet, base_name='user-deposits')
router.register(r'all-deposits', PublicUserDepositModelViewSet, base_name='all-deposits')

router.register(r'assets', AssetModelViewSet)
router.register(r'sell-assets', SoldAssetsModelViewSet)

urlpatterns = [

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
    # User management
    url(r'^accounts/', include('allauth.urls')),

    #auth urls
     url(r'^rest-auth/registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
     url(r'^rest-auth/registration/account-confirm-email/', null_view, name='account_confirm_email'),
     url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',null_view, name='password_reset_confirm'),
     url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
     url(r'^verify-email/(?P<key>\w+)/$', confirm_email, name="account_confirm_email"),
     url(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
     url(r'^auth/v1/api-token-auth/', obtain_jwt_token),
     url(r'^api-token-refresh/', refresh_jwt_token),
     url(r'^api/v1/', include(router.urls), name='home'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
