from django.http import JsonResponse
from ..serializers import BookSerializer
from ..models import Book
from ..elastic.document import BookDocument


class BookService:
    def get_all_books():
        # book = Book(
        #     title = "AHAP",
        #     author = "BILL",
        #     content = "Wayyooo"
        # )
        # book.save()
        
        bks = BookDocument.search().query("match", title="AHAP")
        for hit in bks:
            print("Book title : {}, author {}".format(hit.title, hit.author))
        return "bks"

        books = Book.objects.all()
        response = BookSerializer(books, many=True)
        return response.data

    def get_one_book(id):
        try:
            book = Book.objects.get(pk=id)
            response = BookSerializer(book)
            return response.data, 200
        except:
            return "Book with that id does not exist", 400

    def create_book(request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data, 201
        return serializer.errors, 400

    def update_book(request, id):
        try:
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(instance=book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return serializer.data, 200
            return serializer.errors, 400
        except:
            return "Book with that id does not exist", 400

    def delete_book(id):
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return "Deleted Successfully", 200
        except:
            return "Book with that id does not exist", 400
