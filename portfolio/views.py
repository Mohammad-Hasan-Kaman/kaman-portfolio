from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import (Article, ContactMessage, CvLanguage, Education, Experience,
                     Profile, Project, Service, Skill, Testimonial)
from .translations import STRINGS


MARQUEE_TAGS = [
    'Python', 'Django', 'C#', '.NET', 'JavaScript', 'REST APIs', 'PyQt6', 'CustomTkinter',
    'WinForms', 'WebView2', 'SQLite', 'SQL', 'LLMs', 'OpenAI', 'Gemini', 'DeepSeek',
    'SSE Streaming', 'Tool Calling', 'TCP Sockets', 'AES / Fernet', 'bcrypt', 'Git',
    'nginx', 'gunicorn', 'Linux', 'Cloudflare Workers', 'KV', 'BIND9 DNS', 'HTML5', 'CSS3',
]


def _marquee_tags():
    """Admin-managed marquee tags; falls back to the defaults above."""
    from .models import MarqueeTag
    tags = list(MarqueeTag.objects.values_list('label', flat=True))
    return tags or MARQUEE_TAGS


def get_profile():
    return Profile.objects.first()


def _t(request):
    return STRINGS.get(request.LANGUAGE_CODE, STRINGS['en'])


def home(request):
    profile = get_profile()
    projects = Project.objects.all()
    context = {
        'profile': profile,
        'skills': Skill.objects.all(),
        'services': Service.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'featured_projects': projects.filter(featured=True)[:6],
        'other_projects': [p for p in projects if not p.featured][:6],
        'articles': Article.objects.filter(published=True)[:6],
        'marquee_tags': _marquee_tags(),
    }
    return render(request, 'portfolio/home.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    next_project = Project.objects.filter(id__gt=project.id).order_by('id').first()
    if next_project is None:
        next_project = Project.objects.exclude(id=project.id).order_by('id').first()
    context = {
        'profile': get_profile(),
        'project': project,
        'next_project': next_project,
    }
    return render(request, 'portfolio/project_detail.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, published=True)
    next_article = Article.objects.filter(published=True, id__gt=article.id).order_by('id').first()
    if next_article is None:
        next_article = Article.objects.filter(published=True).exclude(id=article.id).order_by('id').first()
    context = {
        'profile': get_profile(),
        'article': article,
        'next_article': next_article,
    }
    return render(request, 'portfolio/article_detail.html', context)


def cv_page(request):
    import os
    from django.conf import settings

    profile = get_profile()
    cv_pdf_url = None
    if profile and profile.cv_file:
        root, ext = os.path.splitext(profile.cv_file.name)
        lang_pdf = f'{root}_{request.LANGUAGE_CODE}{ext}'
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, lang_pdf)):
            cv_pdf_url = f'{settings.MEDIA_URL}{lang_pdf}'
        else:
            cv_pdf_url = profile.cv_file.url
    context = {
        'profile': profile,
        'skills': Skill.objects.all(),
        'projects': Project.objects.all()[:6],
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'cv_languages': CvLanguage.objects.all(),
        'cv_pdf_url': cv_pdf_url,
    }
    return render(request, 'portfolio/cv.html', context)


def cv_download(request):
    """Generate and serve a CV PDF in the requested language."""
    lang = request.GET.get('lang', request.LANGUAGE_CODE)
    if lang not in STRINGS:
        lang = 'en'
    from .cv_pdf import _CvPdf
    profile = get_profile()
    pdf = _CvPdf(lang=lang)
    content = pdf.build(profile, lang)
    filename = f"Mohammad_Hasan_Kaman_CV_{lang.upper()}.pdf"
    resp = HttpResponse(content, content_type='application/pdf')
    resp['Content-Disposition'] = f'attachment; filename="{filename}"'
    try:
        from . import analytics
        if not analytics.is_bot(request):
            analytics.record(request, resp, event='cv_download', path=f'/cv/download/{lang}/')
    except Exception:
        pass
    return resp


def contact_submit(request):
    from django.views.decorators.http import require_POST
    # Honeypot: the hidden "website" field must stay empty. Bots fill it.
    if (request.POST.get('website') or '').strip():
        return JsonResponse({'ok': True, 'msg': _t(request)['contact']['success']})

    name = (request.POST.get('name') or '').strip()
    email = (request.POST.get('email') or '').strip()
    subject = (request.POST.get('subject') or '').strip()
    message = (request.POST.get('message') or '').strip()

    if request.method != 'POST' or not all([name, email, subject, message]) or '@' not in email:
        return JsonResponse({'ok': False, 'msg': _t(request)['contact']['error']}, status=400)

    ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

    # analytics event
    try:
        from . import analytics
        from django.http import JsonResponse as _JR
        if not analytics.is_bot(request):
            analytics.record(request, _JR({'ok': True}), event='contact')
    except Exception:
        pass

    # Optional email notification (works automatically once EMAIL_* settings are configured)
    try:
        from django.core.mail import send_mail
        from django.conf import settings as s
        send_mail(
            f'[Portfolio] {subject}',
            f'From: {name} <{email}>\n\n{message}',
            s.DEFAULT_FROM_EMAIL,
            [s.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
    except Exception:
        pass

    return JsonResponse({'ok': True, 'msg': _t(request)['contact']['success']})
