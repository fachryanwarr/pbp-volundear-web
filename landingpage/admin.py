from tkinter.messagebox import QUESTION
from django.contrib import admin
from landingpage.models import Faq, Feedback


admin.site.register(Faq)
admin.site.register(Feedback)
# Register your models here.
