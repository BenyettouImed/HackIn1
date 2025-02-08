from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from dj_next_auth.authentication import JWTAuthentication  # adjust based on your project name
from .serializers import EventSerializer  # make sure you have this serializer
from .models import Event

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_event(request):
    try:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {'detail': serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {'detail': str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )