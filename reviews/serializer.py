from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review Object."""
    id = serializers.IntegerField(read_only=True)
    rate = serializers.IntegerField(required=False)
    feedback = serializers.CharField(required=False)

    class Meta:
        """Meta info."""
        model = Review
        fields = '__all__'
