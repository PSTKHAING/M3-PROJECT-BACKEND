from django.shortcuts import render
from api.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

# ========================= CATEGORY CRUD =========================

@api_view(['GET'])
@permission_classes([AllowAny])
def CategoryList(request):
    try:
        categories = CategoryModel.objects.all().order_by('-created_at')
        return Response({
            'success':True,
            'message': 'Categories retrieved successfully',
            'categories': [
                {   'id': category.id,
                    'name' : category.name,
                    'created_at': category.created_at,
                    'updated_at': category.updated_at,
                }
                for category in categories
            ]
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'message':f'Categories retrieved failed {str(e)}'
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def CategoryCreate(request):
    try:
        name = request.data.get('name')
        if not name:
            return Response({
                "success": False,
                "message": "Please fill all fields"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        category = CategoryModel.objects.create(
            name=name
        )
        category.save()
        return Response({
            'success':True,
            'message':"Category created successfully",
            'category':{
                "id": category.id,
                "name":category.name,
                "created_at":category.created_at,
                "updated_at":category.updated_at
            }
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'message': f'Category created failed {str(e)}'
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def CategoryUpdate(request,pk):
    try:
        category = CategoryModel.objects.get(id=pk)
        category.name = request.data.get('name')
        category.save()
        return Response({
            'success':True,
            'message': 'Category updated successfully',
            'category':{
                "id": category.id,
                "name":category.name,
                "created_at":category.created_at,
                "updated_at":category.updated_at
            }
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'message': f'Category updated failed {str(e)}'
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def CategoryDelete(request,pk):
    try:
        category = CategoryModel.objects.get(id = pk)
        category.delete()
        return Response({
            'success':True,
            'message': 'Category deleted successfully'
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'message': f'Category deleted failed {str(e)}'
        },status=status.HTTP_400_BAD_REQUEST)
    
# ========================= PRODUCT CRUD =========================

@api_view(['GET'])
@permission_classes([AllowAny])
def ProductList(request):
    try:
        products = ProductModel.objects.all().order_by('-created_at')
        return Response({
            'success':True,
            'message':"Product retrieved successfully",
            "products":[
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image': product.image.url,
                    'quantity': product.quantity,
                    'category':{
                        'id': product.category.id,
                        'name': product.category.name,
                    },
                    'created_at': product.created_at,
                    'updated_at': product.updated_at
                }
                for product in products
            ]
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'message': f'Product retrieved failed {str(e)}'
        },status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def ProductCreate(request):
    try:
        name = request.data.get('name')
        price = request.data.get('price')
        image = request.FILES.get('image')
        quantity = request.data.get('quantity')
        category = request.data.get('category')

        if not name or not price or not image or not quantity or not category:
            return Response({
                'success' : False,
                'message': 'Please fill all fields'
            },status=status.HTTP_400_BAD_REQUEST)
        
        product = ProductModel.objects.create(
            name = name,
            price = price,
            image = image,
            quantity = quantity,
            category_id = category
        )
        product.save()
        return Response({
            'success' : True,
            'message': 'Product created successfully',
            'product' : {
                "id" : product.id,
                "name": product.name,
                "price" : product.price,
                "image" : product.image.url,
                "quantity" : product.quantity,
                "category" : {
                    "id": product.category.id,
                    "name" : product.category.name,
                },
                "created_at" : product.created_at,
                "updated_at": product.updated_at
            }
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "success" : False,
            "message" : f"Product created failed {str(e)}"
        },status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([AllowAny])
def ProductUpdate(request,pk):
    try:
        product = ProductModel.objects.get(id=pk)
        product.name = request.data.get('name')
        product.price = request.data.get('price')
        if request.FILES.get('image'):
            product.image.delete()
            product.image = request.FILES.get('image')
        product.quantity = request.data.get('quantity')
        product.category_id = request.data.get('category')
        product.save()
        return Response({
            'success' : True,
            'message': 'Product updated successfully',
            'product' : {
                "id" : product.id,
                "name": product.name,
                "price" : product.price,
                "image" : product.image.url,
                "quantity" : product.quantity,
                "category" : {
                    "id": product.category_id,
                    "name" : product.category.name,
                },
                "created_at" : product.created_at,
                "updated_at": product.updated_at
            }
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "success" : False,
            "message" : f"Product updated failed {str(e)}"
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def ProductDelete(request,pk):
    try:
        product = ProductModel.objects.get(id = pk)
        if product.image:
            product.image.delete()
        product.delete()
        return Response({
            'success':True,
            'message': 'Product deleted successfully'
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'message': f'Product deleted failed {str(e)}'
        },status=status.HTTP_400_BAD_REQUEST)