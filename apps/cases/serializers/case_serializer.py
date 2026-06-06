from rest_framework import serializers
from apps.cases.models.case_study import CaseStudy


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = '__all__'
