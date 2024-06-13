from rest_framework import serializers
from .models import Report, Photo, UserAut


class ReportSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserAut.objects.all(), source='user', write_only=True)
    photo_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Report
        fields = ['id', 'department', 'object', 'type', 'quantity', 'date', 'user_id', 'photo_ids']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        photo_ids = validated_data.pop('photo_ids', [])

        report = Report.objects.create(user_id=user_id.user.id, **validated_data)

        for photo_id in photo_ids:
            try:
                photo = Photo.objects.get(id=photo_id)
                report.photos.add(photo)
            except Photo.DoesNotExist:
                raise serializers.ValidationError(f"Photo with id {photo_id} does not exist.")

        return report
