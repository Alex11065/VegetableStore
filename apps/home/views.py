from django.shortcuts import render
from django.views import View


class IndexShopView(View):
    def get(self, requesst):
        context = {'data': [{'name': 'Болгарский перец',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-1.jpg'},
                            {'name': 'Клубника',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-2.jpg'},
                            {'name': 'Зеленая фасоль',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-3.jpg'},
                            {'name': 'Фиолетовая капуста',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-4.jpg'},
                            {'name': 'Томаты',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-5.jpg'},
                            {'name': 'Брокколи',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-6.jpg'},
                            {'name': 'Морковь',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-7.jpg'},
                            {'name': 'Фруктовый сок',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-8.jpg'},
                            ]
                   }
        return render(requesst, 'home/index.html', context)


class AboutSopView(View):
    def get(self, request):
        return render(request, 'home/about.html')


class ContactSopView(View):
    def get(self, request):
        return render(request, 'home/contact.html')
