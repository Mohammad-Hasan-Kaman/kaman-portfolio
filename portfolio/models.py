from django.db import models


class Profile(models.Model):
    """Single-row profile model — editable from the Django admin."""
    name_en = models.CharField(max_length=120, default='Mohammad Hasan Kaman')
    name_fa = models.CharField(max_length=120, default='محمد حسن کَمَن')
    name_ar = models.CharField(max_length=120, default='محمد حسن كَمَن')

    role_en = models.CharField(max_length=200, default='Full-Stack Developer')
    role_fa = models.CharField(max_length=200, default='توسعه‌دهنده فول‌استک')
    role_ar = models.CharField(max_length=200, default='مطور برمجيات متكاملة')

    tagline_en = models.TextField(blank=True)
    tagline_fa = models.TextField(blank=True)
    tagline_ar = models.TextField(blank=True)

    about_en = models.TextField(blank=True)
    about_fa = models.TextField(blank=True)
    about_ar = models.TextField(blank=True)

    email = models.EmailField(default='mohammadhasankaman@gmail.com')
    phone = models.CharField(max_length=40, blank=True)
    location_en = models.CharField(max_length=120, default='Germany (Remote)')
    location_fa = models.CharField(max_length=120, default='آلمان (دورکاری)')
    location_ar = models.CharField(max_length=120, default='ألمانيا (عن بُعد)')

    github = models.URLField(default='https://github.com/Mohammad-Hasan-Kaman')
    linkedin = models.URLField(default='https://www.linkedin.com/in/kaman-programmer/')
    twitter = models.URLField(default='https://x.com/kaman_hasan0975')
    telegram = models.URLField(default='https://t.me/mohaka0975')

    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)

    summary_en = models.TextField(
        blank=True,
        default='Highly motivated and self-taught developer with a strong foundation in Python and JavaScript. '
                'Experienced in engineering custom AI-powered applications, backend automation tools and full-stack '
                'web solutions, with a passion for solving algorithmic and system-level problems.')
    summary_fa = models.TextField(blank=True)
    summary_ar = models.TextField(blank=True)

    # Core Competencies — from the original CV PDF
    core_competencies_en = models.TextField(
        blank=True,
        default='Backend Development & Automation\nAPI Integration & Management\nDatabase Design & Architecture\nAI Application Development\nWeb Application Architecture\nNetwork Infrastructure & Troubleshooting')
    core_competencies_fa = models.TextField(blank=True)
    core_competencies_ar = models.TextField(blank=True)

    years_experience = models.PositiveIntegerField(default=4)
    projects_completed = models.PositiveIntegerField(default=15)
    happy_clients = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('ai', 'AI & Developer Tools'),
        ('web', 'Web Platforms'),
        ('security', 'Security & Networking'),
        ('desktop', 'Desktop & Bots'),
    ]

    title_en = models.CharField(max_length=160)
    title_fa = models.CharField(max_length=160, blank=True)
    title_ar = models.CharField(max_length=160, blank=True)

    slug = models.SlugField(max_length=160, unique=True)

    description_en = models.TextField()
    description_fa = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='ai')
    icon = models.CharField(max_length=10, default='🚀', help_text='Emoji shown on the project card')
    tech_stack = models.CharField(max_length=300, help_text='Comma-separated, e.g. Python, Django, SQLite')

    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False, help_text='Featured projects appear larger on the home page')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-featured', 'id']
    def __str__(self):
        return self.title_en


class Skill(models.Model):
    TIER_CHOICES = [
        (1, 'Advanced — used in shipped projects'),
        (2, 'Production experience'),
        (3, 'Working knowledge'),
    ]
    name = models.CharField(max_length=80)
    tier = models.PositiveIntegerField(default=2, choices=TIER_CHOICES,
                                       help_text='Honest level label — no percentages')
    level_en = models.CharField(max_length=60, blank=True,
                                help_text='Optional custom label (EN). Leave blank to use tier default.')
    level_fa = models.CharField(max_length=60, blank=True, help_text='Optional custom label (FA).')
    level_ar = models.CharField(max_length=60, blank=True, help_text='Optional custom label (AR).')
    icon = models.CharField(max_length=10, blank=True, help_text='Emoji (optional)')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name

    def tier_label(self, lang='en'):
        custom = getattr(self, f'level_{lang}', '') or self.level_en
        if custom:
            return custom
        defaults = {
            1: {'en': 'Advanced — shipped in projects', 'fa': 'تسلط عملی — در پروژه‌های تحویل‌شده', 'ar': 'متقدم — في مشاريع منجزة'},
            2: {'en': 'Production experience', 'fa': 'تجربهٔ production', 'ar': 'خبرة إنتاجية'},
            3: {'en': 'Working knowledge', 'fa': 'آشنایی کاری', 'ar': 'معرفة عملية'},
        }
        return defaults.get(self.tier, defaults[2]).get(lang) or defaults[self.tier]['en']


