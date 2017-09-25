from django.shortcuts import render

# Create your views here.
def access_doc(request):
	return render(request, 'access_doc.html')

def view_pdf_cae(request):
	return render(request, 'view_pdf_cae.html')
