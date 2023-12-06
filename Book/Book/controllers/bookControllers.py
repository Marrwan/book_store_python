from ..services.bookService import BookService
from rest_framework.views import APIView, Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BookListCreate(ListCreateAPIView):
    def get_queryset(self):
        return BookService.get_all_books()

    def get(self, id):
        result = BookService.get_all_books()
        return Response({"data": result}, status=200)

    @staticmethod
    @csrf_exempt
    def create(request):
        data, status = BookService.create_book(request)
        return Response({"data": data}, status)


class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return BookService.get_all_books()

    def get(self, request, id):
        data, status = BookService.get_one_book(id)
        return Response({"data": data}, status)

    def patch(self, request, id):
        data, status = BookService.update_book(request, id)
        return Response({"data": data}, status)

    def delete(self, request, id):
        data, status = BookService.delete_book(id)
        return Response({"data": data}, status)
