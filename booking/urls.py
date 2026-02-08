from django.urls import path
from .views import login_view
from .views import register_view
from .views import logout_view

from .views import (
    home,
    slots_page,
    specialization_page,
    provider_detail,
    slots_api,
    providers_api,
    bookings_api,
)

urlpatterns = [
    # AUTH
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('verify-phone/', verify_phone, name='verify_phone'),
    path('resend-otp/', resend_otp, name='resend_otp'),

    # PAGES
    path('', home, name='home'),
    path('slots/', slots_page, name='slots'),
    path('specialization/<str:name>/', specialization_page, name='specialization'),
    path('provider/<int:provider_id>/', provider_detail, name='provider_detail'),

    # BOOKING
    path('book/<int:slot_id>/', book_slot, name='book_slot'),
    path('my-appointments/', my_appointments, name='my_appointments'),
    path('my-schedule/', my_schedule, name='my_schedule'),

    # API
    path('api/slots/', slots_api),
    path('api/slots/<int:slot_id>/', slots_api),
    path('api/providers/', providers_api),
    path('api/providers/<int:provider_id>/', providers_api),
    path('api/bookings/', bookings_api),
    path('api/bookings/<int:booking_id>/', bookings_api),
]
