from django.shortcuts import render
from django.views import View


class IndexShopView(View):

    def get(self, requesst):
        return render(requesst, 'home/index.html')
