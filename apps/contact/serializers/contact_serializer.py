from rest_framework import serializers
from apps.contact.models.contact_message import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'company', 'subject', 'message']
