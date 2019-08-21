from django.urls import re_path,path
from django.contrib.auth import views as auth_views
from . import views, forms
urlpatterns = [
    path('', views.empty_view, name='empty'),

    re_path(r'^login/$', views.login_view, name='login'),

    re_path(r'^logout/$', views.logout_view, name='logout'),

    re_path(r'^export/all/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.export_all, name='export_all'),

    re_path(r'export/with_troubles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.export_with_troubles,
            name='export_with_troubles'),

    re_path(r'export/not_sent/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.export_not_sent, name='export_not_sent'),

    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(
        template_name='app/registration/password_reset_form.html',
        form_class=forms.PassResetForm), name='password_reset'),

    re_path(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(
        template_name='app/registration/password_reset_confirm.html',
            form_class=forms.PassResetConfirmForm), name='password_reset_confirm'),

    re_path(r'^password_reset_done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='app/registration/password_reset_done.html'), name='password_reset_done'),

    re_path(r'^password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/registration/password_reset_complete.html'), name='password_reset_complete'),

    re_path(r'^form/$', views.get_self_examination_form, name='self_examination_form'),

    re_path(r'^result_form/with_troubles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.get_result_form_with_troubles, name='with_troubles'),
    re_path(r'^result_form/with_no_troubles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.get_with_no_troubles, name='with_no_troubles'),
    re_path(r'^result_form/not_sent/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.get_result_form_not_sent, name='not_sent'),
    re_path(r'^result_form/(?P<service_name>[a-z_]{10,30})/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.get_result_form, name='result_form'),
    re_path(r'^result_form/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<short_region_name>[a-z]{3,60})/$',
            views.get_region_form, name='region_form')

]
