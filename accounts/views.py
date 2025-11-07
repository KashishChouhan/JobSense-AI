from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .utils import get_model, embed_text

#signup
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("signup")

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        login(request, user)  # auto login after signup
        messages.success(request, "Signup successful! You are now logged in.")
        return redirect("/")  # redirect to home page or results

    return render(request, "signup.html")
#login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("/")  # home page
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")
#logout
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

def job_view(request):
    # Example job texts
    job_texts = ["Python developer", "Data Analyst", "Machine Learning Engineer"]

    try:
        embeddings = embed_text(job_texts)  # memory-safe CPU embedding
        embeddings_list = embeddings.tolist()  # convert for template display
    except Exception as e:
        messages.error(request, f"Error processing embeddings: {str(e)}")
        embeddings_list = []

    context = {
        "job_texts": job_texts,
        "embeddings": embeddings_list
    }
    return render(request, "job_view.html", context)
