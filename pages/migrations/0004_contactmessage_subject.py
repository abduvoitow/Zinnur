from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_contactmessage_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ] 