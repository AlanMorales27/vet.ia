from rest_framework import serializers

from ia_process.models import review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'