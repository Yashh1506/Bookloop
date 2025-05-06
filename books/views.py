from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from . models import books
import os
from django.conf import settings
from django.contrib import messages

# Create your views here.
@login_required
def book_upload(request):
    
    if request.method == "POST":
        try:
            title = request.POST.get('title')
            coverimage = request.FILES.get('cover_image')
            additional_image1 = request.FILES.get('additional-image-1')
            additional_image2 = request.FILES.get('additional-image-2')
            additional_image3 = request.FILES.get('additional-image-3')
            author = request.POST.get('author')
            price = request.POST.get('price')
            condition = request.POST.get('condition')
            category = request.POST.get('category')
            language = request.POST.get('language')
            publisher = request.POST.get('publisher')
            description = request.POST.get('description')
            exchange_option = request.POST.get('exchange-option')
            location = request.POST.get('location')
            tags = request.POST.get('tags')
            user = request.user

            book = books.objects.create(
                book_title = title,
                user = user,
                coverimage = coverimage,
                additional_image1 = additional_image1,
                additional_image2 = additional_image2,
                additional_image3 = additional_image3,
                author = author,
                price = price,
                condition = condition,
                category = category,
                language = language,
                publisher = publisher,
                description = description,
                exchange_option = exchange_option,
                location = location,
                tags = tags
            )
            
            book.save()

            return redirect('book-details', book_id = book.book_id)
        except Exception as e:
           for image in [coverimage, additional_image1, additional_image2, additional_image3]:
                if image:
                    image_path = os.path.join(settings.MEDIA_ROOT, 'book_images', image.name)
                    if os.path.exists(image_path):
                        os.remove(image_path)
                print("Error while saving:", e)
    return render(request,'book-upload.html')

def book_details(request, book_id):
    book_qs = books.objects.filter(pk=book_id)
    all_books = books.objects.all()
    if book_qs.exists():
        book = book_qs.first()
        return render(request, 'book-details.html', {'book' : book, 'all_books':all_books})
    else:
        messages.error(request, "Book doesn't exist !!")
        return render(request, 'book-details.html')


def catalog(request):
    user = request.user
    all_books = books.objects.all()
    return render(request, 'catalog.html', {'all_books' : all_books, 'user' : user})