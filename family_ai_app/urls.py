from django.urls import path
from family_ai_app.views.auth_views import home, alerts
from family_ai_app.views.user_views import UserListView
from family_ai_app.views.ticket_views import (
    TicketListCreateView,
    TicketDetailView,
    TicketDeleteView,
    AssignSelfToTicketView,
)
from family_ai_app.views.message_views import (
    MessageListCreateView,
    MessageDetailView,
)
from family_ai_app.views.notification_views import (
    NotificationListView,
    NotificationDetailView,
)

app_name = 'family_ai_app'

urlpatterns = [
    # Navigation endpoints
    path('', home, name='home'),
    path('notifications/', alerts, name='alerts'),

    # User endpoints
    path('users/', UserListView.as_view(), name='user-list'),

    # Ticket endpoints
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket-delete'),
    path('tickets/<int:pk>/assign-me/', AssignSelfToTicketView.as_view(), name='ticket-assign-self'),

    # Message endpoints
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),

    path('api/notifications/', NotificationListView.as_view(), name='notification-list'),
    path('api/notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
]