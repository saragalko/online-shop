from catalog.models import Category, Product, Discount, Seller
from rest_framework.generics import ListAPIView
from catalog.serializers import CategorySerializer, ProductSerializer, DiscountSerializer, SellerSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class CategoryProductsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, category_id):
        queryset = Product.objects.filter(category__id=category_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (AllowAny, )


class DiscountProductsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, discount_id):
        queryset = Discount.objects.filter(category__id=discount_id)
        serializer = DiscountSerializer(queryset, many=True)
        return Response(serializer.data)


class SellerListView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (AllowAny, )


class SellerProductsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, seller_id):
        queryset = Seller.objects.filter(category__id=seller_id)
        serializer = SellerSerializer(queryset, many=True)
        return Response(serializer.data)
