from django.shortcuts import render, redirect
from .models import Job
from .utils import extract_skills, embed_text, cosine_similarity, cluster_jobs, get_resource
from django.contrib.auth.decorators import login_required
from .utils import get_model, extract_skills, embed_text, cosine_similarity

def recommend_jobs(request):
    model = get_model()   #  Safe lazy load

def home(request):
    """
    Home page where user can enter skills.
    """
    if request.method == 'POST':
        skills_text = request.POST.get('skills_text', '')
        request.session['user_skills_text'] = skills_text
        return redirect('results')
    return render(request, 'home.html')

def results(request):
    """
    Show job recommendations based on user-entered skills.
    """
    skills_text = request.session.get('user_skills_text', '')
    if not skills_text:
        return redirect('home')

    # Step 1: Convert user skills to embedding
    user_skills = extract_skills(skills_text)
    user_embedding = embed_text(skills_text)

    # Step 2: Generate recommendations
    jobs = Job.objects.all()
    recommendations = []
    for job in jobs:
        job_embedding = embed_text(job.skills)
        similarity = round(100 * cosine_similarity(user_embedding, job_embedding), 2)

        job_skills = extract_skills(job.skills)
        missing = sorted(list(job_skills - user_skills))
        have = sorted(list(user_skills & job_skills))

        recommendations.append({
            'job': job,
            'score': similarity,
            'missing': [(s, get_resource(s)) for s in missing],
            'have': have,
        })

    # Step 3: Sort by similarity score (highest first)
    recommendations.sort(key=lambda x: x['score'], reverse=True)

    # Optional: Cluster jobs (for grouping similar ones)
    clustered_jobs = cluster_jobs(jobs)

    return render(request, 'results.html', {
        'skills_text': skills_text,
        'user_skills': user_skills,
        'recommendations': recommendations,
        'clustered_jobs': clustered_jobs,
    })

def all_jobs(request):
    """
    Display all jobs stored in the database.
    """
    jobs = Job.objects.all()
    return render(request, 'all_jobs.html', {'jobs': jobs})
