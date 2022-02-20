from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort', None)
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')

    context = {'phones':  phones}
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]

    context = {'phone': phone}

    return render(request, template, context)