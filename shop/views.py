from django.shortcuts import render


def home(request):
    categories = [
        {'name': 'Elektronika', 'emoji': '📱'},
        {'name': 'Ev və mətbəx', 'emoji': '🏠'},
        {'name': 'Geyim', 'emoji': '👕'},
        {'name': 'Kitablar', 'emoji': '📚'},
        {'name': 'Oyunlar', 'emoji': '🎮'},
        {'name': 'İdman', 'emoji': '⚽'},
    ]
    products = [
        {'name': 'Simsiz qulaqlıq', 'emoji': '🎧', 'price': 49.90, 'stars': '★★★★☆'},
        {'name': 'Smart saat', 'emoji': '⌚', 'price': 89.00, 'stars': '★★★★★'},
        {'name': 'Noutbuk çantası', 'emoji': '💼', 'price': 34.50, 'stars': '★★★★☆'},
        {'name': 'Kamera', 'emoji': '📷', 'price': 249.00, 'stars': '★★★★☆'},
        {'name': 'İdman ayaqqabısı', 'emoji': '👟', 'price': 64.99, 'stars': '★★★★★'},
        {'name': 'Qəhvə maşını', 'emoji': '☕', 'price': 119.00, 'stars': '★★★☆☆'},
        {'name': 'Günəş eynəyi', 'emoji': '🕶️', 'price': 27.00, 'stars': '★★★★☆'},
        {'name': 'Bluetooth dinamik', 'emoji': '🔊', 'price': 39.90, 'stars': '★★★★☆'},
    ]
    return render(request, 'shop/index.html', {
        'categories': categories,
        'products': products,
    })
