from .views import MailboxViewSet, TemplateViewSet, EmailViewSet
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


mailbox_list = MailboxViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

mailbox_detail = MailboxViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

template_list = TemplateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

template_detail = TemplateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

email_list = EmailViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = format_suffix_patterns([
    path('mailbox/', mailbox_list, name='mailbox-list'),
    path('mailbox/<str:pk>/', mailbox_detail, name='mailbox-detail'),
    path('template/', template_list, name='template-list'),
    path('template/<str:pk>/', template_detail, name='template-detail'),
    path('email/', email_list, name='email-list'),
])