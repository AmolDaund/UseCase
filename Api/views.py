from django.shortcuts import render
from django.views import View
from Api.forms import MyForm
from .models import Data
import os
from django.conf import settings
import PyPDF2


class HomeView(View):

    def get(self, request):
        form = MyForm()
        return render(request, 'Api/home.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST, request.FILES)
        content = ''
        if form.is_valid():
            uploadfile = Data(file=request.FILES["file"])
            uploadfile.save()
            with open(os.path.join(settings.MEDIA_ROOT,
                                   f"{uploadfile.file}"), 'rb') as f:
                pdReader = PyPDF2.PdfReader(f)
                # print number of pages
                print(pdReader.pages)

                # create page object
                page_obj = pdReader.pages[0]

                # using page object extract text
                # print(page_obj.extract_text())

                content = page_obj.extract_text()
                # print(content)
            form = MyForm()
            return render(request, 'Api/home.html', {'form': form, 'content': content})

        return render(request, 'Api/home.html', {'form': form})


