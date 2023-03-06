from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')

# def index(request):
#     phone_objects = Phone.objects.all()
#     phones = [f'id: {c.id} модель: {c.name} цена:{c.price}' for c in phone_objects]
#     return HttpResponse('<br>'.join(phones) )

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
