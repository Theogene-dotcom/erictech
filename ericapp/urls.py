from django.urls import path
from ericapp import views

app_name = "ericapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("blogs/", views.blogs, name="blogs"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("contact/", views.contact, name="contact"),
    path('blog/', views.blog_posts, name='blog_posts'),
    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('marketing/', views.mail_letter, name='mail_letter'),
]