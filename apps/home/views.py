from django.shortcuts import render
from django.views import View


class IndexShopView(View):
    def get(self, requesst):
        return render(requesst, 'home/index.html')


class AboutSopView(View):
    def get(self, request):
        return render(request, 'home/about.html')


class ContactSopView(View):
    def get(self, request):
        return render(request, 'home/contact.html')
