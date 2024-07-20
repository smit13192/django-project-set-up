from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer


@api_view(["GET"])
def getItem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response({"statusCode": 200, "success": True, "data": serializer.data})


@api_view(["POST"])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"statusCode": 200, "success": True, "message": "Item add successfully" , "data": serializer.data})
    else:
        return Response({"statusCode": 400, "success": False, "message": "Item not added"}, status=400)
