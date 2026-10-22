"""Align the testimonial heading with the real content.

The two testimonial cards are feedback from people the author worked with,
not client endorsements, so the heading must not imply clients.
"""
from django.db import migrations

VALUES = {
    'testimonials.title': {
        'en': 'Feedback & Collaborators',
        'fa': 'بازخورد و همکاران',
        'ar': 'آراء وتعاون',
    },
    'testimonials.label': {
        'en': 'Feedback',
        'fa': 'بازخورد',
        'ar': 'آراء',
    },
}


def apply(apps, schema_editor):
    SiteText = apps.get_model('portfolio', 'SiteText')
    for key, values in VALUES.items():
        obj, _ = SiteText.objects.get_or_create(
            key=key, defaults={'label': key.split('.')[0]})
        obj.value_en = values['en']
        obj.value_fa = values['fa']
        obj.value_ar = values['ar']
        obj.save()


def revert(apps, schema_editor):
    SiteText = apps.get_model('portfolio', 'SiteText')
    SiteText.objects.filter(key__in=VALUES).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0009_alter_profile_happy_clients_and_more'),
    ]

    operations = [
        migrations.RunPython(apply, revert),
    ]
