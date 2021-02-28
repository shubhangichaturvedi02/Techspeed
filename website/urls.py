
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
urlpatterns = [
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('work_with_us/',views.Work_withuss,name="work_with_us"),
    path('services/',views.services,name="services"),
    path('logout/',views.logout,name="logout"),
    path('videos/',views.videos,name="videos"),
    path('tech_support/',views.tech_support,name="tech_support"),
    path('video_tech/',views.video_tech,name="video_tech"),
    path('one_on_one_online/',views.one_on_one_online,name="one_on_one_online"),
    path('online_g_d/',views.online_g_d,name="online_g_d"),
    path('process_payment/',views.process_payment,name="process_payment"),
    path('payment_done/',views.payment_done,name="payment_done"),
    path('payment_canceled/',views.payment_canceled,name="payment_canceled"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('create_query_page/',views.create_query_page),
    path('Welcome/',views.welcome,name="welcome"),
    path('team/',views.team,name='team'),
    path('GD_success/',views.GD_success,name='GD_success'),
    url(r'^$',views.home),
    url(r'^search/',views.search_view),
    url(r'^pay2/',views.pay2),
    url(r'^pay1/',views.pay1,name='pay1'),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
