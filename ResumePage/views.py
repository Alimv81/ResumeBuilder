from django.shortcuts import render, get_object_or_404, redirect

from ResumePage.forms import ResumeForm
from ResumePage.models import Resume


# Create your views here.
def home(request):
    return render(request, "ResumePage/index.html", {})


def resume_list(request):
    return render(request, "ResumePage/list.html", {})


def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    resume_form = ResumeForm(request.POST or None, instance=resume)
    return render(request, "ResumePage/detail.html", {"form": resume_form})


def resume_update(request, resume_id):
    pass


def resume_delete(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    resume.delete()
    return redirect("ResumePage:home")


def resume_new(request):
    if request.method == "POST":
        form = ResumeForm(request.POST or None)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            profile_summary = form.cleaned_data["profile_summary"]
            education = form.cleaned_data["education"]
            skills = form.cleaned_data["skills"]
            work_experience = form.cleaned_data["work_experience"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            resume = Resume(full_name=full_name, profile_summary=profile_summary,
                            education=education, skills=skills, work_experience=work_experience,
                            email=email, phone_number=phone_number)
            resume.save()
            return redirect("ResumePage:home")
        else:
            form.add_error(None, 'Invalid information')
            print(form.errors)
            return redirect("ResumePage:home")
    else:
        form = ResumeForm()
        return render(request, "ResumePage/create.html", {"form": form})
