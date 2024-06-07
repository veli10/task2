from django.shortcuts import render, redirect, get_object_or_404
from .models import FormModel
from .forms import ResumeForm

# Create your views here.
def create__profile__view(request):
    form = ResumeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('all-resumes')
    
    context = {'form': form}
    return render(request, 'create-resume.html', context)

def profile__detail__view(request, id):
    resume = get_object_or_404(FormModel, id=id)
    return render(request, 'resume.html', {'resume': resume})

def all__resumes__view(request):
    resumes = FormModel.objects.all()
    return render(request, 'all-resumes.html', {"resumes": resumes})