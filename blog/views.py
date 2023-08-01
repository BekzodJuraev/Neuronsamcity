from .models import Post,News,Teacher,About,Feedback,Category
from .forms import Register
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView

from django.db.models import F
from django.core.mail import send_mail
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = Register()
    return render(request, 'register.html', {"form": form})



class Home(ListView):
    model = Teacher
    template_name = 'index.html'
    context_object_name = 'teacher'
    paginate_by = 4
    extra_context={'title':'NEURON'}



    def get_context_data(self, *args, **kwargs):
     context = super().get_context_data(*args, **kwargs)
     context['news'] = News.objects.all()
     context['post'] = Post.objects.all()
     context['feedback'] = Feedback.objects.all()

     return context


class About(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'
    paginate_by=1
    extra_context = {'title': 'О нас'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['feedback'] = Feedback.objects.all()
        return context









class Contact(TemplateView):
    template_name = 'contact.html'
    extra_context = {'title': 'Контакты'}


class PostsByCategory(ListView):

    template_name = 'category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

class GetPost(DetailView):
    model = Post
    template_name = 'single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context







