from django.shortcuts import render

chefsData = [
    {"id":1, "name":"Walter White", "profession": "Master Chef", "imgUrl":'img/chefs/chefs-1.jpg'},
    {"id":2, "name":"Sarah Jhonson", "profession": "Patissier", "imgUrl":'img/chefs/chefs-2.jpg'},
    {"id":3, "name":"William Anderson", "profession": "Cook", "imgUrl":'img/chefs/chefs-3.jpg'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def specials(request):
    return render(request, 'specials.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html', {"chefsData": chefsData})

def chef_detail(request, chef_id):
    chefData = chefsData[chef_id - 1]
    return render(request, 'chef_detail.html', {"chefData": chefData})

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')