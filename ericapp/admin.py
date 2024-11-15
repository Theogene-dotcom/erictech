from django.contrib import admin
from ericapp.models import Contact,BlogPost,Comment,Subscription,MailMessage

# Register your models here.
admin.site.register(Contact)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Subscription)
admin.site.register(MailMessage)