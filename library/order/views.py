from django.shortcuts import render, redirect

from authentication.models import CustomUser
from book.models import Book
from order.forms import OrderForm
from order.models import Order
import datetime

from rest_framework import viewsets
from .serializers import OrderSerializer
from django.db.models import Q


# for API
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# def index(request):  # название функции должно совпадать folder/file.html
#     data = {'title': 'ORDER'}
#
#     return render(request, 'order/index.html', context=data)

def orders_find(request):
    context = {'orders': Order.objects.all(), "search_text": ""}
    if request.POST:
        search_name = request.POST['search_name']
        search_id = request.POST['search_id']

        if search_name:
            user = CustomUser.objects.filter(email__icontains=search_name)
            orders = Order.objects.filter(user__in=user)
            context = {'orders': orders, "search_text": search_name}
        if search_id:
            orders = Order.objects.filter(id=search_id)
            context = {'orders': orders, "search_text": search_id}

    return context


def orders(request):
    context = {"search_text": "Login as librarian to see orders"}
    if request.user.id:
        if request.user.role == 1:
            context = orders_find(request)

    return render(request, 'order/orders_list.html', context)


def order_item(request, order_id):
    order = Order.objects.get(pk=order_id)

    context = {'user': order.user, 'book': order.book,
               # 'created_at': order.created_at,
               # 'end_at': order.end_at,
               # 'plated_end_at': order.plated_end_at,
               "order": order
               }
    # context={"orders": order}
    return render(request, 'order/order_details.html', context)


def delete_order(request, pk):
    Order.delete_by_id(pk)
    return redirect('/order/')


def close_order(request, pk):
    order = Order.get_by_id(pk)

    order.end_at = datetime.datetime.now()
    order.save()
    return redirect('/orders/')


# def create_order(request):
#     # context = {}
#     error = ''
#     new_order = Order()
#     context = {}
#     if request.method == 'POST':
#         userid = request.POST['userid']
#         user = CustomUser.get_by_id(userid)
#         bookid = str(request.POST.get('bookid', False))
#         book = Book.get_by_id(bookid)
#         data_time = request.POST['data_time']
#         new_order = new_order.create(user, book, data_time)
#         order_id = str(new_order.id)
#         return redirect('/orders/orders/' + order_id)
#
#     context = {'order': new_order, 'books': Book.objects.all(), 'error': error}
#     return render(request, 'order/create_order.html', context)
#     # return render(request, 'order/orders_list.html', context)


def add_order(request, order_id=0):
    if request.method == 'GET':
        if order_id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=order_id)
            form = OrderForm(instance=order)
        return render(request, 'order/add_order.html', {'form': form})
    else:
        if order_id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=order_id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(f'/orders/')
        return redirect(f'/orders/orders/{order_id}')
