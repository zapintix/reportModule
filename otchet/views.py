from rest_framework import generics
from otchet.models import Report
from otchet.serializers import ReportSerializer


class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save()
