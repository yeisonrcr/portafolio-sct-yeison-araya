from apps.contact.models.contact_message import ContactMessage


class ContactService:

    @staticmethod
    def save_message(form, request):
        message = form.save(commit=False)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            message.ip_address = x_forwarded_for.split(',')[0].strip()
        else:
            message.ip_address = request.META.get('REMOTE_ADDR')
        message.save()
        return message

    @staticmethod
    def get_new_messages():
        return ContactMessage.objects.filter(status='new').order_by('-created_at')
