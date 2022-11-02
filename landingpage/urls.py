from django.urls import path
from landingpage.views import show_feedback, show_landingpage, get_faq, get_feedback, new_feedback

app_name = 'landingpage'

urlpatterns = [
    path('', show_landingpage, name='show_landingpage'),
    path('json/', get_faq, name='get_faq'),
    path('feedback_json/', get_feedback, name='get_feedback'),
    path('feedback/', show_feedback, name='feedback'),
    path('add_feedback/', new_feedback, name="new_feedback")
]