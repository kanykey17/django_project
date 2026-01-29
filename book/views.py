from django.http import HttpResponse

def quote(request):
    return HttpResponse(
        "«Книга — это мечта, которую держишь в руках». — Нил Гейман"
    )
