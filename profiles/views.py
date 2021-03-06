from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from profiles.models import Profile

class ProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "profiles/profile.html"
    context_object_name = "profile"
    login_url = "account_login"

    def get_queryset(self):
        return self.request.user.profile
