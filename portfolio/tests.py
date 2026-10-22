"""Content-integrity tests.

These guard the claims the site makes about the author's real work:
the project list, the experience counters and the absence of stale
or unverifiable marketing text. They run against the seeded database
created by ``manage.py seed_data``.
"""
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from portfolio.models import (
    Article,
    Experience,
    MarqueeTag,
    Profile,
    Project,
    Service,
    SiteText,
    Skill,
)

# The twelve public project repositories, in display order.
EXPECTED_PROJECTS = [
    'kaman-ai-translator',
    'agent-stream-doctor',
    'ai-counseling-widget',
    'ai-counseling-bot',
    'kaman-portfolio',
    'kaman-messenger',
    'dr-kaman-site',
    'planikaa-portal',
    'kaman-ai-chat',
    'quran-group-bot',
    'youtube-downloader',
    'kaman-web-browser',
]

# Claims that were never backed by the real projects and must not come back.
STALE_CLAIMS = [
    'bunifu',
    'google cloud tts',
    'exam analysis',
    '3+ years',
    'happy clients',
    'fluent, professional',
]


class SeededTestCase(TestCase):
    """Base case that loads the real seeded content into the test database.

    The site content lives in the database, so the tests have to run
    against exactly what ``manage.py seed_data`` produces.
    """

    @classmethod
    def setUpTestData(cls):
        call_command('seed_data', verbosity=0)
        call_command('seed_site_text', verbosity=0)


class ProjectListTests(SeededTestCase):
    def test_exactly_twelve_projects(self):
        self.assertEqual(Project.objects.count(), len(EXPECTED_PROJECTS))

    def test_slugs_and_order_match_the_public_repositories(self):
        slugs = list(
            Project.objects.order_by('order', 'id').values_list('slug', flat=True)
        )
        self.assertEqual(slugs, EXPECTED_PROJECTS)

    def test_every_project_links_to_its_repository(self):
        for project in Project.objects.all():
            self.assertTrue(
                project.repo_url.startswith('https://github.com/Mohammad-Hasan-Kaman/'),
                f'{project.slug} has no public repository link',
            )

    def test_six_projects_are_featured(self):
        self.assertEqual(Project.objects.filter(featured=True).count(), 6)

    def test_every_project_has_all_three_languages(self):
        for project in Project.objects.all():
            for field in ('title_en', 'title_fa', 'title_ar',
                          'description_en', 'description_fa', 'description_ar'):
                self.assertTrue(
                    getattr(project, field).strip(),
                    f'{project.slug} is missing {field}',
                )


class ProfileCounterTests(SeededTestCase):
    def setUp(self):
        self.profile = Profile.objects.first()
        self.assertIsNotNone(self.profile)

    def test_years_of_experience_is_four(self):
        self.assertEqual(self.profile.years_experience, 4)

    def test_projects_completed_matches_the_project_count(self):
        self.assertEqual(self.profile.projects_completed, Project.objects.count())

    def test_no_invented_client_count(self):
        self.assertEqual(self.profile.happy_clients, 0)


class ContentInventoryTests(SeededTestCase):
    def test_expected_inventory_sizes(self):
        self.assertEqual(Skill.objects.count(), 24)
        self.assertEqual(Service.objects.count(), 4)
        self.assertEqual(Article.objects.count(), 4)
        self.assertEqual(Experience.objects.count(), 6)
        self.assertEqual(MarqueeTag.objects.count(), 30)

    def test_every_experience_exists_in_the_project_list(self):
        titles = {e.title_en for e in Experience.objects.all()}
        self.assertNotIn('Exam Analysis & Statistics System', titles)

    def test_no_stale_claims_anywhere(self):
        blobs = []
        for model, fields in (
            (SiteText, ('value_en', 'value_fa', 'value_ar')),
            (Project, ('title_en', 'description_en', 'tech_stack')),
            (Experience, ('title_en', 'description_en')),
            (Article, ('title_en', 'excerpt_en')),
            (Profile, ('summary_en', 'location_en')),
        ):
            for obj in model.objects.all():
                for field in fields:
                    value = getattr(obj, field, '') or ''
                    blobs.append(value.lower())

        haystack = '\n'.join(blobs)
        for claim in STALE_CLAIMS:
            self.assertNotIn(claim, haystack, f'stale claim still present: {claim}')

    def test_orphaned_clients_statistic_is_gone(self):
        self.assertFalse(SiteText.objects.filter(key='stats.clients').exists())


class HomePageTests(SeededTestCase):
    # secure=True mirrors the production setup: nginx terminates TLS and
    # Django's SECURE_SSL_REDIRECT would otherwise answer 301 in tests.
    def test_home_renders_the_real_project_count(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['repo_count'], Project.objects.count())

    def test_home_shows_four_years_of_experience(self):
        response = self.client.get(reverse('portfolio:home'), secure=True)
        self.assertEqual(response.context['profile'].years_experience, 4)

    def test_home_renders_in_every_language(self):
        for prefix in ('en', 'fa', 'ar'):
            response = self.client.get(f'/{prefix}/', secure=True)
            self.assertEqual(response.status_code, 200, prefix)
            self.assertContains(response, 'data-count="12"')

