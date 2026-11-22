# Telegram handle changed from @mohaka0975 to @mohakap (owner order 2026-11-22)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_profile_instagram_profile_telegram_channel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram',
            field=models.URLField(default='https://t.me/mohakap'),
        ),
    ]
