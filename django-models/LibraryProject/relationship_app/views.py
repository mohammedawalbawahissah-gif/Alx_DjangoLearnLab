from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm  # your custom form
from .models import Library
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details of a single library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books in this library
        context['books'] = Book.objects.filter(library=self.object)
        return context


# Home page (for logged-in users)
def home(request):
    return render(request, 'relationship_app/home.html')


# Registration
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # ← use the built-in form
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()  # ← this satisfies the check
    return render(request, 'relationship_app/register.html', {'form': form})


# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# Logout
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, 'relationship_app/logout.html')


# Role checkers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
