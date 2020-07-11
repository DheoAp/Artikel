from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView, CreateView


# untuk Auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ModelArtikel
from .forms import FormArtikel
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def cv(request):
    context ={}
    return render(request, 'cv.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')

        user = authenticate(request, username=username_, password=password_)

        if user is not None:
            login(request, user)
            return redirect('manage')
        else:
            messages.info(request, 'Username atau Password salah!')
    
    return render(request,'artikel/login.html')

def LogoutPage(request) :
    logout(request)
    return redirect('login')


class Artikel(ListView):
    model = ModelArtikel
    template_name = 'artikel/index_artikel.html'
    context_object_name = "Post"
    ordering = ['-publish']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        list_kategori = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'Kategori':list_kategori})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class KategoriArtikel(ListView):
    model = ModelArtikel
    template_name = 'artikel/kategori_artikel.html'
    context_object_name = "Kategori_artikel"
    ordering = ['-publish']
    paginate_by = 2

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_kategori = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'Kategori':list_kategori})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class DetailArtikel(DetailView):
    model = ModelArtikel
    template_name = 'artikel/detail_artikel.html'
    context_object_name = "Detail"


# Manage Artikel gunakan Function Base View
@login_required(login_url='login')
def manage(request):
    data_artikel = ModelArtikel.objects.all()
    context = {
        'Data':data_artikel,
    }
    return render(request,'artikel/manage/manage.html',context)

@login_required(login_url='login')
def create(request):
    artikel_form = FormArtikel(request.POST or None)

    if request.method == "POST":
        artikel_form = FormArtikel(request.POST, request.FILES) 
        if artikel_form.is_valid():
            artikel_form.save()       
            return redirect('manage')
    else:
        artikel_form = FormArtikel()
        
    return render(request,'artikel/manage/manage_create.html', {'form_data':artikel_form})

@login_required(login_url='login')
def update(request, update_id):
    updateData = ModelArtikel.objects.get(id=update_id)
    Data = FormArtikel(instance=updateData)
    if request.method == "POST":
        Data = FormArtikel(data=request.POST, files=request.FILES, instance=updateData)
        if Data.is_valid():
            Data.save()
            return redirect('manage')
    else:
        Data = FormArtikel(instance=updateData)
    return render(request, 'artikel/manage/manage_update.html', {'Update':Data})

@login_required(login_url='login')
def delete(request, delete_id):
    artikel = ModelArtikel.objects.get(id=delete_id)
    if request.method == "POST":
        artikel.delete()
        return redirect('manage')    
    
    return render(request, 'artikel/manage/manage_delete.html', {'Data':artikel})

@login_required(login_url='login')
def detail(request,detail_id):
    detailData = ModelArtikel.objects.get(id=detail_id)
    
    return render(request, 'artikel/manage/manage_detail.html', {'Detail':detailData})