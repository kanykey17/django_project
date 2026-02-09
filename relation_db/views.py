from django.shortcuts import render
from .models import Registration

def results_view(request):
    registrations = Registration.objects.select_related('person', 'tour').prefetch_related('reviews', 'person__categories')
    return render(request, 'relation_db/results.html', {'registrations': registrations})
