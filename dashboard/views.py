from django.shortcuts import render
from tablib import Dataset
from django.core.paginator import Paginator
from django.db.models import Sum
from .resource import BookResource
from .models import Book

# Create your views here.

def upload(request):
    if request.method == 'POST':
        book_resource = BookResource()
        dataset = Dataset()
        new_books = request.FILES['myfile']

        imported_data = dataset.load(new_books.read(), format='xlsx')
        result = book_resource.import_data(imported_data, dry_run=True)

        if result.has_errors():
            # Print the errors to the console
            print(result.errors)
        else:
            print("Data is valid, ready to be imported")
            book_resource.import_data(imported_data, dry_run=False)
            for row_result in result:
                if row_result.instance:
                    value = Book(
                        row_result.instance.id,
                        row_result.instance.title,
                        row_result.instance.subtitle,
                        row_result.instance.authors,
                        row_result.instance.publisher,
                        row_result.instance.published_date,
                        row_result.instance.category,
                        row_result.instance.distribution_expense
                    )
                    value.save()
            print('Data imported')
        print(result.total_rows)

    return render(request, 'upload.html', {})

def home(request):
    return render(request, 'home.html', {})

from django.shortcuts import render
from .models import Book

def book_tracker(request):
    books_list = Book.objects.all().order_by('published_date')
    paginator = Paginator(books_list, 20)

    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'book.html', {'books': books})

def expense_analysis(request):
    expenses = Book.objects.all()
    total_expense = expenses.aggregate(Sum('distribution_expense'))['distribution_expense__sum']
    category_total = list(expenses.values('category').annotate(total=Sum('distribution_expense')))
    context = {
        'expenses': expenses,
        'total_expense': total_expense,
        'category_total': category_total,
    }
    return render(request, 'expense.html', context)