class LlmsFilesTests(SeededTestCase):
    """The machine-readable files must describe the real database."""

    @staticmethod
    def _read(name):
        from pathlib import Path
        path = Path(__file__).resolve().parent.parent / 'static' / name
        return path.read_text(encoding='utf-8')

    def test_llms_txt_links_every_project(self):
        text = self._read('llms.txt')
        for project in Project.objects.all():
            self.assertIn(f'/en/projects/{project.slug}/', text)

    def test_llms_txt_links_every_article(self):
        text = self._read('llms.txt')
        for article in Article.objects.all():
            self.assertIn(f'/en/articles/{article.slug}/', text)

    def test_llms_txt_states_the_real_numbers(self):
        text = self._read('llms.txt')
        self.assertIn('12 public project case studies', text)
        self.assertIn('4 years of shipping production software', text)
        self.assertNotIn('PostgreSQL', text)

    def test_llms_full_reports_the_real_counters(self):
        text = self._read('llms-full.txt')
        self.assertIn('4+ Years Building Software', text)
        self.assertIn('12 Projects Delivered', text)
        self.assertIn('12 Open-Source Repos', text)
        for project in Project.objects.all():
            self.assertIn(project.repo_url, text)


class TestimonialHeadingTests(SeededTestCase):
    """The section must not imply clients: the two cards are feedback."""

    def test_heading_is_feedback_and_collaborators(self):
        for lang, expected in (('en', 'Feedback & Collaborators'),
                               ('fa', 'بازخورد و همکاران'),
                               ('ar', 'آراء وتعاون')):
            obj = SiteText.objects.get(key='testimonials.title')
            self.assertEqual(getattr(obj, f'value_{lang}'), expected)

    def test_no_client_wording_in_the_headings(self):
        for lang in ('en', 'fa', 'ar'):
            title = SiteText.objects.get(key='testimonials.title')
            value = getattr(title, f'value_{lang}').lower()
            self.assertNotIn('client', value)
            self.assertNotIn('مشتری', value)
            self.assertNotIn('عميل', value)

    def test_both_cards_are_still_rendered(self):
        from portfolio.models import Testimonial
        self.assertEqual(Testimonial.objects.count(), 2)


class HreflangTests(SeededTestCase):
    """Every page advertises its language alternates and an x-default."""

    def test_home_has_all_alternates(self):
        response = self.client.get('/en/', secure=True)
        self.assertEqual(response.status_code, 200)
        body = response.content.decode('utf-8')
        for code in ('en', 'fa', 'ar'):
            self.assertIn(f'hreflang="{code}"', body)
            self.assertIn(f'https://mhkaman.com/{code}/', body)
        self.assertIn('hreflang="x-default"', body)
        self.assertIn('https://mhkaman.com/en/', body)

    def test_project_page_has_alternates(self):
        response = self.client.get(
            '/en/projects/kaman-ai-translator/', secure=True)
        self.assertEqual(response.status_code, 200)
        body = response.content.decode('utf-8')
        self.assertIn('hreflang="fa"', body)
        self.assertIn('hreflang="ar"', body)
        self.assertIn(
            'https://mhkaman.com/fa/projects/kaman-ai-translator/', body)
        self.assertIn('hreflang="x-default"', body)

    def test_canonical_uses_the_public_domain(self):
        response = self.client.get('/fa/', secure=True)
        body = response.content.decode('utf-8')
        self.assertIn(
            '<link rel="canonical" href="https://mhkaman.com/fa/">', body)


class SitemapTests(SeededTestCase):
    """The sitemap must list the CV pages and carry language alternates."""

    def _sitemap(self, section=None):
        url = '/sitemap.xml' if not section else f'/sitemap-{section}.xml'
        response = self.client.get(url, secure=True)
        self.assertEqual(response.status_code, 200)
        return response.content.decode('utf-8')

    def test_cv_pages_are_listed(self):
        body = self._sitemap()
        for code in ('en', 'fa', 'ar'):
            self.assertIn(f'<loc>https://mhkaman.com/{code}/cv/</loc>', body)

    def test_alternates_are_present(self):
        body = self._sitemap()
        self.assertIn('hreflang="fa"', body)
        self.assertIn('hreflang="ar"', body)
        self.assertIn('hreflang="x-default"', body)

    def test_no_local_host_in_the_sitemap(self):
        body = self._sitemap()
        self.assertNotIn('127.0.0.1', body)
        self.assertNotIn('localhost', body)
        self.assertNotIn('testserver', body)


class CvContentTests(SeededTestCase):
    """The CV source of truth must carry the verified facts and no guesses."""

    @staticmethod
    def _data():
        import importlib
        import cv_data
        importlib.reload(cv_data)
        return cv_data.DATA

    def test_every_project_shows_its_real_release(self):
        releases = [
            'v3.0.0', 'v0.2.0', 'v1.0.0', 'v1.1.0', 'v7.0.1',
            'v10.0.0', 'v1.2.1',
        ]
        for lang in ('en', 'fa', 'ar'):
            projects = self._data()[lang]['sections'][0][1]
            headers = ' '.join(h for _, h, _ in projects)
            for release in releases:
                self.assertIn(release, headers, f'{lang} misses {release}')

    def test_unverifiable_claims_are_gone(self):
        for lang in ('en', 'fa', 'ar'):
            blob = str(self._data()[lang])
            self.assertNotIn('Bootstrap', blob)
            self.assertNotIn('PyCharm', blob)
            self.assertNotIn('VS Code', blob)

    def test_verified_facts_are_present(self):
        en = str(self._data()['en'])
        self.assertIn('303 offline tests', en)
        self.assertIn('Twelve named checks', en)
        self.assertIn('Edge WebView2', en)
        self.assertIn('CustomTkinter', en)
        self.assertIn('yt-dlp', en)
        self.assertIn('FastAPI', en)
        self.assertIn('django-allauth', en)
        self.assertIn('jdatetime', en)