class Service(models.Model):
    icon = models.CharField(max_length=10, default='💡', help_text='Emoji')
    title_en = models.CharField(max_length=140)
    title_fa = models.CharField(max_length=140, blank=True)
    title_ar = models.CharField(max_length=140, blank=True)

    description_en = models.TextField()
    description_fa = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title_en


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    role_en = models.CharField(max_length=140, blank=True)
    role_fa = models.CharField(max_length=140, blank=True)
    role_ar = models.CharField(max_length=140, blank=True)

    text_en = models.TextField()
    text_fa = models.TextField(blank=True)
    text_ar = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Experience(models.Model):
    """Professional projects / experience entries — shown on the CV page."""
    title_en = models.CharField(max_length=200)
    title_fa = models.CharField(max_length=200, blank=True)
    title_ar = models.CharField(max_length=200, blank=True)

    org_en = models.CharField(max_length=160, blank=True, help_text='Company / client (optional)')
    org_fa = models.CharField(max_length=160, blank=True)
    org_ar = models.CharField(max_length=160, blank=True)

    period_en = models.CharField(max_length=80, blank=True, help_text='e.g. 2024 — 2026')
    period_fa = models.CharField(max_length=80, blank=True)
    period_ar = models.CharField(max_length=80, blank=True)

    description_en = models.TextField()
    description_fa = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title_en


class Education(models.Model):
    degree_en = models.CharField(max_length=200)
    degree_fa = models.CharField(max_length=200, blank=True)
    degree_ar = models.CharField(max_length=200, blank=True)

    institution_en = models.CharField(max_length=200, blank=True)
    institution_fa = models.CharField(max_length=200, blank=True)
    institution_ar = models.CharField(max_length=200, blank=True)

    period_en = models.CharField(max_length=80, blank=True)
    period_fa = models.CharField(max_length=80, blank=True)
    period_ar = models.CharField(max_length=80, blank=True)

    details_en = models.TextField(blank=True, help_text='Relevant studies / highlights (one per line)')
    details_fa = models.TextField(blank=True)
    details_ar = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.degree_en


class CvLanguage(models.Model):
    name_en = models.CharField(max_length=60)
    name_fa = models.CharField(max_length=60, blank=True)
    name_ar = models.CharField(max_length=60, blank=True)

    level_en = models.CharField(max_length=80)
    level_fa = models.CharField(max_length=80, blank=True)
    level_ar = models.CharField(max_length=80, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'CV Language'
        verbose_name_plural = 'CV Languages'

    def __str__(self):
        return self.name_en


class Article(models.Model):
    """Blog / articles — fully manageable from the Django admin."""
    title_en = models.CharField(max_length=220)
    title_fa = models.CharField(max_length=220, blank=True)
    title_ar = models.CharField(max_length=220, blank=True)

    slug = models.SlugField(max_length=220, unique=True)

    icon = models.CharField(max_length=10, default='📝', help_text='Emoji shown on the article card')

    excerpt_en = models.TextField(blank=True, help_text='Short summary shown on the card')
    excerpt_fa = models.TextField(blank=True)
    excerpt_ar = models.TextField(blank=True)

    body_en = models.TextField(help_text='Full article text (EN). Separate paragraphs with a blank line.')
    body_fa = models.TextField(blank=True)
    body_ar = models.TextField(blank=True)

    cover = models.ImageField(upload_to='articles/', blank=True, null=True)
    published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text='Newest first by date; use order to pin items')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title_en


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'


class SiteText(models.Model):
    """Every UI string on the site, editable from the admin.

    key mirrors the nested keys of translations.STRINGS using dots
    (e.g. hero.greeting, footer.rights, projects.title).  Empty FA/AR
    fields fall back to EN, exactly like the templates' `tf` helper.
    """
    key = models.CharField(max_length=100, unique=True, db_index=True)
    label = models.CharField(
        max_length=200, blank=True,
        help_text='Human-readable hint shown in the admin (auto-filled by seed)')
    value_en = models.TextField(blank=True)
    value_fa = models.TextField(blank=True)
    value_ar = models.TextField(blank=True)

    class Meta:
        ordering = ['key']
        verbose_name = 'UI Text'
        verbose_name_plural = 'UI Texts (menus, headings, buttons, footer)'

    def __str__(self):
        return self.key


class MarqueeTag(models.Model):
    """Tech tags scrolling in the hero marquee bar."""
    label = models.CharField(max_length=60, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'label']

    def __str__(self):
        return self.label


class Visit(models.Model):
    """Server-side analytics — no third-party trackers, no raw IPs.

    event: pageview | cv_download | contact | lang_switch
    ip_hash is a salted hash (never the raw address); session_key is an
    anonymous per-visitor cookie id used only for unique-visitor counts.
    """
    EVENT_CHOICES = [
        ('pageview', 'Page view'),
        ('cv_download', 'CV download'),
        ('contact', 'Contact form'),
        ('lang_switch', 'Language switch'),
    ]
    DEVICE_CHOICES = [('desktop', 'Desktop'), ('mobile', 'Mobile'), ('tablet', 'Tablet')]

    event = models.CharField(max_length=20, choices=EVENT_CHOICES, default='pageview')
    path = models.CharField(max_length=300, blank=True, db_index=True)
    lang = models.CharField(max_length=2, default='en')
    referrer = models.CharField(max_length=400, blank=True)
    device = models.CharField(max_length=10, choices=DEVICE_CHOICES, default='desktop')
    user_agent = models.CharField(max_length=300, blank=True)
    ip_hash = models.CharField(max_length=16, blank=True)
    session_key = models.CharField(max_length=40, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Visit / event'
        verbose_name_plural = 'Analytics — visits & events'

    def __str__(self):
        return f'{self.event} {self.path} @ {self.created_at:%Y-%m-%d %H:%M}'