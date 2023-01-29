from django.shortcuts import render
from rest_framework import viewsets
from reviews.serializer import ReviewSerializer
from reviews.models import Review
from accounts import permissions as user_permissions


class ReviewView(viewsets.ModelViewSet):
    """View for review."""
    permission_classes = (user_permissions.IsAuthenticated,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
