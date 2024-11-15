from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.paginator import Paginator
from .models import BlogPost
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import CommentForm
from django.core.mail import send_mail



# Create your views here.
def index(request):
    return render (request, "ericapp/index.html")

def careers(request):
    return render (request, "ericapp/careers.html")
def about(request):
    return render (request, "ericapp/about.html")

def services(request):
    return render (request, "ericapp/services.html")
def portfolio(request):
    return render (request, "ericapp/portfolio.html")

def blogs(request):
    return render (request, "ericapp/blogs.html")

def terms(request):
    return render (request, "ericapp/terms.html")

def privacy(request):
    return render (request, "ericapp/privacy.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
            return redirect('ericapp:contact')  # Replace 'ericapp:contact' with your contact URL name
    else:
        form = ContactForm()
    return render(request, 'ericapp/contact.html', {'form': form})

def blog_posts(request):
    posts_list = BlogPost.objects.all().order_by('-published_date')  # Order posts by date
    paginator = Paginator(posts_list, 20)  # Show 20 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'ericapp/blog_posts.html', {'page_obj': page_obj})


def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    # Handle the comment form submission
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.save()
            return redirect('ericapp:blog_post_detail', pk=post.pk)  # Redirect to the same post after adding the comment
    else:
        form = CommentForm()

    # Get all comments for this post
    comments = post.comments.all()

    return render(request, 'ericapp/blog_post_detail.html', {'post': post, 'comments': comments, 'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from.forms import SubscriptionForm, MailMessageForm
from.models import Subscription, MailMessage

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email is already subscribed
            if not Subscription.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.info(request, "Please enter a valid email address.")
        else:
            messages.error(request, "You are already subscribed.")
    return redirect('ericapp:index')  # Redirect to the homepage or another page

def mail_letter(request):
    # Get all emails as a list without using `django_pandas`
    mail_list = list(Subscription.objects.values_list('email', flat=True))
    print(mail_list)

    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',  # Enter your email here
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('ericapp:mail_letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'ericapp/mail_letter.html', context)


