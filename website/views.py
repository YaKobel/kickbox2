from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News



def home(request):
	return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['kickboxua@gmail.com'],  # To Email
            )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'feder.html', {})


# def blog(request):
#     return render(request, 'blog.html', {})


def blog(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog.html', data)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'news_confirm_delete.html'


    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


class ShowNewsView(ListView):
    model = News
    template_name = 'blog.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5


    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'страница блога'
        return ctx

class UserAllNewsView(ListView):
    model = News
    template_name = 'user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')


    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] = f"Все статьи от пользовотеля {self.kwargs.get('username')}"
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'text']
    template_name = 'news_form.html'

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'text']
    # template_name = 'news_form.html'

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)




def service(request):
    return render(request, 'sport.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        # send an email
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Day: " + your_date + " Message: " + your_message

        send_mail(
            'Appointment Request',  # subject
            appointment,  # message
            your_email,  # from email
            ['kickboxua@gmail.com'],  # To Email
        )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})

def pricing_screen_view(request):
    print(request.headers)
    return render(request, "feder.html")