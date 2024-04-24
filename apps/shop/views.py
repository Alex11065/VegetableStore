from django.shortcuts import render
from django.views import View


class ShopView(View):
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
                            {'name': 'Лук',
                             'discount': None,
                             'price_before': 100.00,
                             'url': 'store/images/product-9.jpg'},
                            {'name': 'Яблоки',
                             'discount': None,
                             'price_before': 110.00,
                             'url': 'store/images/product-10.jpg'},
                            {'name': 'Чеснок',
                             'discount': None,
                             'price_before': 90.00,
                             'url': 'store/images/product-11.jpg'},
                            {'name': 'Перец чили',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-12.jpg'},
                            ]
                   }
        return render(requesst, 'shop/shop.html', context)


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'shop/product-single.html')
