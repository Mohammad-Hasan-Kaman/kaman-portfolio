from django.contrib import admin
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from django.utils.html import format_html

from .models import (Article, ContactMessage, CvLanguage, Education, Experience,
                     MarqueeTag, Profile, Project, Service, SiteText, Skill,
                     Testimonial, Visit)

now = timezone.now


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Analytics dashboard: summary cards + popular pages + referrers."""
    change_list_template = 'admin/portfolio/visit/dashboard.html'
    list_display = ('event', 'path', 'lang', 'device', 'referrer', 'created_at')
    list_filter = ('event', 'lang', 'device', 'referrer')
    search_fields = ('path', 'referrer')
    date_hierarchy = 'created_at'
    list_per_page = 100

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def changelist_view(self, request, extra_context=None):
        ctx = dict(extra_context or {})
        qs = self.get_queryset(request)
        today = now().replace(hour=0, minute=0, second=0, microsecond=0)
        week = today - timezone.timedelta(days=7)
        month = today - timezone.timedelta(days=30)

        def agg(queryset, field):
            rows = (queryset.annotate(day=TruncDate('created_at'))
                    .values(field).annotate(n=Count('id')).order_by('-n')[:12])
            return list(rows)

        def daily(queryset, days=14):
            start = today - timezone.timedelta(days=days - 1)
            rows = (queryset.filter(created_at__gte=start)
                    .annotate(day=TruncDate('created_at'))
                    .values('day').annotate(n=Count('id')).order_by('day'))
            by_day = {r['day']: r['n'] for r in rows}
            out, d = [], start.date()
            while d <= today.date():
                out.append((d, by_day.get(d, 0)))
                d += timezone.timedelta(days=1)
            return out

        ctx['cards'] = {
            'total': qs.count(),
            'today': qs.filter(created_at__gte=today).count(),
            'week': qs.filter(created_at__gte=week).count(),
            'month': qs.filter(created_at__gte=month).count(),
            'visitors': qs.values('session_key').distinct().count(),
            'cv': qs.filter(event='cv_download').count(),
            'contacts': qs.filter(event='contact').count(),
            'mobile_pct': (qs.filter(device='mobile').count() * 100 // max(qs.count(), 1)),
        }
        ctx['popular'] = agg(qs.filter(event='pageview'), 'path')
        ctx['referrers'] = agg(qs, 'referrer')
        ctx['langs'] = agg(qs, 'lang')
        ctx['devices'] = agg(qs, 'device')
        ctx['daily'] = daily(qs)
        ctx['max_daily'] = max((n for _, n in ctx['daily']), default=1) or 1
        ctx['recent'] = qs[:15]
        return super().changelist_view(request, ctx)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Names', {'fields': [('name_en', 'name_fa', 'name_ar')]}),
        ('Roles', {'fields': [('role_en', 'role_fa', 'role_ar')]}),
        ('Taglines', {'fields': ['tagline_en', 'tagline_fa', 'tagline_ar']}),
        ('About', {'fields': ['about_en', 'about_fa', 'about_ar']}),
        ('CV Summary', {'fields': ['summary_en', 'summary_fa', 'summary_ar'],
                        'description': 'Short professional summary shown at the top of the Resume page (falls back to About if empty).'}),
        ('Core Competencies', {'fields': ['core_competencies_en', 'core_competencies_fa', 'core_competencies_ar'],
                        'description': 'Core competency bullet points shown on the CV page (one per line).'}),
        ('Contact', {'fields': ['email', 'phone', ('location_en', 'location_fa', 'location_ar')]}),
        ('Social', {'fields': ['github', 'linkedin', 'twitter', 'telegram']}),
        ('Media', {'fields': ['avatar', 'cv_file']}),
        ('Counters', {'fields': ['years_experience', 'projects_completed', 'happy_clients']}),
    ]

    # obj=None: Django calls this with (request, obj) on the change page
    def has_add_permission(self, request, obj=None):
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'category', 'featured', 'order')
    list_editable = ('featured', 'order')
    list_filter = ('category', 'featured')
    prepopulated_fields = {'slug': ('title_en',)}
    search_fields = ('title_en', 'title_fa', 'title_ar', 'tech_stack')
    fieldsets = [
        (None, {'fields': [('title_en', 'title_fa', 'title_ar'), 'slug', ('category', 'icon')]}),
        ('Descriptions', {'fields': ['description_en', 'description_fa', 'description_ar']}),
        ('Details', {'fields': ['tech_stack', ('image', 'live_url', 'repo_url')]}),
        ('Visibility', {'fields': [('featured', 'order')]}),
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'published', 'order', 'created_at')
    list_editable = ('published', 'order')
    prepopulated_fields = {'slug': ('title_en',)}
    date_hierarchy = 'created_at'
    fieldsets = [
        (None, {'fields': [('title_en', 'title_fa', 'title_ar'), 'slug', ('icon', 'cover')]}),
        ('Excerpt (shown on card)', {'fields': ['excerpt_en', 'excerpt_fa', 'excerpt_ar']}),
        ('Full text', {'fields': ['body_en', 'body_fa', 'body_ar'],
                       'description': 'Separate paragraphs with a blank line. If a FA/AR body is left empty, the English body is shown.'}),
        ('Visibility', {'fields': [('published', 'order')]}),
    ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'level_en', 'icon', 'order')
    list_editable = ('tier', 'order')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'icon', 'order')
    list_editable = ('order',)
    fieldsets = [
        (None, {'fields': ['icon', ('title_en', 'title_fa', 'title_ar')]}),
        ('Descriptions', {'fields': ['description_en', 'description_fa', 'description_ar']}),
    ]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_en', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_editable = ('is_read',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'org_en', 'period_en', 'order')
    list_editable = ('order',)
    fieldsets = [
        (None, {'fields': [('title_en', 'title_fa', 'title_ar'), ('org_en', 'org_fa', 'org_ar'), ('period_en', 'period_fa', 'period_ar')]}),
        ('Description', {'fields': ['description_en', 'description_fa', 'description_ar']}),
    ]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_en', 'institution_en', 'period_en', 'order')
    list_editable = ('order',)
    fieldsets = [
        (None, {'fields': [('degree_en', 'degree_fa', 'degree_ar'), ('institution_en', 'institution_fa', 'institution_ar'), ('period_en', 'period_fa', 'period_ar')]}),
        ('Details (one per line)', {'fields': ['details_en', 'details_fa', 'details_ar']}),
    ]


@admin.register(CvLanguage)
class CvLanguageAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'level_en', 'order')
    list_editable = ('level_en', 'order')
    fields = [('name_en', 'name_fa', 'name_ar'), ('level_en', 'level_fa', 'level_ar'), 'order']


@admin.register(SiteText)
class SiteTextAdmin(admin.ModelAdmin):
    """Every UI string on the site — search by key or label."""
    list_display = ('key', 'label', 'value_en', 'value_fa')
    list_display_links = ('key',)
    search_fields = ('key', 'label', 'value_en', 'value_fa', 'value_ar')
    list_per_page = 50
    fieldsets = [
        (None, {'fields': ('key', 'label'),
                'description': 'Key is fixed (dot notation like hero.greeting). '
                               'Leave FA/AR empty to fall back to English.'}),
        ('Values', {'fields': [('value_en', 'value_fa', 'value_ar')]}),
    ]

    def has_add_permission(self, request):
        # Keys must mirror template variables; add new ones via the seed
        # command or by editing the template + translations first.
        return False

    def has_delete_permission(self, request):
        return False


@admin.register(MarqueeTag)
class MarqueeTagAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')
    list_editable = ('order',)
    search_fields = ('label',)
