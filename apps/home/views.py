from django.shortcuts import render
from django.views import View


class IndexShopView(View):
    def get(self, requesst):
        context = {'data': [{'name': 'Bell Peper',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-1.jpg'}
                            ]
                   }
        return render(requesst, 'home/index.html', context)


class AboutSopView(View):
    def get(self, request):
        return render(request, 'home/about.html')


class ContactSopView(View):
    def get(self, request):
        return render(request, 'home/contact.html')
