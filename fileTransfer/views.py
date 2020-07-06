from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.core.signing import BadSignature
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FileForm
from .models import File

# Class based view implementation
class Home(TemplateView):
    template_name = 'fileTransfer/home.html'

class FileUpload(LoginRequiredMixin, CreateView):
    model = File
    template_name = 'fileTransfer/upload.html'
    form_class = FileForm
    success_url = reverse_lazy('file_transfer:file_list')

class FileList(LoginRequiredMixin, ListView):
    model = File
    template_name = 'fileTransfer/file_list.html'
    context_object_name = 'files'

class SingleFile(LoginRequiredMixin, View):
    model = File
    template_name = 'fileTransfer/single_file.html'

    def get(self, request, signed_pk):
        try:
            pk = File.signer.unsign(signed_pk)
            single_file = File.objects.get(pk=pk)
        except (BadSignature, File.DoesNotExist):
            raise Http404('File doesn\'t exist.')

        return render(request, self.template_name, { 'single_file' : single_file })

    def post(self, request):
        pass

class DeleteFile(LoginRequiredMixin, DeleteView):
    model = File
    success_url = reverse_lazy('file_transfer:file_list')

class SignUp(View):
    form = UserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, { 'form' : form })
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('file_transfer:login')
    
        return render(request, self.template_name, { 'form' : form })

# Function based view implementation

# Local file upload without reference in database
# def file_upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file) # filename will auto-change if same file uploaded
#         url = fs.url(name)
#     return render(request, 'upload.html')

# File upload using form
# def file_upload(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('file_transfer:files_list')
#         else:
#             form = FileForm()
#     return render(request, 'upload.html', { 'form' : form })

# def file_list(request):
#     files = File.objects.all()
#     return render(request, 'fileTransfer/file_list.html', { 'files' : files })