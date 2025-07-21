from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # 👈 Yangi maydon

    def __str__(self):
        status = "✅" if self.is_read else "📩"
        return f"{status} {self.name} - {self.phone_number}"
