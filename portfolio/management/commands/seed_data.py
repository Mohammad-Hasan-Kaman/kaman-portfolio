"""Seed the database with Mohammad Hasan Kaman portfolio data.

Every project, skill and experience below is backed by a public GitHub
repository, its release tags, its README or a live URL — no claim here that
is not verifiable in code.

Run:  python manage.py seed_data
Idempotent: creates what is missing, updates what drifted, never duplicates.
"""
from django.core.management.base import BaseCommand

from portfolio.models import (Article, CvLanguage, Education, Experience, Profile,
                              Project, Service, Skill, Testimonial)

# ---------------------------------------------------------------- projects
# Source of truth: the 12 public project repositories. The profile repository
# is not a project and is deliberately excluded.
PROJECTS = [
    {
        'title_en': 'Kaman AI Translator', 'slug': 'kaman-ai-translator', 'category': 'ai', 'icon': '📚',
        'title_fa': 'مترجم هوشمند کَمَن', 'title_ar': 'مترجم كَمَن الذكي',
        'description_en': 'A PyQt6 desktop studio that translates whole PDF and EPUB books into fluent academic Persian — and back into English — one page at a time or an entire book unattended. Per-book structure templates keep terminology consistent, a QC review loop catches meaning drift, and API keys are encrypted with Windows DPAPI. 303 offline tests, Windows release v3.0.0.',
        'description_fa': 'یک استودیوی دسکتاپ با PyQt6 که کل کتاب‌های PDF و EPUB را به فارسی آکادمیک روان — و برعکس به انگلیسی — ترجمه می‌کند؛ صفحه‌به‌صفحه یا یک کتاب کامل به‌صورت خودکار. تمپلیت ساختار اختصاصی هر کتاب اصطلاحات را یکدست نگه می‌دارد، حلقهٔ بازبینی QC انحراف معنایی را می‌گیرد و کلید API با Windows DPAPI رمزنگاری می‌شود. ۳۰۳ تست آفلاین، نسخهٔ ویندوز v3.0.0.',
        'description_ar': 'استوديو سطح مكتب بـ PyQt6 يترجم كتب PDF وEPUB كاملة إلى الفارسية الأكاديمية السليمة — وإلى الإنجليزية — صفحةً صفحة أو كتاباً كاملاً دون إشراف. قوالب بنية خاصة لكل كتاب تحافظ على اتساق المصطلحات، وحلقة مراجعة QC تكشف الانحراف المعنى، ومفاتيح API مشفّرة بـ Windows DPAPI. 303 اختباراً دون اتصال، وإصدار v3.0.0 لويندوز.',
        'tech_stack': 'Python, PyQt6, Gemini / OpenAI-compatible APIs, SSE, DPAPI, PDF, EPUB',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator',
        'featured': True, 'order': 1,
    },
    {
        'title_en': 'Agent Stream Doctor', 'slug': 'agent-stream-doctor', 'category': 'ai', 'icon': '🩺',
        'title_fa': 'ایجنت استریم داکتر', 'title_ar': 'دكتور البث للوكلاء',
        'description_en': 'A zero-dependency Python CLI that reads raw SSE chat-completion captures and explains exactly why an LLM stream returned nothing — reasoning-only responses, missing finish_reason, malformed SSE framing, truncated tool calls. Twelve named checks, an explainable report, JSON output for CI, usable as a library. Release v0.2.0.',
        'description_fa': 'یک CLI پایتونی بدون وابستگی که کپچرهای خام SSE را می‌خواند و دقیقاً توضیح می‌دهد چرا یک استریم LLM خالی برگشته — پاسخ‌های فقط-استدلالی، فقدان finish_reason، فریم‌بندی خراب SSE و فراخوانی ابزار ناقص. ۱۲ بررسی نام‌گذاری‌شده، گزارش قابل‌توضیح، خروجی JSON برای CI و قابل استفاده به‌عنوان کتابخانه. نسخهٔ v0.2.0.',
        'description_ar': 'واجهة سطر أوامر Python بلا تبعيات تقرأ لقطات SSE الخام وتشرح بدقة سبب عودة بث LLM فارغاً — ردود استدلالية فقط، غياب finish_reason، تلف إطارات SSE واستدعاءات أدوات مبتورة. اثنا عشر فحصاً مسمّاة، وتقرير مُفسَّر، ومخرج JSON للاستخدام في CI، وقابل للاستيراد كمكتبة. إصدار v0.2.0.',
        'tech_stack': 'Python, SSE, OpenAI-compatible APIs, CLI, JSON output',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/agent-stream-doctor',
        'featured': True, 'order': 2,
    },
    {
        'title_en': 'AI Counseling Widget', 'slug': 'ai-counseling-widget', 'category': 'web', 'icon': '🧠',
        'title_fa': 'ویجت مشاورهٔ هوشمند', 'title_ar': 'أداة مشورة ذكية',
        'description_en': 'An AI intake system for counselling centres, shipped as a Persian RTL chat widget. The assistant talks to every visitor, runs the GHQ-28 wellbeing screening, extracts clinical concepts from free text and matches the person to the right consultant. Multi-tenant API keys and admin panel, embedded with a single script tag — no hosted LLM, no per-message cost. Live at kahaai.ir.',
        'description_fa': 'یک سامانهٔ پذیرش هوشمند برای مراکز مشاوره که به‌شکل ویجت چت فارسی و راست‌چین عرضه می‌شود. دستیار با هر مراجعه‌کننده گفتگو می‌کند، تست سلامت GHQ-28 را اجرا می‌کند، مفاهیم بالینی را از متن آزاد استخراج می‌کند و فرد را به مشاور مناسب وصل می‌کند. کلید API چندمستاجری و پنل مدیریت، با یک تگ اسکریپت — بدون LLM ابری و بدون هزینهٔ هر پیام. زنده در kahaai.ir.',
        'description_ar': 'نظام استقبال ذكي لمراكز الاستشارات، يُطرح كأداة محادثة فارسية كاملة الاتجاه. يتحدث المساعد مع كل زائر، ويجري فحص GHQ-28، ويستخرج المفاهيم السريرية من النص الحر، ثم يطابق الشخص مع المستشار المناسب. مفاتيح API متعددة المستأجرين ولوحة إدارة، عبر وسم واحد — دون نموذج سحابي ولا تكلفة لكل رسالة. يعمل على kahaai.ir.',
        'tech_stack': 'FastAPI, SQLite, GHQ-28 screening, concept extraction, matching engine, RTL UI',
        'live_url': 'https://kahaai.ir',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget',
        'featured': True, 'order': 3,
    },
    {
        'title_en': 'AI Counseling Bot', 'slug': 'ai-counseling-bot', 'category': 'ai', 'icon': '💬',
        'title_fa': 'ربات مشاورهٔ هوشمند', 'title_ar': 'بوت مشورة ذكي',
        'description_en': 'The same clinical intake intelligence as a Bale messenger bot: a 12-state guided conversation, the GHQ-28 wellbeing screen, and a SpiralMatchEngine that re-weights itself from panel feedback. Admins run statistics, Excel import/export, broadcasts and engine training from inside the chat. No external API, no cloud LLM. Release v1.0.0.',
        'description_fa': 'همان هوش پذیرش بالینی، این بار به‌شکل ربات پیام‌رسان بله: یک گفتگوی هدایت‌شده با ۱۲ وضعیت، تست GHQ-28 و موتور SpiralMatchEngine که از بازخورد پنل خودش را بازتنظیم می‌کند. مدیران آمار، ورود/خروج اکسل، پیام همگانی و آموزش موتور را از داخل گفتگو انجام می‌دهند. بدون API خارجی، بدون LLM ابری. نسخهٔ v1.0.0.',
        'description_ar': 'نفس ذكاء الاستقبال السريري، لكن كبوت مراسلة على Bale: محادثة موجّهة باثنتي عشرة حالة، وفحص GHQ-28، ومحرك SpiralMatchEngine يعيد ضبط نفسه من تغذية راجعة اللوحة. يدير المشرفون الإحصاءات واستيراد/تصدير Excel والبثّ وتدريب المحرك من داخل المحادثة. دون API خارجي ولا نموذج سحابي. إصدار v1.0.0.',
        'tech_stack': 'Python, Bale Messenger API, GHQ-28 screening, matching engine, SQLite',
        'live_url': 'https://kahaai.ir',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot',
        'featured': True, 'order': 4,
    },
    {
        'title_en': 'Kaman Portfolio', 'slug': 'kaman-portfolio', 'category': 'web', 'icon': '🗂️',
        'title_fa': 'پورتفولیوی کَمَن', 'title_ar': 'ملف أعمال كَمَن',
        'description_en': 'This very site: a trilingual (EN/FA/AR) Django portfolio where every page is editable from the Django admin, with a trilingual PDF CV generator that shapes RTL text with HarfBuzz, privacy-friendly server-side analytics, and sitemap, robots.txt and llms.txt built in. Live at mhkaman.com.',
        'description_fa': 'همین سایت: یک پورتفولیوی سه‌زبانه (انگلیسی/فارسی/عربی) با جنگو که همهٔ صفحه‌هایش از پنل ادمین قابل ویرایش است، به‌همراه تولیدکنندهٔ CV سه‌زبانهٔ PDF با شکل‌دهی متن راست‌به‌چپ، تحلیل حریم‌خصوصی سمت سرور و sitemap، robots.txt و llms.txt آماده. زنده در mhkaman.com.',
        'description_ar': 'هذا الموقع نفسه: ملف أعمال Django ثلاثي اللغات (EN/FA/AR) تُحرَّر كل صفحاته من لوحة الإدارة، مع مولّد سيرة ذاتية PDF ثلاثي اللغات يشكّل النص من اليمين إلى اليسار، وتحليلات تحافظ على الخصوصية، وsitemap وrobots.txt وllms.txt مدمجة. يعمل على mhkaman.com.',
        'tech_stack': 'Django, SQLite, fpdf2, HarfBuzz shaping, nginx, gunicorn',
        'live_url': 'https://mhkaman.com',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-portfolio',
        'featured': True, 'order': 5,
    },
    {
        'title_en': 'Kaman Messenger', 'slug': 'kaman-messenger', 'category': 'security', 'icon': '🔐',
        'title_fa': 'پیام‌رسان کَمَن', 'title_ar': 'مرسال كَمَن',
        'description_en': 'A real-time encrypted messenger built completely from scratch: raw TCP sockets, Fernet (AES) traffic encryption, bcrypt authentication, rate limiting and SQLite storage, with a CustomTkinter GUI. Ships as a client and a server executable.',
        'description_fa': 'یک پیام‌رسان رمزنگاری‌شدهٔ بلادرنگ که کاملاً از صفر ساخته شده: سوکت TCP خام، رمزنگاری ترافیک با Fernet (AES)، احراز هویت bcrypt، محدودسازی نرخ و ذخیره‌سازی SQLite، با رابط CustomTkinter. به‌صورت اجرایی کلاینت و سرور منتشر می‌شود.',
        'description_ar': 'مرسال مشفّر فوري مبني بالكامل من الصفر: مقابس TCP الخام، تشفير حركة المرور بـ Fernet (AES)، مصادقة bcrypt، تحديد المعدل، وتخزين SQLite، بواجهة CustomTkinter. يُنشر كملفَّذي عميل وخادم.',
        'tech_stack': 'Python, TCP Sockets, Fernet/AES, bcrypt, SQLite, CustomTkinter',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-messenger',
        'featured': True, 'order': 6,
    },
    {
        'title_en': 'Dr-Kaman Site', 'slug': 'dr-kaman-site', 'category': 'web', 'icon': '🌐',
        'title_fa': 'سایت دکتر کَمَن', 'title_ar': 'موقع د. كَمَن',
        'description_en': 'A multimedia archive for Dr. Mohammad Reza Kaman — podcasts, videos, books and articles with cross-media search, topic categories, a homepage slider and SEO endpoints for crawlers. Django behind nginx and gunicorn on a Linux VPS. Live at drkaman.ir.',
        'description_fa': 'یک آرشیو چندرسانه‌ای برای دکتر محمدرضا کَمَن — پادکست، ویدیو، کتاب و مقاله با جستجوی بین‌رسانه‌ای، دسته‌بندی موضوعی، اسلایدر صفحهٔ اصلی و endpointهای سئو برای خزنده‌ها. جنگو پشت nginx و gunicorn روی سرور لینوکسی. زنده در drkaman.ir.',
        'description_ar': 'أرشيف وسائط متعددة للدكتور محمدرضا كَمَن — بودكاست ومقاطع وكتب ومقالات مع بحث عبر الوسائط وتصنيف موضوعي وشريط الصفحة الرئيسية ونقاط SEO للزواحف. Django خلف nginx و gunicorn على خادم Linux. يعمل على drkaman.ir.',
        'tech_stack': 'Django, SQLite, nginx, gunicorn, Linux VPS, JavaScript',
        'live_url': 'https://drkaman.ir',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site',
        'featured': False, 'order': 7,
    },
    {
        'title_en': 'Planikaa Portal', 'slug': 'planikaa-portal', 'category': 'web', 'icon': '🎓',
        'title_fa': 'پورتال پلنیکا', 'title_ar': 'بوابة بلانيكا',
        'description_en': 'A Django educational platform for exam and competition analysis with visual dashboards, an educational blog, a review and feedback system, Jalali (Persian) calendar support and django-allauth accounts.',
        'description_fa': 'یک پلتفرم آموزشی جنگو برای تحلیل آزمون‌ها و مسابقات با داشبوردهای بصری، وبلاگ آموزشی، سیستم نظرات و بازخورد، پشتیبانی از تقویم هجری شمسی و حساب‌های django-allauth.',
        'description_ar': 'منصة تعليمية Django لتحليل الاختبارات والمسابقات مع لوحات بصرية، ومدونة تعليمية، ونظام مراجعات وتغذية راجعة، ودعم التقويم الهجري Solar، وحسابات django-allauth.',
        'tech_stack': 'Django, SQLite, Chart.js, Jalali calendar, django-allauth',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/planikaa-portal',
        'featured': False, 'order': 8,
    },
    {
        'title_en': 'Kaman AI Chat', 'slug': 'kaman-ai-chat', 'category': 'ai', 'icon': '💬',
        'title_fa': 'چت هوشمند کَمَن', 'title_ar': 'دردشة كَمَن الذكية',
        'description_en': 'A C# WinForms chat assistant that talks to DeepSeek models through the OpenModel API and speaks the reply with the Windows built-in text-to-speech engine. The API key is resolved at runtime from an environment variable, app.config or a per-user settings file — never baked into the source. Single dependency-free .exe.',
        'description_fa': 'یک دستیار گفتگوی دسکتاپ با C# و WinForms که با مدل‌های DeepSeek از طریق OpenModel API گفتگو می‌کند و پاسخ را با موتور گفتار به‌نمایش‌داده‌شدهٔ داخلی ویندوز می‌خواند. کلید API در زمان اجرا از متغیر محیطی، app.config یا فایل تنظیمات کاربر خوانده می‌شود — هرگز در سورس قرار نمی‌گیرد. یک فایل اجرایی مستقل و بدون وابستگی.',
        'description_ar': 'مساعد دردشة سطح مكتب بـ C# و WinForms يتحدث إلى نماذج DeepSeek عبر OpenModel API وينطق الردّ بمحرك النطق المدمج في ويندوز. تُقرأ مفتاح API عند التشغيل من متغيّر بيئة أو app.config أو ملف إعدادات المستخدم — ولا تُدمج في الشيفرة أبداً. ملف تنفيذي واحد بلا تبعيات.',
        'tech_stack': 'C#, .NET Framework 4.8, WinForms, OpenModel API, System.Speech',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-ai-chat',
        'featured': False, 'order': 9,
    },
    {
        'title_en': 'Quran Group Bot', 'slug': 'quran-group-bot', 'category': 'desktop', 'icon': '🕌',
        'title_fa': 'ربات گروه قرآن', 'title_ar': 'بوت مجموعة القرآن',
        'description_en': 'A serverless Bale bot that runs a 30-person weekly Quran juz reading circle — Cloudflare Workers and KV with cron-scheduled posts, rotating juz assignment and a weekly hadith. No server, no hosting bill.',
        'description_fa': 'یک ربات بدون سرور روی بله که حلقهٔ هفتگی قرائت جزء قرآن برای ۳۰ نفر را اداره می‌کند — Cloudflare Workers و KV با زمان‌بندی کرون، نوبت‌بندی چرخشی جزء و حدیث هفتگی. بدون سرور و بدون فاکتور هاستینگ.',
        'description_ar': 'بوت بلا خادم على Bale يدير حلقة أسبوعية لقراءة جزء القرآن لـ30 شخصاً — Cloudflare Workers و KV مع جدولة cron، وإسناد متناوب للأجزاء، وحديث أسبوعي. دون خادم ولا فاتورة استضافة.',
        'tech_stack': 'Bale Messenger, Cloudflare Workers, KV, JavaScript, Cron',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/quran-group-bot',
        'featured': False, 'order': 10,
    },
    {
        'title_en': 'YouTube Downloader', 'slug': 'youtube-downloader', 'category': 'desktop', 'icon': '⬇️',
        'title_fa': 'دانلودر یوتیوب', 'title_ar': 'محمّل يوتيوب',
        'description_en': 'A Windows YouTube downloader built on yt-dlp with a Persian dark-mode GUI, three live progress bars, video and audio format selection, and browser-cookie support for age-restricted or private links.',
        'description_fa': 'یک دانلودر یوتیوب ویندوزی بر پایهٔ yt-dlp با رابط گرافیکی تیره و فارسی، سه نوار پیشرفت زنده، انتخاب قالب ویدیو و صدا و پشتیبانی از کوکی مرورگر برای لینک‌های محدودشده یا خصوصی.',
        'description_ar': 'محمّل يوتيوب لويندوز مبني على yt-dlp بواجهة داكنة فارسية، وثلاثة أشرطة تقدّم حيّة، واختيار صيغة الفيديو والصوت، ودعم ملفات تعريف الارتباط للمتصفح للروابط المقيّدة أو الخاصة.',
        'tech_stack': 'Python, CustomTkinter, yt-dlp, RTL UI',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/youtube-downloader',
        'featured': False, 'order': 11,
    },
    {
        'title_en': 'Kaman Web Browser', 'slug': 'kaman-web-browser', 'category': 'desktop', 'icon': '🧭',
        'title_fa': 'مرورگر وب کَمَن', 'title_ar': 'متصفح كَمَن',
        'description_en': 'A lightweight multi-tab Windows browser on Microsoft Edge WebView2 (Chromium) with smart routing that decides whether what you typed is a URL or a search query, plus bookmarks and session handling.',
        'description_fa': 'یک مرورگر سبک و چندتب‌ویندوزی روی Microsoft Edge WebView2 (کرومیوم) با مسیریابی هوشمند که تشخیص می‌دهد آنچه تایپ کرده‌اید آدرس است یا عبارت جست‌وجو، به‌همراه بوکمارک و مدیریت نشست.',
        'description_ar': 'متصفح ويندوز خفيف متعدد التبويبات على Microsoft Edge WebView2 (Chromium) مع توجيه ذكي يحدّد إن كان ما كتبته رابطاً أم عبارة بحث، إضافة إلى المفضلة وإدارة الجلسات.',
        'tech_stack': 'C#, .NET, WebView2, Chromium',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-web-browser',
        'featured': False, 'order': 12,
    },
]

# ------------------------------------------------------------------ skills
# tier: 1 = shipped in projects, 2 = production experience, 3 = working knowledge
SKILLS = [
    ('Python', 1, '🐍', 1), ('Django', 1, '🎸', 2), ('C#', 1, '🎯', 3),
    ('JavaScript', 2, '⚡', 4), ('REST API Design', 1, '🔗', 5),
    ('LLM APIs (OpenAI / Gemini / DeepSeek)', 1, '🤖', 6),
    ('SSE Streaming & Tool Calling', 1, '📡', 7),
    ('PyQt6 / CustomTkinter', 1, '🖥️', 8), ('C# WinForms / WebView2', 1, '🪟', 9),
    ('Edge WebView2 (Chromium)', 2, '🧭', 10), ('TCP Socket Programming', 1, '🔌', 11),
    ('AES / Fernet Encryption', 1, '🔐', 12),
    ('bcrypt & Auth Systems', 1, '🔑', 13), ('Rate Limiting & Hardening', 2, '🛡️', 14),
    ('SQLite / SQL Databases', 1, '🗄️', 15), ('nginx + gunicorn Deployment', 1, '🚀', 16),
    ('Linux VPS Administration', 2, '🐧', 17), ('BIND9 DNS', 3, '🌐', 18),
    ('Cloudflare Workers / KV', 2, '☁️', 19), ('Git & GitHub', 1, '🌱', 20),
    ('yt-dlp / Automation', 2, '⚙️', 21), ('HTML5 / CSS3', 2, '🎨', 22),
    ('OOP & Clean Architecture', 1, '🏛️', 23), ('Multithreading & Concurrency', 2, '🧵', 24),
]

# ---------------------------------------------------------------- services
SERVICES = [
    ('🌐', 'Web Development', 'توسعه وب', 'تطوير الويب',
     'Production-grade Django platforms with REST APIs, analytics dashboards and clean architecture.',
     'پلتفرم‌های حرفه‌ای جنگو با REST API، داشبورد تحلیلی و معماری تمیز.',
     'منصات Django احترافية مع REST API ولوحات تحليلات وبنية نظيفة.', 1),
    ('🤖', 'AI Engineering', 'مهندسی هوش مصنوعی', 'هندسة الذكاء الاصطناعي',
     'LLM-powered apps: chat assistants, streaming diagnostics, tool calling and AI integrations.',
     'اپلیکیشن‌های مبتنی بر LLM: دستیار گفتگو، تشخیص خطای استریم و یکپارچه‌سازی هوش مصنوعی.',
     'تطبيقات مدعومة بنماذج LLM: مساعدات محادثة، تشخيص البث، ودمج الذكاء الاصطناعي.', 2),
    ('🖥️', 'Desktop Applications', 'اپلیکیشن دسکتاپ', 'تطبيقات سطح المكتب',
     'Cross-platform desktop tools with PyQt6, CustomTkinter and C# WinForms.',
     'ابزارهای دسکتاپ چندسکویی با PyQt6، CustomTkinter و C# WinForms.',
     'أدوات سطح مكتب متعددة المنصات بـ PyQt6 و CustomTkinter و C# WinForms.', 3),
    ('🔐', 'Secure Systems', 'سیستم‌های امن', 'الأنظمة الآمنة',
     'Encrypted communication, hard authentication and rate-limited networking from scratch.',
     'ارتباط رمزنگاری‌شده، احراز هویت امن و شبکه‌سازی با محدودسازی نرخ، از صفر.',
     'اتصالات مشفّرة، مصادقة قوية وشبكات محددة المعدل — من الصفر.', 4),
]

# ------------------------------------------------------------------- about
ABOUT = {
    'about_en': "I'm a freelance full-stack developer focused on AI applications, developer tooling and secure systems. "
                "I build end-to-end software in Python and C# — from AI-driven clinical screening pipelines and "
                "encrypted desktop messengers to diagnostics for LLM streaming APIs and production Django platforms "
                "serving real users. I care about shipping reliable, well-engineered products that solve real problems.",
    'about_fa': "من یک توسعه‌دهنده فریلنسِ فول‌استک هستم و روی اپلیکیشن‌های هوش مصنوعی، ابزارهای توسعه‌دهنده و سیستم‌های امن تمرکز دارم. "
                "نرم‌افزارهای کامل با پایتون و سی‌شارپ می‌سازم — از خط لوله‌های غربال بالینی مبتنی بر هوش مصنوعی و "
                "پیام‌رسان‌های رمزنگاری‌شدهٔ دسکتاپ تا ابزارهای تشخیص خطای APIهای استریم LLM و پلتفرم‌های جنگو در محیط "
                "پروداکشن با کاربران واقعی. برای من مهم است که محصولاتی قابل‌اعتماد بسازم که مشکل واقعی را حل کنند.",
    'about_ar': "أنا مطوّر برمجيات متكاملة مستقل، أركّز على تطبيقات الذكاء الاصطناعي وأدوات المطورين والأنظمة الآمنة. "
                "أبني برمجيات كاملة بلغتي Python و C# — من خطوط فحص سريري مدعومة بالذكاء الاصطناعي ورسائل مشفّرة "
                "سطح المكتب إلى أدوات تشخيص لـ APIs البث في نماذج LLM ومنصات Django تعمل في الإنتاج لمستخدمين حقيقيين. "
                "أهتم بإنتاج برمجيات موثوقة ومهندسة جيداً تحل مشكلات حقيقية.",
}

TAGLINE = {
    'tagline_en': 'I build end-to-end software — from AI clinical screening pipelines and encrypted messengers to production Django platforms and AI-powered developer tools.',
    'tagline_fa': 'من نرم‌افزارهای کامل می‌سازم — از خط لوله‌های غربال بالینی هوشمند و پیام‌رسان‌های رمزنگاری‌شده تا پلتفرم‌های جنگو در محیط پروداکشن و ابزارهای توسعه مبتنی بر هوش مصنوعی.',
    'tagline_ar': 'أبني برمجيات متكاملة — من خطوط فحص سريري مدعومة بالذكاء الاصطناعي ورسائل مشفّرة إلى منصات Django في بيئة الإنتاج وأدوات تطوير مدعومة بالذكاء الاصطناعي.',
}

CORE_COMPETENCIES = {
    'core_competencies_en': 'Backend Development & Automation\nAPI Integration & Management\nDatabase Design & Architecture\nAI Application Development\nWeb Application Architecture\nNetwork Infrastructure & Troubleshooting',
    'core_competencies_fa': 'توسعه بک‌اند و اتوماسیون\nیکپارچه‌سازی و مدیریت API\nطراحی و معماری پایگاه داده\nتوسعه اپلیکیشن‌های هوش مصنوعی\nمعماری اپلیکیشن وب\nزیرساخت شبکه و عیب‌یابی',
    'core_competencies_ar': 'تطوير الواجهات الخلفية والأتمتة\nتكامل وإدارة واجهات برمجة التطبيقات\nتصميم وهندسة قواعد البيانات\nتطوير تطبيقات الذكاء الاصطناعي\nهندسة تطبيقات الويب\nالبنية التحتية للشبكات واستكشاف الأخطاء',
}

# ------------------------------------------------------------- testimonials
# Only relationships that are independently verifiable: the Dr. Kaman site
# is a real client project (live at drkaman.ir) and the second entry is an
# open-source user report — not a paid-client claim.
TESTIMONIALS = [
    ('Dr. Mohammad Reza Kaman', 'Site Owner, drkaman.ir', 'مالک سایت drkaman.ir', 'صاحب الموقع drkaman.ir',
     'Hasan delivered our production website end-to-end — Django, nginx and gunicorn on our own VPS. Fast, reliable and always reachable.',
     'حسن وب‌سایت پروداکشن ما را به‌صورت کامل تحویل داد — جنگو، nginx و gunicorn روی سرور اختصاصی خودمان. سریع، قابل‌اعتماد و همیشه در دسترس.',
     'أنجز حسن موقعنا في الإنتاج من البداية للنهاية — Django و nginx و gunicorn على خادمنا الخاص. سريع وموثوق ومتاح دائماً.', 1),
    ('Open-Source Collaborator', 'GitHub', 'همکار متن‌باز', 'متعاون مفتوح المصدر',
     'agent-stream-doctor solved a streaming bug that had cost me hours. Clean code, zero dependencies, spot-on documentation.',
     'ایجنت-استریم-داکتر یک باگ استریم را حل کرد که ساعت‌ها وقت من را گرفته بود. کد تمیز، بدون وابستگی، مستندات دقیق.',
     'حلّ agent-stream-doctor خطأً في البث كلفني ساعات طويلة. كود نظيف وبدون تبعيات وتوثيق دقيق.', 2),
]

# ---------------------------------------------------------------- summary
CV_SUMMARY = {
    'summary_en': 'Self-taught full-stack developer with strong foundations in Python, C# and JavaScript, and 4 years of '
                  'hands-on experience shipping production-ready software — from AI clinical screening pipelines, '
                  'LLM streaming diagnostics and encrypted desktop messengers to Django platforms deployed on a Linux '
                  'VPS with nginx and gunicorn. Passionate about solving algorithmic and system-level problems and '
                  'building database-driven platforms. Currently completing secondary education (expected graduation '
                  'mid-2028) while freelancing for international clients.',
    'summary_fa': 'توسعه‌دهنده فول‌استکِ خودآموخته با پایه‌ای قوی در پایتون، سی‌شارپ و جاوااسکریپت و ۴ سال تجربهٔ '
                  'عملی در ساخت نرم‌افزارهای آمادهٔ پروداکشن — از خط لوله‌های غربال بالینی مبتنی بر هوش مصنوعی، '
                  'ابزارهای تشخیص خطای استریم LLM و پیام‌رسان‌های رمزنگاری‌شده تا پلتفرم‌های جنگو مستقر روی سرور '
                  'لینوکس با nginx و gunicorn. علاقه‌مند به حل مسائل الگوریتمی و سطح-سیستم و ساخت پلتفرم‌های '
                  'دیتابیس‌محور. در حال تکمیل تحصیلات متوسطه (فراغت: اواسط ۲۰۲۸) و همکاری با مشتریان '
                  'بین‌المللی به‌صورت فریلنس.',
    'summary_ar': 'مطوّر برمجيات متكاملة متعلّم ذاتياً بأساس متين في Python و C# و JavaScript وأربع سنوات من الخبرة '
                  'العملية في بناء برمجيات جاهزة للإنتاج — من خطوط فحص سريري مدعومة بالذكاء الاصطناعي، وأدوات تشخيص '
                  'بث LLM، ورسائل مشفّرة سطح المكتب، إلى منصات Django العاملة على خوادم Linux مع nginx و gunicorn. '
                  'شغوف بحل المشكلات الخوارزمية ومستوى النظام وبناء منصات قائمة على قواعد البيانات. أُكمل حالياً '
                  'التعليم الثانوي (التخرج المتوقع منتصف ٢٠٢٨) وأعمل مستقلاً مع عملاء دوليين.',
}

# ------------------------------------------------------------- experiences
# Six entries. The live database has exactly six; the two "KamanBrowser"
# rows in the old seed were the same project counted twice.
EXPERIENCES = [
    {
        'title_en': 'Kaman AI Translator — Whole-Book PDF & EPUB Translation',
        'title_fa': 'مترجم هوشمند کَمَن — ترجمهٔ کامل کتاب‌های PDF و EPUB',
        'title_ar': 'مترجم كَمَن الذكي — ترجمة كتب PDF وEPUB كاملة',
        'org_en': 'Freelance', 'org_fa': 'فریلنس', 'org_ar': 'عمل حر',
        'period_en': '2024 — 2026', 'period_fa': '۲۰۲۴ — ۲۰۲۶', 'period_ar': '٢٠٢٤ — ٢٠٢٦',
        'description_en': 'Commercial Python desktop application that translates academic and technical PDF/EPUB books into fluent Persian and back into English. Smart paragraph-level chunking with a rolling context tail, a per-book structure template for headings and recurring labels, a QC review loop, per-page job store with pause/resume across restarts, DPAPI-encrypted API keys and 303 offline tests. Windows executable, release v3.0.0.',
        'description_fa': 'اپلیکیشن دسکتاپ تجاری پایتون که کتاب‌های آکادمیک و فنی PDF/EPUB را به فارسی روان و برعکس ترجمه می‌کند. تکه‌تکه‌سازی هوشمند در مرز پاراگراف با کانتکست غلتان، تمپلیت ساختار اختصاصی هر کتاب برای عنوان‌ها و برچسب‌های تکرارشونده، حلقهٔ بازبینی QC، ذخیرهٔ کار هر صفحه با توقف/ادامه پس از ری‌استارت، کلید API رمزنگاری‌شده با DPAPI و ۳۰۳ تست آفلاین. فایل اجرایی ویندوز، نسخهٔ v3.0.0.',
        'description_ar': 'تطبيق سطح مكتب تجاري بلغة Python يترجم الكتب الأكاديمية والفنية PDF/EPUB إلى فارسية سليمة وإلى الإنجليزية. تقسيم ذكي عند حدود الفقرات بسياق متحرك، وقالب بنية خاص لكل كتاب للعناوين والتسميات المتكررة، وحلقة مراجعة QC، ومخزن عمل لكل صفحة مع إيقاف/استئناف بعد إعادة التشغيل، ومفاتيح API مشفّرة بـ DPAPI، و303 اختباراً دون اتصال. ملف تنفيذي لويندوز، إصدار v3.0.0.',
        'order': 1,
    },
    {
        'title_en': 'Agent Stream Doctor — LLM Streaming Diagnostics',
        'title_fa': 'ایجنت استریم داکتر — تشخیص خطای استریم LLM',
        'title_ar': 'Agent Stream Doctor — تشخيص بث LLM',
        'org_en': 'Open Source', 'org_fa': 'متن‌باز', 'org_ar': 'مفتوح المصدر',
        'period_en': '2025 — 2026', 'period_fa': '۲۰۲۵ — ۲۰۲۶', 'period_ar': '٢٠٢٥ — ٢٠٢٦',
        'description_en': 'Zero-dependency Python toolkit that diagnoses why an LLM stream returns nothing: reasoning-only responses, missing finish_reason, malformed SSE framing and truncated tool calls. Twelve named checks, a tolerant parser that turns every malformed deviation into a finding instead of an exception, JSON output for CI and a clean library API. Release v0.2.0.',
        'description_fa': 'جعبه‌ابزار پایتونی بدون وابستگی که علت خالی بودن پاسخ استریم LLM را تشخیص می‌دهد: پاسخ‌های فقط-استدلالی، فقدان finish_reason، فریم‌بندی خراب SSE و فراخوانی ابزار ناقص. ۱۲ بررسی نام‌گذاری‌شده، پارسر مقاوم که هر انحراف خراب را به یافته تبدیل می‌کند نه استثنا، خروجی JSON برای CI و API کتابخانه‌ای تمیز. نسخهٔ v0.2.0.',
        'description_ar': 'عدة Python بدون تبعيات تشخّص سبب عودة بث LLM فارغاً: الردود الاستدلالية فقط، غياب finish_reason، تلف إطارات SSE واستدعاءات الأدوات المبتورة. اثنا عشر فحصاً مسمّاة، ومحلّل متسامٍ يحوّل كل انحراف تالف إلى اكتشاف بدل استثناء، ومخرج JSON للاستخدام في CI، وواجهة مكتبة نظيفة. إصدار v0.2.0.',
        'order': 2,
    },
    {
        'title_en': 'AI Counseling Platform — Widget & Bale Bot',
        'title_fa': 'پلتفرم مشاورهٔ هوشمند — ویجت و ربات بله',
        'title_ar': 'منصة مشورة ذكية — الواجهة والروبوت',
        'org_en': 'Freelance', 'org_fa': 'فریلنس', 'org_ar': 'عمل حر',
        'period_en': '2024', 'period_fa': '۲۰۲۴', 'period_ar': '٢٠٢٤',
        'description_en': 'Built an AI intake system for a counselling centre: a conversational Persian RTL widget and a Bale messenger bot, both running a 12-state guided interview, the GHQ-28 wellbeing screening, clinical concept extraction and a self-learning consultant-matching engine. Fully local — no hosted LLM, no per-message cost, no visitor data leaving the server. Running in production at kahaai.ir.',
        'description_fa': 'برای یک مرکز مشاوره یک سامانهٔ پذیرش هوشمند ساختم: یک ویجت گفتگویی فارسی راست‌چین و یک ربات پیام‌رسان بله، هر دو با ۱۲ وضعیت گفتگوی هدایت‌شده، تست GHQ-28، استخراج مفاهیم بالینی و موتور تطبیق مشاورِ خودآموز. کاملاً محلی — بدون LLM ابری، بدون هزینهٔ هر پیام و بدون خروج دادهٔ مراجع از سرور. در محیط پروداکشن در kahaai.ir.',
        'description_ar': 'بنيت نظام استقبال ذكي لمركز استشارات: واجهة محادثة فارسية كاملة الاتجاه وبوت على مراسلة Bale، كلاهما يشغّل مقابلة موجّهة باثنتي عشرة حالة، وفحص GHQ-28، واستخراج المفاهيم السريرية، ومحرك مطابقة مستشارين يتعلّم بنفسه. محلي بالكامل — دون نموذج سحابي ولا تكلفة لكل رسالة ولا خروج بيانات الزائر من الخادم. يعمل في الإنتاج على kahaai.ir.',
        'order': 3,
    },
    {
        'title_en': 'Educational Website & CMS (Django)',
        'title_fa': 'وب‌سایت آموزشی و سیستم مدیریت محتوا (Django)',
        'title_ar': 'موقع تعليمي ونظام إدارة محتوى (Django)',
        'org_en': 'Client Project', 'org_fa': 'پروژه مشتری', 'org_ar': 'مشروع عميل',
        'period_en': '2023 — 2024', 'period_fa': '۲۰۲۳ — ۲۰۲۴', 'period_ar': '٢٠٢٣ — ٢٠٢٤',
        'description_en': 'Django-based CMS platform with secure user authentication, SQLite storage, multi-format media management (video/audio playback) and dynamic categorized content delivery, deployed with nginx and gunicorn on a Linux VPS.',
        'description_fa': 'پلتفرم CMS مبتنی بر Django با احراز هویت امن، ذخیره‌سازی SQLite، مدیریت رسانه چندقالبه (پخش ویدیو/صوت) و ارائه محتوای پویا و دسته‌بندی‌شده، مستقر با nginx و gunicorn روی سرور لینوکسی.',
        'description_ar': 'منصة CMS مبنية على Django مع مصادقة آمنة، وتخزين SQLite، وإدارة وسائط متعددة الصيغ (تشغيل فيديو/صوت)، وتقديم محتوى ديناميكي مصنّف، منشورة مع nginx و gunicorn على خادم Linux.',
        'order': 4,
    },
    {
        'title_en': 'Planikaa Portal — Educational Platform (Django)',
        'title_fa': 'پورتال پلنیکا — پلتفرم آموزشی (Django)',
        'title_ar': 'بوابة بلانيكا — منصة تعليمية (Django)',
        'org_en': 'Client Project', 'org_fa': 'پروژه مشتری', 'org_ar': 'مشروع عميل',
        'period_en': '2023', 'period_fa': '۲۰۲۳', 'period_ar': '٢٠٢٣',
        'description_en': 'Educational web platform built with Django: exam and competition analysis with visual dashboards, an educational blog, a review and feedback system, django-allauth accounts and Jalali (Persian) calendar support. SQLite is the only database backend the project is configured for.',
        'description_fa': 'پلتفرم وب آموزشی ساخته‌شده با Django: تحلیل آزمون‌ها و مسابقات با داشبوردهای بصری، وبلاگ آموزشی، سیستم نظرات و بازخورد، حساب‌های django-allauth و پشتیبانی از تقویم هجری شمسی. تنها پایگاه دادهٔ پیکربندی‌شده SQLite است.',
        'description_ar': 'منصة ويب تعليمية مبنية على Django: تحليل الاختبارات والمسابقات مع لوحات بصرية، ومدونة تعليمية، ونظام مراجعات وتغذية راجعة، وحسابات django-allauth، ودعم التقويم الهجري الشمسي. قاعدة البيانات الوحيدة المُهيّأة هي SQLite.',
        'order': 5,
    },
    {
        'title_en': 'KamanBrowser — Desktop Web Browser',
        'title_fa': 'کَمَن‌براوزر — مرورگر دسکتاپ',
        'title_ar': 'كَمَن براوزر — متصفح سطح مكتب',
        'org_en': 'Personal Project', 'org_fa': 'پروژه شخصی', 'org_ar': 'مشروع شخصي',
        'period_en': '2022 — 2023', 'period_fa': '۲۰۲۲ — ۲۰۲۳', 'period_ar': '٢٠٢٢ — ٢٠٢٣',
        'description_en': 'Modern desktop web browser built with C# and Windows Forms on Edge WebView2 (Chromium): tab management, bookmarks, custom UI components and smooth navigation with a minimal memory footprint.',
        'description_fa': 'مرورگر دسکتاپ مدرن با C# و Windows Forms روی WebView2 (کرومیوم): مدیریت تب، بوکمارک، کامپوننت‌های سفارشی و ناوبری روان با کمترین مصرف حافظه.',
        'description_ar': 'متصفح ويب حديث بـ C# و Windows Forms على Edge WebView2 (Chromium): إدارة تبويبات وعلامات مرجعية ومكونات واجهة مخصصة وتنقل سلس بأقل استهلاك للذاكرة.',
        'order': 6,
    },
]

EDUCATIONS = [
    {
        'degree_en': 'Secondary Education (High School)',
        'degree_fa': 'تحصیلات متوسطه (دبیرستان)',
        'degree_ar': 'التعليم الثانوي',
        'period_en': 'Expected Graduation: Mid-2028',
        'period_fa': 'فارغ‌التحصیلی پیش‌بینی‌شده: اواسط ۲۰۲۸',
        'period_ar': 'التخرج المتوقع: منتصف 2028',
        'details_en': 'Data Structures & Algorithms\nMachine Learning Fundamentals (freeCodeCamp Track)\nAdvanced Mathematics, Logic and Statistics\nNetworking Concepts (Network+ Preparation)',
        'details_fa': 'ساختار داده و الگوریتم‌ها\nمبانی یادگیری ماشین (دوره freeCodeCamp)\nریاضیات پیشرفته، منطق و آمار\nمفاهیم شبکه (آمادگی Network+)',
        'details_ar': 'هياكل البيانات والخوارزميات\nأساسيات تعلم الآلة (مسار freeCodeCamp)\nرياضيات متقدمة ومنطق وإحصاء\nمفاهيم الشبكات (التحضير لـ Network+)',
        'order': 1,
    },
]

CV_LANGUAGES = [
    ('Persian (Farsi)', 'Native', 'فارسی', 'زبان مادری', 'الفارسية', 'لغة أم', 1),
    ('Arabic', 'Fluent — strong communication', 'عربی', 'مسلط — ارتباط قوی', 'العربية', 'بطلاقة — تواصل قوي', 2),
    ('English', 'Upper-Intermediate', 'انگلیسی', 'بالاتر از متوسط', 'الإنجليزية', 'فوق المتوسط', 3),
]


ARTICLES = [
    {
        'slug': 'why-is-my-llm-stream-empty',
        'icon': '',
        'published': True,
        'order': 0,
        'cover': '',
        'title_en': 'Why is my LLM stream empty? A field guide to broken SSE responses',
        'title_fa': 'چرا استریم LLM من خالی است؟ راهنمای تشخیص پاسخ\u200cهای خراب SSE',
        'title_ar': 'لماذا بث LLM فارغ؟ دليل عملي لاستجابات SSE المعطلة',
        'excerpt_en': 'Reasoning-only replies, missing finish_reason, malformed SSE frames — the four most common reasons a streaming LLM call returns nothing, and how to diagnose each one.',
        'excerpt_fa': 'پاسخ\u200cهای فقط-استدلالی، فقدان finish_reason و فریم\u200cهای خراب SSE — چهار دلیل رایجی که یک فراخوانی استریم LLM خالی برمی\u200cگرداند و روش تشخیص هر کدام.',
        'excerpt_ar': 'ردود استدلالية فقط، غياب finish_reason وإطارات SSE تالف — الأسباب الأربعة الأكثر شيوعاً لعودة استدلال البث فارغاً وكيفية تشخيص كل منها.',
        'body_en': "If you have ever called an OpenAI-compatible API with streaming enabled and received... nothing, you are not alone. After debugging dozens of these cases (and building agent-stream-doctor to automate it), I keep seeing the same four failure modes.\n\n1. Reasoning-only responses. Some models emit their entire answer inside a reasoning channel and mark the content channel as empty. The stream 'works' but your UI shows nothing. Always inspect the delta fields, not just the content.\n\n2. Missing finish_reason. When a proxy truncates the final chunk, finish_reason disappears and many clients silently drop the message. Treat a missing finish_reason as a red flag, not a quirk.\n\n3. Malformed SSE framing. Multi-byte UTF-8 split across chunk boundaries, or a proxy that rewrites 'data:' prefixes, will break parsers quietly. Log raw frames before parsing.\n\n4. Truncated tool calls. Partial tool_call deltas that never merge into a complete call leave your agent hanging. Accumulate and validate arguments before executing.\n\nThe fix is always the same: observe the raw stream first, then reason about the protocol. That is exactly what my diagnostic toolkit does — check it out on GitHub.",
        'body_fa': 'اگر تا به حال با API سازگار با OpenAI و استریم کار کرده باشید و هیچ خروجی نگرفته باشید، تنها نیستید. پس از دیباگ ده\u200cها مورد از این دست (و ساخت ابزار agent-stream-doctor برای خودکارسازی آن)، همیشه چهار حالت خرابی تکراری می\u200cبینم.\n\n۱. پاسخ\u200cهای فقط-استدلالی: برخی مدل\u200cها کل پاسخ را در کانال reasoning می\u200cفرستند و کانال content را خالی می\u200cگذارند. استریم «کار می\u200cکند» ولی رابط کاربری شما چیزی نشان نمی\u200cدهد. همیشه فیلدهای delta را بررسی کنید.\n\n۲. فقدان finish_reason: وقتی پراکسی چانک آخر را قطع می\u200cکند، finish_reason حذف می\u200cشود و خیلی از کلاینت\u200cها بی\u200cصدا پیام را دور می\u200cریزند. نبودِ finish_reason را یک زنگ خطر جدی بدانید.\n\n۳. فریم\u200cبندی خراب SSE: چندبایتی بودن UTF-8 روی مرز چانک\u200cها یا بازنویسی پیشوند data: توسط پراکسی، پارسرها را بی\u200cصدا می\u200cشکند. قبل از پارس، فریم\u200cهای خام را لاگ کنید.\n\n۴. فراخوانی ابزار ناقص: دلتاهای نیمه\u200cکاره tool_call که هرگز کامل نمی\u200cشوند، ایجنت شما را معلق می\u200cگذارند. قبل از اجرا، آرگومان\u200cها را جمع\u200cآوری و اعتبارسنجی کنید.\n\nراه\u200cحل همیشه یکی است: اول استریم خام را ببین، بعد درباره پروتکل فکر کن. جعبه\u200cابزار تشخیصی من دقیقاً همین کار را می\u200cکند — روی گیت\u200cهاب ببینید.',
        'body_ar': 'إذا سبق لك استدعاء API متوافق مع OpenAI مع تمكين البث ولم يتِك شيء، فأنت لست وحدك. بعد تصحيح عشرات الحالات (وبناء أداة agent-stream-doctor لأتمتتها)، أرى دائماً نفس أنماط الفشل الأربعة.\n\n١. الردود الاستدلالية فقط: بعض النماذج ترسل الإجابة كاملة في قناة reasoning وتترك قناة content فارغة. البث «يعمل» لكن واجهتك لا تعرض شيئاً. افحص حقول delta دائماً.\n\n٢. غياب finish_reason: عندما يقتطع البروكسي القطعة الأخيرة يختفي finish_reason ويستكتب عملاء كثيرون الرسالة بصمت. اعتبر غيابه علامة خطر.\n\n٣. تلف إطار SSE: انقسام أحرف UTF-8 متعددة البايتات عبر حدود القطع أو إعادة كتابة البادئة data: تكسر المحللات بصمت. سجّل الإطارات الخام قبل التحليل.\n\n٤. استدعاءات أدوات مبتورة: دلتا tool_call الجزئية التي لا تكتمل تُعلّق الوكيل. جمّع الحجج وتحقق منها قبل التنفيذ.\n\nالحل واحد دائماً: راقب البث الخام أولاً ثم فكّر في البروتوكول. هذا بالضبط ما تفعله أداتي التشخيصية — راجعها على GitHub.',
    },
    {
        'slug': 'building-an-ai-counseling-widget-that-matches-visitors-to-counselors',
        'icon': '',
        'published': True,
        'order': 0,
        'cover': '',
        'title_en': 'Building an AI counseling widget that matches visitors to the right counselor — without a hosted LLM',
        'title_fa': 'ساخت ویجت مشاورهٔ هوشمند: از بازدیدکننده تا مشاور مناسب، بدون LLM ابری',
        'title_ar': 'بناء أداة مشورة ذكية تربط الزائر بالمستشار المناسب — دون نموذج لغوي سحابي',
        'excerpt_en': "A drop-in Persian RTL chat widget that runs a structured intake, administers the GHQ-28 wellbeing screen, extracts clinical concepts from free text and ranks counselors — with every clinic's own API key, admin panel and intake flow. No hosted model, no per-message cost, nothing leaving the server.",
        'excerpt_fa': 'ویجت چت فارسی و راست\u200cچین که با یک تگ اسکریپت روی سایت کلینیک می\u200cنشیند: مصاحبهٔ ساختاریافته، تست GHQ-28، استخراج مفاهیم بالینی از متن آزاد و رتبه\u200cبندی مشاوران. بدون مدل ابری، بدون هزینهٔ پیام، و بدون خروج داده از سرور.',
        'excerpt_ar': 'أداة محادثة فارسية كاملة الاتجاه تدمج عبر وسم واحد: مقابلة منظمة، وفحص GHQ-28، واستخراج المفاهيم السريرية من النص الحر، وترتيب المرشحين — بمفتاح خاص بكل مركز، ولوحة إدارة، ودون نموذج سحابي أو تكلفة لكل رسالة.',
        'body_en': 'A counseling center\'s website usually does two things badly: it makes a visitor fill in a form, and it makes the visitor phone to ask whether anyone is free. Both are slow, and both lose people.\n\nI wanted to find out what it would take to replace that with a single embedded chat bubble that does the triage itself. The result is the AI Counseling Widget — a Persian, right-to-left intake assistant that a clinic drops onto its site with one `<script>` tag.\n\n## The constraint that shaped everything\n\nThe interesting decision was not the interface. It was what runs behind it.\n\nThere is no hosted language model here. The "AI" is a local, deterministic engine: a curated clinical lexicon that maps free text to concepts, fuzzy counselor-name matching, age-bound parsing, weighted scoring over a roster, and a feedback table that re-weights future matches. A visitor\'s words never leave the server, there is no vendor API key, and there is no per-message cost.\n\nThat decision buys three things that matter for mental-health tooling specifically. It removes a third-party data processor from the path of sensitive disclosures. It makes the per-message cost zero, so a clinic can run this on a small budget. And it makes the behaviour auditable — every recommendation comes with a stated reason instead of a plausible-sounding sentence.\n\n## What the visitor actually gets\n\nA floating bubble opens a 380×580 panel, which goes fullscreen under 480 pixels. The conversation is a state machine over numbered steps — `text`, `phone`, `number`, or `choice` — with optional conditional steps and two possible endings. Nothing about that flow is hardcoded.\n\nThe steps themselves are edited live from the clinic\'s admin panel, so the centre can change its intake questions, reorder them, add a branch, or switch the ending from "recommend a counselor" to "capture a lead" without a redeploy. A tenant may also list the domains its widget may be embedded on; the check is an exact host or subdomain match, deliberately not a substring match, so `notexample.org` cannot impersonate `example.org`.\n\nTwo validation rules are worth calling out because they are the kind of detail that decides whether a form feels hostile. A phone number must be exactly eleven digits starting with `09`, and Persian numerals are converted before the check — a visitor typing ۰۹ is not rejected for typing in their own script. A suspicious-looking number is treated as a warning, not a rejection: the intake continues, because a blocked number means a person who needs help gets no help.\n\n## The screening step is optional, and it is a screen, not a diagnosis\n\nIf the tenant enables it, the widget offers the GHQ-28 wellbeing instrument: 28 questions across four subscales — somatic, anxiety, social and depression. Answers are scored server-side and interpreted into bands, with the main warning at a total of 43 or above, or a depression subscale of 15 or above, and a milder warning from a total of 22.\n\nThe distinction the code insists on is that this is a screening instrument, not a diagnosis. The widget presents it that way, and so does the matching engine, which never tells a visitor what condition they have. It extracts concepts, scores, ranks, and explains.\n\n## Ranking two counselors out of a roster\n\nThe matching engine applies hard filters first — gender, branch, age bounds, and a legal-specialty guard — and then scores what survives on topic fit, extracted clinical concepts, ability, live free-slot count, and a learned per-counselor weight. It returns the top two, each with a reason in plain language and a booking link.\n\nThe learned weight is the part that makes it a product rather than a demo. Every rating in the panel, and every successful recommendation, adjusts a per-(tenant, counselor, concept) weight within a bounded range. The clinic\'s own staff, by rating a recommendation, are retraining the matcher.\n\nEleven clinical concepts sit at the centre of this — anxiety, depression, obsessive-compulsive symptoms, relationships and interpersonal conflict, couple and marriage, parent and child, child, adolescent and young adult, personal development, legal, and medical/psychiatric. The synonym lexicon is curated and readable, and a contributor can extend it.\n\n## The lead is written before the match runs\n\nThis is a small change with a large consequence. The request is persisted before matching executes, so a visitor who needs a counselor is recorded even when the engine finds no match at all. Earlier behaviour dropped them, and a dropped lead is a person who reached out and got silence.\n\n## The clinic\'s side\n\nThe admin panel is the other half of the product: a dashboard, a full conversation inbox, a lead table, a conflict-resolution screen, a flow editor, a consultant roster manager, feedback, crawler control, and a super-admin area for tenant management. Leads export to a two-sheet Excel workbook — `Users` and `Request history` — with frozen headers and Persian formatting.\n\nAvailability is kept fresh by a background crawler that scrapes the centre\'s public team pages every two hours, with retry, backoff and a direct-connection fallback. Booking URLs are mapped per counselor, and slot counts feed straight into the ranking, so the engine prefers someone the visitor can actually book.\n\n## How it is secured\n\nPasswords are hashed with PBKDF2-HMAC-SHA256 at 100,000 iterations with a 16-byte salt, stored as `salt$hex_digest`. Sessions are signed cookies with `httponly` and `samesite=lax`. Responses carry `nosniff`, `strict-origin-when-cross-origin`, and `X-Frame-Options: SAMEORIGIN` — except on `/widget`, which has to be embeddable.\n\nRate limiting is real: 30 requests per minute per client IP and session token on the chat API, and 10 failed panel logins per IP per five minutes. The tenant API key is the tenant identity — it scopes the flow, the roster, the learning weights and the leads, and it rotates from the super-admin panel, with the widget picking up the new key on the next page load.\n\n## The stack, and the one rule that is not negotiable\n\nFastAPI 0.115.6 with uvicorn 0.34.0, Jinja2 for the panel, SQLite for storage, APScheduler for the crawl and the session GC, and vanilla JavaScript and CSS for the widget itself — no framework, no bundler, no npm. The widget ships as three static files.\n\nThe rule that is not negotiable: **one worker.** The scheduler jobs live in the process, and the rate-limit counters are in memory. Multiple workers would start multiple crawlers and split the counters. Scale vertically until the scheduler moves out of the process.\n\n## What I would build next\n\nThe honest next step is not a bigger model. It is better data: a real evaluation set of intake conversations with the recommendations a good counsellor would actually make, so the ranking can be measured instead of argued about. Everything else — a second flow branch, a richer panel — is comparatively easy.\n\nThe full technical documentation is published as a wiki: the architecture, the API reference, the matching engine, the GHQ screening, the admin panel, deployment, and troubleshooting. The source is on GitHub under the MIT license.\n\n- [Source code and setup on GitHub](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget)\n- [Read the full technical wiki](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget/wiki)\n\n**Related:** the messenger version of the same engine — a Bale bot with the same GHQ screen and matching logic — is covered in a separate article on this site.',
        'body_fa': 'سایت یک مرکز مشاوره معمولاً دو کار را بد انجام می\u200cدهد: از بازدیدکننده فرم پر می\u200cکند، و مجبورش می\u200cکند تلفن بزند تا بپرسد کسی وقت خالی دارد یا نه. هر دو کندند و هر دو آدم\u200cها را از دست می\u200cدهند.\n\nمی\u200cخواستم بدانم جایگزینی برای این با یک حباب چت تعبیه\u200cشده که خودش تریاژ را انجام می\u200cدهد چه هزینه\u200cای دارد. نتیجه، ویجت مشاورهٔ هوشمند است: یک دستیار مصاحبهٔ فارسی و راست\u200cچین که کلینیک با یک تگ `<script>` روی سایتش می\u200cگذارد.\n\n## محدودیتی که همه\u200cچیز را شکل داد\n\nتصمیم مهم، رابط کاربری نبود. آنچه پشت آن اجرا می\u200cشود بود.\n\nاینجا هیچ مدل زبانی ابری وجود ندارد. «هوش مصنوعی» یک موتور محلی و قطعی است: یک واژگان بالینی پالایش\u200cشده که متن آزاد را به مفاهیم نگاشت می\u200cکند، تطبیق فازی نام مشاور، تجزیهٔ بازهٔ سنی، امتیازدهی وزنی روی فهرست مشاوران، و یک جدول بازخورد که وزن\u200cهای آینده را بازتنظیم می\u200cکند. حرف بازدیدکننده هرگز از سرور خارج نمی\u200cشود، هیچ کلید API فروشنده\u200cای در کار نیست، و هزینهٔ هر پیام صفر است.\n\nاین تصمیم سه چیز را برای ابزار سلامت روانی ممکن می\u200cکند: یک پردازش\u200cگر دادهٔ شخص ثالث را از مسار افشای حساس حذف می\u200cکند، هزینهٔ هر پیام را صفر می\u200cکند — که برای کلینیکی با بودجهٔ کوچک تعیین\u200cکننده است — و رفتار سیستم را قابل حسابرسی می\u200cکند: هر پیشنهاد با یک دلیل صریح می\u200cآید، نه با جمله\u200cای که فقط خوش\u200cآهنگ به نظر می\u200cرسد.\n\n## بازدیدکننده دقیقاً چه می\u200cگیرد\n\nیک حباب شناور که پنلی ۳۸۰×۵۸۰ باز می\u200cکند، و زیر ۴۸۰ پیکسل تمام\u200cصفحه می\u200cشود. گفتگو یک ماشین حالت روی گام\u200cهای شماره\u200cدار است — `text`، `phone`، `number` یا `choice` — با گام\u200cهای شرطی اختیاری و دو پایان ممکن. هیچ\u200cکدام از این\u200cها ثابت کدنویسی نشده است.\n\nخودِ گام\u200cها از پنل مدیریت کلینیک زنده ویرایش می\u200cشوند: مرکز می\u200cتواند سؤال\u200cهای مصاحبه را عوض کند، ترتیبشان را جابه\u200cجا کند، یک شاخه اضافه کند، یا پایان جریان را از «پیشنهاد مشاور» به «ثبت لید» تغییر دهد — بدون redeploy. هر tenant می\u200cتواند دامنه\u200cهای مجاز برای embed شدن ویجت را هم فهرست کند؛ این بررسی تطبیق دقیق host یا subdomain است، عمداً نه تطبیق زیررشته\u200cای، تا `notexample.org` نتواند خود را جای `example.org` جا بزند.\n\nدو قاعدهٔ اعتبارسنجی ارزش گفتن دارند، چون همین جزئیات تعیین می\u200cکند فرم حساس به نظر برسد یا نه. شمارهٔ تماس باید دقیقاً ۱۱ رقم و با `09` شروع شود، و ارقام فارسی پیش از بررسی تبدیل می\u200cشوند — یعنی بازدیدکننده\u200cای که ۰۹ می\u200cنویسد، به\u200cخاطر نوشتن با خط خودش رد نمی\u200cشود. شمارهٔ مشکوک فقط هشدار است نه رد: مصاحبه ادامه پیدا می\u200cکند، چون شمارهٔ بلاک\u200cشده یعنی کسی که کمک لازم دارد کمکی نگرفت.\n\n## مرحلهٔ غربال اختیاری است، و غربال است نه تشخیص\n\nاگر tenant آن را فعال کند باشد، ویجت پرسش\u200cنامهٔ سلامت عمومی GHQ-28 را پیشنهاد می\u200cدهد: ۲۸ سؤال در چهار زیرمقیاس — جسمانی، اضطراب، اجتماعی و افسردگی. پاسخ\u200cها سمت سرور نمره\u200cگذاری و به بازه تفسیر می\u200cشوند؛ هشدار اصلی در نمرهٔ کل ۴۳ به بالا یا زیرمقیاس افسردگی ۱۵ به بالا، و هشدار ملایم\u200cتر از نمرهٔ کل ۲۲.\n\nتمایزی که کد روی آن اصرار دارد این است که این یک ابزار غربال است، نه تشخیص. ویجت همین\u200cطور ارائه\u200cاش می\u200cکند و موتور تطبیق هم همین\u200cطور: هرگز به بازدیدکننده نمی\u200cگوید چه اختلالی دارد. مفهوم استخراج می\u200cکند، امتیاز می\u200cدهد، رتبه\u200cبندی می\u200cکند و توضیح می\u200cدهد.\n\n## رتبه\u200cبندی دو مشاور از میان یک فهرست\n\nموتور تطبیق اول فیلترهای سخت را اعمال می\u200cکند — جنسیت، شعبه، بازهٔ سنی و محافظت تخصص حقوقی — و بعد آنچه باقی مانده را روی تناسب موضوع، مفاهیم بالینی استخراج\u200cشده، توانمندی، تعداد نوبت خالی زنده و وزن یادگرفته\u200cشدهٔ هر مشاور امتیاز می\u200cدهد. خروجی، دو مشاور برتر است، هرکدام با دلیلی به زبان ساده و لینک رزرو.\n\nوزن یادگرفته\u200cشده همان بخشی است که این را از دمو به محصول تبدیل می\u200cکند. هر امتیازدهی در پنل و هر توصیهٔ موفق، وزنِ (tenant، مشاور، مفهوم) را در یک بازهٔ بسته تنظیم می\u200cکند. یعنی کارکنان خود کلینیک، با امتیاز دادن به یک پیشنهاد، موتور تطبیق را دوباره آموزش می\u200cدهند.\n\nدر مرکز این کار یازده مفهوم بالینی قرار دارد: اضطراب، افسردگی، وسواس، روابط و تعارض بین\u200cفردی، زوج و ازدواج، والد و فرزند، کودک، نوجوان و جوان، توسعهٔ فردی، حقوقی، و پزشکی-روانپزشکی. واژگان مترادف پالایش\u200cشده و خوانا است و هر مشارکت\u200cکننده\u200cای می\u200cتواند آن را گسترش دهد.\n\n## لید پیش از اجرای تطبیق نوشته می\u200cشود\n\nاین تغییر کوچک اما پیامد بزرگی دارد. درخواست پیش از اجرای تطبیق ذخیره می\u200cشود، پس کسی که به مشاور نیاز دارد حتی وقتی موتور هیچ تطبیقی پیدا نمی\u200cکند هم ثبت می\u200cشود. رفتار قبلی آن\u200cها را دور می\u200cریخت، و لیدِ افتاده یعنی کسی که کمک خواست و جواب نگرفت.\n\n## سمت کلینیک\n\nپنل مدیریت نیمهٔ دیگر محصول است: داشبورد، صندوق کامل گفتگوها، جدول لیدها، صفحهٔ حل تعارض، ویرایشگر جریان، مدیر فهرست مشاوران، بازخورد، کنترل خزنده، و بخش super-admin برای مدیریت tenantها. لیدها به یک فایل Excel دو شیتی صادر می\u200cشوند — `Users` و `Request history` — با سربرگ\u200cهای ثابت و قالب\u200cبندی فارسی.\n\nتازگی نوبت\u200cها را یک خزندهٔ پس\u200cزمینه تأمین می\u200cکند که هر دو ساعت صفحات عمومی تیم مرکز را می\u200cخواند، با retry، backoff و fallback اتصال مستقیم. لینک رزرو برای هر مشاور نگاشت می\u200cشود و تعداد slot مستقیماً وارد رتبه\u200cبندی می\u200cشود، پس موتور کسی را ترجیح می\u200cدهد که بازدیدکننده واقعاً می\u200cتواند رزرو کند.\n\n## امنیت چطور است\n\nرمزهای عبور با PBKDF2-HMAC-SHA256 و ۱۰۰٬۰۰۰ تکرار و salt شانزده\u200cبایتی هش می\u200cشوند و به شکل `salt$hex_digest` ذخیره می\u200cشوند. نشست\u200cها کوکی\u200cهای امضاشده با `httponly` و `samesite=lax` هستند. پاسخ\u200cها `nosniff`، `strict-origin-when-cross-origin` و `X-Frame-Options: SAMEORIGIN` می\u200cفرستند — به\u200cجز `/widget` که باید قابل embed باشد.\n\nمحدودسازی نرخ واقعی است: ۳۰ درخواست در دقیقه به\u200cازای هر IP کلاینت و توکن نشست روی API چت، و ۱۰ تلاش ناموفق ورود به پنل در هر ۵ دقیقه به\u200cازای هر IP. کلید API مربوط به tenant خودش هویت tenant است — جریان، فهرست مشاوران، وزن\u200cهای یادگیری و لیدها را محدود می\u200cکند — و از پنل super-admin قابل چرخش است، و ویجت کلید جدید را در بارگذاری بعدی برمی\u200cدارد.\n\n## پشتهٔ فنی، و یک قانون غیرقابل مذاکره\n\nFastAPI 0.115.6 با uvicorn 0.34.0، Jinja2 برای پنل، SQLite برای ذخیره\u200cسازی، APScheduler برای خزنده و GC نشست\u200cها، و جاوااسکریپت و CSS خالص برای خود ویجت — بدون فریم\u200cورک، بدون باندلر، بدون npm. ویجت در قالب سه فایل استاتیک تحویل می\u200cشود.\n\nقانونی که قابل مذاکره نیست: **یک worker.** jobهای زمان\u200cبندی داخل همان پروسه\u200cاند و شمارنده\u200cهای محدودسازی نرخ در حافظه. چند worker یعنی چند خزنده و شمارنده\u200cهای تقسیم\u200cشده. تا وقتی زمان\u200cبند از پروسه بیرون نرود، عمودی مقیاس بدهید.\n\n## قدم بعدی چه باشد\n\nقدم بعدیِ صادقانه مدل بزرگ\u200cتر نیست. دادهٔ بهتر است: یک مجموعه\u200cارزیابی واقعی از گفتگوهای مصاحبه، همراه با پیشنهادهایی که یک مشاور خوب واقعاً می\u200cداد، تا رتبه\u200cبندی به\u200cجای بحث\u200cکردن اندازه\u200cگیری شود. بقیهٔ کارها — یک شاخهٔ دوم جریان، پنل غنی\u200cتر — نسبتاً ساده\u200cاند.\n\nکل مستندات فنی به\u200cصورت ویکی منتشر شده است: معماری، مرجع API، موتور تطبیق، غربال GHQ، پنل مدیریت، استقرار و عیب\u200cیابی. سورس روی GitHub با مجوز MIT.\n\n- [سورس کد و راهنمای راه\u200cاندازی روی GitHub](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget)\n- [مطالعهٔ کامل ویکی فنی](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget/wiki)\n\n**مرتبط:** نسخهٔ پیام\u200cرسانِ همین موتور — یک ربات بل با همان غربال GHQ و همان منطق تطبیق — در مقاله\u200cای جداگانه در همین سایت آمده است.',
        'body_ar': 'تالمواقع心理咨询常常Identifier بطريقتين سيئتين: يملأ الزائر نموذجاً، ويجبره على الاتصال هاتفياً ليسأل هل يوجد متاح. كلا الأمرين بطيء وكلاهما يفقد الناس.\n\nأردت أن أعرف تكلفة استبدال ذلك بفقاعة محادثة مدمجة تؤمّن الفرز بنفسها. جاءت النتيجة أداة المشورة الذكية: مساعد مقابلة فارسي كامل الاتجاه يضعه المركز في موقعه بوسم `<script>` واحد.\n\n## القيد الذي شكّل كل شيء\n\nلم يكن القرار المهم في الواجهة، بل فيما يعمل خلفها.\n\nلا يوجد هنا أي نموذج لغوي سحابي.所谓 «الذكاء» محرك محلي حتمي: مسرد سريري منقّح يربط النص الحر بالمفاهيم، ومطابقة ضبابية لأسماء المستشارين، وتحليل حدود العمر، وتسجيل مرجّح على قائمة المستشارين، وجدول تغذية راجعة يعيد ضبط الأوزان المستقبلية. كلام الزائر لا يغادر الخادم، ولا يوجد مفتاح API لمزوّد، ولا تكلفة لكل رسالة.\n\nهذا القرار يشتري ثلاثة أمور مهمة تحديداً لأدوات الصحة النفسية: يلغي معالج بيانات خارجياً من مسار الإفصاحات الحساسة، ويجعل تكلفة الرسالة صفراً — وهو ما يناسب مركزاً بميزانية صغيرة — ويجعل السلوك قابلاً للتدقيق: كل توصية تأتي بسبب مذكور لا بجملة تبدو معقولة فقط.\n\n## ما الذي يحصل عليه الزائر\n\nفقاعة عائمة تفتح لوحة ٣٨٠×٥٨٠، تصبح ملء الشاشة تحت ٤٨٠ بكسل. الحوار آلة حالات فوق خطوات مرقّمة — `text` أو `phone` أو `number` أو `choice` — مع خطوات شرطية اختيارية ونهايتين محتملتين. لا شيء من ذلك مكتوب بشكل ثابت.\n\nالخطوات نفسها تُحرَّر مباشرة من لوحة إدارة المركز، فيغيّر أسئلة المقابلة أو يعيد ترتيبها أو يضيف فرعاً أو يحوّل النهاية من «اقترح مستشاراً» إلى «سجّل طلباً» دون إعادة نشر. وقد يسرد كل مستأجر النطاقات المسموح بضمّ الأداة فيها؛ والفحص مطابقة دقيقة للمضيف أو نطاق فرعي، وليس مطابقة لسلسلة فرعية عمداً، حتى لا تستطيع `notexample.org` انتحال `example.org`.\n\nقاعدتا تحقّق تستحقان الذكر، لأن هذه التفاصيل هي التي تقرّر إن بدا النموذج معادياً أم لا. يجب أن يتكوّن رقم الهاتف من أحد عشر رقماً بالضبط يبدأ بـ `09`، وتُحوَّل الأرقام الفارسية قبل الفحص — فلا يُرفض زائر كتب ٠٩ لأنه كتب بلغته. والرقم المريب يبقى تحذيراً لا رفضاً: تتابع المقابلة، لأن الرقم المحظور يعني شخصاً يحتاج المساعدة ولم يحصل عليها.\n\n## خطوة الفحص اختيارية، وهي فحص لا تشخيص\n\nإن فعّلها المستأجر، تعرض الأداة استبيان GHQ-28: ٢٨ سؤالاً في أربعة مقاييس فرعية — جسدي، قلق، اجتماعي، اكتئاب. تُصحَّح الإجابات على الخادم وتُفسَّر إلى نطاقات، مع التحذير الرئيسي عند مجموع ٤٣ فأكثر أو مقياس الاكتئاب ١٥ فأكثر، وتحذير أهدأ من مجموع ٢٢.\n\nالتمييز الذي يصرّ عليه الكود أن هذا استبيان فحص لا تشخيص. تعرض الأداة الأمر كذلك، وكذلك محرّك المطابقة الذي لا يخبر الزائر أبداً بأي اضطراب لديه؛ فهو يستخرج المفاهيم ويقيّم ويرتّب ويشرح.\n\n## ترتيب مستشارين من قائمة\n\nيطبّق محرّك المطابقة أولاً المرشّحات الصارمة — الجنس والفرع وحدود العمر وحماية التخصص القانوني — ثم يقيّم ما بقي على تناسب الموضوع والمفاهيم السريرية المستخرجة والقدرة وعدد المواعيد المتاحة الحيّة والوزن المتعلَّم لكل مستشار. ويعيد أعلى مستشارين، لكلٍّ منهما سبب بلغة واضحة ورابط حجز.\n\nالوزن المتعلَّم هو ما يحوّل هذا من عرض تجريبي إلى منتج: كل تقييم في اللوحة وكل توصية ناجحة تعدّل وزن (المستأجر، المستشار، المفهوم) ضمن نطاق محدود. أي أن موظفي المركز نفسه — بتقييمهم توصية — يعيدون تدريب المحرّك.\n\nمركز هذه المنظومة أحد عشر مفهوماً سريرياً: القلق، الاكتئاب، وسواس الطهار، العلاقات والخلافات بين الأفراد، الزوجية والزواج، الوالد والطفل، الطفل، المراهق والشاب، التطوير الذاتي، القانوني، والطبي النفسي. المسرد المنقّح مقروء، ويمكن لأي مساهم توسيعه.\n\n## يُكتب الطلب قبل تشغيل المطابقة\n\nهذا تغيير صغير بنتيجة كبيرة. يُحفظ الطلب قبل تنفيذ المطابقة، فيسجَّل من يحتاج مستشاراً حتى حين لا يجد المحرّك أي تطابق. السلوك السابق كان يُسقطه، وطلبٌ مُسقَط يعني شخصاً طلب المساعدة فلم يسمع رداً.\n\n## جانب المركز\n\nلوحة الإدارة هي النصف الآخر من المنتج: لوحة مؤشرات، وصندوق محادثات كامل، وجدول طلبات، وشاشة حل تعارضات، ومحرّر تدفّق، ومدير قائمة المستشارين، وتغذية راجعة، وتحكّم في الزاحف، ومنطقة مدير عام لإدارة المستأجرين. وتُصدَّر الطلبات إلى مصنّف Excel من ورقة واحدة—`Users` و`Request history`— برؤوس مجمّدة وتنسيق فارسي.\n\nويحرّك زاحف في الخلفية تحديث التوفّر بقراءة صفحات الفريق العامة كل ساعتين، مع إعادة محاولة وتدرّج وانتقال احتياطي للاتصال المباشر. وتُربط روابط الحجز بكل مستشار، وتدخل أعداد المواعيد مباشرة في الترتيب، فيفضّل المحرّك من يمكن حجزه فعلاً.\n\n## كيف يكون الأمان\n\nتُجزّأ كلمات المرور بـ PBKDF2-HMAC-SHA256 عند مئة ألف تكرار بملح ١٦ بايت، وتُخزَّن بصيغة `salt$hex_digest`. والجلسات كوكيز موقّعة بـ `httponly` و`samesite=lax`. وتحمل الردود `nosniff` و`strict-origin-when-cross-origin` و`X-Frame-Options: SAMEORIGIN` — باستثناء `/widget` الذي يجب أن يكون قابلاً للضمّ.\n\nوحدّ المعدّل واقعي: ٣٠ طلباً في الدقيقة لكل عنوان IP وتوكن جلسة على واجهة المحادثة، و١٠ محاولات فاشلة للدخول إلى اللوحة لكل IP كل خمس دقائق. ومفتاح API للمستأجر هو هوية المستأجر نفسه — فهو يقيّد التدفّق وقائمة المستشارين وأوزان التعلّم والطلبات — ويمكن تدويره من لوحة المدير العام، فتلتقط الأداة المفتاح الجديد عند التحميل التالي.\n\n## الحزمة التقنية، وقاعدة واحدة غير قابلة للتفاوض\n\nFastAPI 0.115.6 مع uvicorn 0.34.0، وJinja2 للوحة، وSQLite للتخزين، وAPScheduler للزاحف وتنظيف الجلسات، وJavaScript وCSS خامان للأداة نفسها — بلا إطار عمل ولا حزم بناء ولا npm. وتُسلَّم الأداة في ثلاثة ملفات ثابتة.\n\nالقاعدة غير القابلة للتفاوض: **عامل واحد.** مهام الجدولة تعيش داخل العملية، وعدّادات حدّ المعدّل في الذاكرة. فعدة عمّال تعني عدة زواحف وعدّادات موزّعة. وسّع رأسياً حتى تُخرَج الجدولة من العملية.\n\n## ما الذي سأبنيه تالياً\n\nالخطوة التالية الصادقة ليست نموذجاً أكبر، بل بيانات أفضل: مجموعة تقييم حقيقية من حوارات Intake مع التوصيات التي كان مستشار جيد سيقدّمها فعلاً، ليقاس الترتيب بدل أن يُتنازع عليه. وكل ما عدا ذلك — فرع ثانٍ للتدفّق، أغنى لوحة — سهل نسبياً.\n\nالوثائق التقنية الكاملة منشورة كويكي: البنية، ومرجع الواجهة، ومحرّك المطابقة، وفحص GHQ، ولوحة الإدارة، والنشر، واستكشاف الأخطاء. والمصدر على GitHub برخصة MIT.\n\n- [الشيفرة المصدرية ودليل الإعداد على GitHub](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget)\n- [قراءة الويكي التقني الكامل](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-widget/wiki)\n\n**ذو صلة:** نسخة المراسلة من المحرّك نفسه — روبوت على بل بالشاشة نفسها ومنطق المطابقة نفسه — تتناولها مقالة منفصلة في هذا الموقع.',
    },
    {
        'slug': 'shipping-a-counseling-bot-on-bale-with-ghq-28-screening-and-self-learning-matching',
        'icon': '',
        'published': True,
        'order': 0,
        'cover': '',
        'title_en': 'Shipping a counseling bot on Bale: GHQ-28 screening, self-learning matching and 12 conversation states',
        'title_fa': 'ساخت ربات مشاوره روی بل: تست GHQ-28، تطبیق یادگیرنده و ۱۲ وضعیت گفتگو',
        'title_ar': 'بناء روبوت مشورة على بل: فحص GHQ-28 ومطابقة تتعلم ذاتياً واثنتي عشرة حالة حوار',
        'excerpt_en': 'How a messenger bot can run a full clinical intake end to end — a 12-state conversation handler, the GHQ-28 wellbeing screen, a matching engine that re-weights itself from panel feedback, an availability crawler and a full admin panel inside the chat itself. Built on the Telegram-compatible Bale API.',
        'excerpt_fa': 'چطور یک ربات پیام\u200cرسان می\u200cتواند کل مسیر مشاوره را اجرا کند: ۱۲ وضعیت گفتگو، تست GHQ-28، موتور تطبیقی که از بازخورد پنل خودش را بازتنظیم می\u200cکند، خزندهٔ نوبت\u200cهای خالی و پنل مدیریت کامل داخل خود گفتگو.',
        'excerpt_ar': 'كيف يستطيع روبوت مراسلة تنفيذ مسار استشاري كاملاً: معالج حوار باثنتي عشرة حالة، وفحص GHQ-28، ومحرك مطابقة يعيد ضبط نفسه من تغذية راجعة اللوحة، وزاحف تفرّغ المواعيد، ولوحة إدارة كاملة داخل المحادثة نفسها.',
        'body_en': 'Every counseling bot I could find was a funnel: a menu, a form, a "book now" button. That works until the visitor has to describe a problem in their own words, which is exactly the step a menu cannot do.\n\nSo I built the opposite: a messenger bot that runs a real clinical intake in a conversation, screens the person, and then ranks the counselors that fit — with the ranking engine inside the bot, not behind a vendor API.\n\n## The platform choice, and why it is a Telegram-compatible one\n\nThe bot runs on **Bale**, an Iranian messenger, and is implemented with `python-telegram-bot==22.8` pointed at `https://tapi.bale.ai/bot`. That is deliberate: Bale exposes a Telegram-compatible HTTP API, so the whole ecosystem around `python-telegram-bot` — handlers, `ConversationHandler`, filters, the scheduler — applies unchanged. The product is a Bale bot; the library is the Telegram library.\n\nThis matters more than it sounds. The `ConversationHandler` is the piece that makes a multi-step intake possible, and it is a mature, well-understood component rather than something hand-rolled. It also means the code is portable: the same handlers would run against Telegram\'s API with a changed base URL and token.\n\n## Twelve states, one conversation\n\nThe intake is a `ConversationHandler` with twelve states: name, phone, gender, age, topic, previous therapy, details of previous therapy, expectation, preferred counselor gender, branch, the GHQ-28 offer, and the GHQ-28 question itself. Each state has its own handler and its own validation.\n\nThe design detail worth noting is the cancellation path. `/cancel` and a message matching `شروع مجدد` both abort the conversation cleanly, and the fallback handler returns the user to the start rather than leaving them in a half-finished state — the thing that makes messenger bots feel hostile when it goes wrong.\n\n## The screen, offered and interpreted server-side\n\nThe GHQ-28 stage is the same instrument the widget uses: 28 questions across four subscales — somatic, anxiety, social and depression — scored server-side and interpreted into bands. The main warning fires at a total of 43 or above, or a depression subscale of 15 or above; a milder warning starts at a total of 22.\n\nWhat the bot will not do is diagnose. The output is presented as a screening signal, and the recommendation is advisory — the user makes the final choice. That distinction is in the code, not just in the disclaimer.\n\n## The matching engine, and how it learns\n\n`SpiralMatchEngine` runs two passes. The first is hard filters: gender, branch, age bounds. The second is weighted scoring across topic fit, extracted clinical concepts, and live free-slot count. It returns a shortlist, and every entry comes with a "why this match" line — topic fit, age group, and a slot the person can actually book.\n\nConcept extraction maps free text to eleven clinical concepts — anxiety, depression, obsessive-compulsive symptoms, relationships and conflict, couple and marriage, parent and child, child, adolescent and young adult, personal development, legal, and medical/psychiatric — using a curated synonym dictionary that includes Persian and Arabic variants. Name matching is fuzzy, so a visitor\'s spelling of a counselor\'s name does not have to be exact — spacing, Arabic/Persian letter variants and nicknames are all handled. Age ranges are parsed out of the free-text topic string, so "برای کودک ۷ ساله" and "نوجوان" land on the right roster rows.\n\nThe learning loop is the part that turns a ranking function into a product. Every recommendation, and every admin rating through `/feedback`, writes to `ai_knowledge.db` as a positive or negative signal. Those signals re-weight future matches. `/learning` prints the current weights, so the training is inspectable rather than a black box.\n\n## Availability without scraping a page by hand\n\nA scheduled crawler refreshes open-slot counts every two hours by reading the centre\'s public team page, with proxy fallback, retry logic, and a lock file that prevents overlapping runs. The counts feed the ranking, so the engine prefers counselors the user can actually book. `/crawl` triggers it on demand.\n\n## The admin panel lives inside the chat\n\nThis is the part I like most, because it removes an entire web application from the deployment. The admin enters `/admin` with a password and gets a menu: `/stats` for live statistics, `/export` for a two-sheet Excel export of users and request history, `/upload` to replace the counselors spreadsheet — which hot-reloads the engine without a restart — `/broadcast` to message every user with a confirmation step, `/crawl` to run the crawler now, `/feedback` and `/learning` to train and inspect the engine, `/myid` to get the Bale user ID, and `/logout` to end the session.\n\nBecause the admin surface is a bot, the whole operational footprint is one process, one SQLite file set and one environment variable set. Access is restricted by `ADMIN_USER_IDS` — a comma-separated list of Bale user IDs — with a separate `ADMIN_PANEL_PASSWORD` and `BOT_TOKEN`. No secret is stored in the code; all three are read from the environment.\n\n## Storage, honestly\n\nSix tables across three SQLite databases: `users`, `user_requests`, `consultants` and `upload_history` in the user database, `appointments` for slot availability, and `concept_feedback` for the learning weights. The roster is loaded from a spreadsheet, converted to JSON, and can be rebuilt from Excel at any time.\n\n## What I would build next\n\nThe honest next step is evaluation again, and it applies here too. The engine can be argued about; what it needs is a labelled set of intake cases with the ranking a good counsellor would have produced, so a change to the weights can be measured instead of assumed. A second useful addition would be a reminder path for people who were screened and then went quiet — the data to support it is already there.\n\nThe full technical documentation is published as a wiki: the architecture, the matching engine, the GHQ screening, the admin panel, setup and deployment, contributing, and troubleshooting. The source is on GitHub under the MIT license.\n\n- [Source code and setup on GitHub](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot)\n- [Read the full technical wiki](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot/wiki)\n\n**Related:** the same engine ships as an embeddable web widget with a full multi-tenant admin panel — that article is on this site too.',
        'body_fa': 'هر ربات مشاوره\u200cای که پیدا می\u200cکردم یک قیف بود: منو، فرم، دکمهٔ «همین حالا رزرو کن». تا وقتی بازدیدکننده لازم داشته مشکلش را با کلمات خودش توصیف کند کار می\u200cکند — و دقیقاً همان مرحله\u200cای که منو نمی\u200cتواند انجامش دهد.\n\nپس برعکسش را ساختم: رباتی که یک مصاحبهٔ بالینی واقعی را در قالب گفتگو اجرا می\u200cکند، فرد را غربال می\u200cکند، و بعد مشاورانی را که به وضعیتش می\u200cخورند رتبه\u200cبندی می\u200cکند — با موتور رتبه\u200cبندی داخل خود ربات، نه پشت یک API فروشنده.\n\n## انتخاب پلتفرم، و اینکه چرا سازگار با تلگرام است\n\nربات روی **بل**، یک پیام\u200cرسان ایرانی، اجرا می\u200cشود و با `python-telegram-bot==22.8` روی `https://tapi.bale.ai/bot` پیاده شده. این عمدی است: بل یک HTTP API سازگار با تلگرام ارائه می\u200cدهد، پس کل اکوسیستم `python-telegram-bot` — هندلرها، `ConversationHandler`، فیلترها، زمان\u200cبند — بدون تغییر کار می\u200cکند. محصول یک ربات بل است؛ کتابخانه، کتابخانهٔ تلگرام.\n\nاین بیشتر از آنچه به نظر می\u200cرسد اهمیت دارد. `ConversationHandler` همان قطعه\u200cای است که مصاحبهٔ چندمرحله\u200cای را ممکن می\u200cکند، و یک مؤلفهٔ بالغ و جاافتاده است نه چیزی که دستی ساخته شده باشد. یعنی کد هم قابل حمل است: همان هندلرها با تغییر base URL و توکن روی API تلگرام هم اجرا می\u200cشوند.\n\n## دوازده وضعیت، یک گفتگو\n\nمصاحبه یک `ConversationHandler` با دوازده وضعیت است: نام، تلفن، جنسیت، سن، موضوع، سابقهٔ درمان، جزئیات سابقهٔ درمان، انتظار، جنسیت مشاور ترجیحی، شعبه، پیشنهاد GHQ-28، و خود سؤال GHQ-28. هر وضعیت هندلر و اعتبارسنجی خودش را دارد.\n\nجزئیات طراحی که ارزش گفتن دارد مسیر لغو است. `/cancel` و پیامی که با `شروع مجدد` م��خواند هر دو گفتگو را تمیز قطع می\u200cکنند، و هندلر fallback کاربر را به شروع برمی\u200cگرداند — همان چیزی که وقتی خراب می\u200cشود ربات\u200cها را ناخوشایند می\u200cکند.\n\n## غربال، پیشنهادی و تفسیرشده سمت سرور\n\nمرحلهٔ GHQ-28 همان ابزاری است که ویجت هم استفاده می\u200cکند: ۲۸ سؤال در چهار زیرمقیاس — جسمانی، اضطراب، اجتماعی و افسردگی — که سمت سرور نمره\u200cگذاری و به بازه تفسیر می\u200cشود. هشدار اصلی در نمرهٔ کل ۴۳ به بالا یا زیرمقیاس افسردگی ۱۵ به بالا فعال می\u200cشود؛ هشدار ملایم\u200cتر از نمرهٔ کل ۲۲ شروع می\u200cشود.\n\nکاری که ربات انجام نمی\u200cدهد، تشخیص دادن است. خروجی به\u200cعنوان یک سیگنال غربال ارائه می\u200cشود و پیشنهاد جنبهٔ مشورتی دارد — انتخاب نهایی با خود کاربر است. این تفکیک در کد هست، نه فقط در متن بیانیهٔ بیانیه.\n\n## موتور تطبیق، و اینکه چطور یاد می\u200cگیرد\n\n`SpiralMatchEngine` دو پاس دارد. پاس اول فیلترهای سخت است: جنسیت، شعبه، بازهٔ سنی. پاس دوم امتیازدهی وزنی روی تناسب موضوع، مفاهیم بالینی استخراج\u200cشده و تعداد نوبت خالی زنده. خروجی یک فهرست کوتاه است و هر مورد با خط «چرا این پیشنهاد» می\u200cآید — تناسب موضوع، گروه سنی، و نوبتی که فرد واقعاً می\u200cتواند رزرو کند.\n\nاستخراج مفهوم متن آزاد را با فرهنگ لغت مترادفِ پالایش\u200cشده به یازده مفهوم بالینی — اضطراب، افسردگی، وسواس، روابط و تعارض، زوج و ازدواج، والد و فرزند، کودک، نوجوان و جوان، توسعهٔ فردی، حقوقی، و پزشکی-روانپزشکی — نگاشت می\u200cکند و تنوع\u200cهای فارسی و عربی را هم پوشش می\u200cدهد. تطبیق نام فازی است، پس املای نام مشاور توسط بازدیدکننده لازم نیست دقیق باشد — فاصله\u200cگذاری، تفاوت حروف عربی/فارسی و لقب\u200cها همه مدیریت می\u200cشوند. بازهٔ سنی از رشتهٔ موضوع آزاد استخراج می\u200cشود، پس «برای کودک ۷ ساله» و «نوجوان» روی درست\u200cترین ردیف\u200cهای فهرست می\u200cنشینند.\n\nحلقهٔ یادگیری همان چیزی است که یک تابع رتبه\u200cبندی را به محصول تبدیل می\u200cکند. هر توصیه و هر امتیازدهی ادمین از طریق `/feedback` به\u200cعنوان سیگنال مثبت یا منفی در `ai_knowledge.db` نوشته می\u200cشود، و این سیگنال\u200cها وزن\u200cهای آینده را بازتنظیم می\u200cکنند. `/learning` وزن\u200cهای فعلی را چاپ می\u200cکند، پس آموزش قابل بازرسی است نه جعبهٔ سیاه.\n\n## نوبت خالی بدون اسکرپ دستی صفحه\n\nیک خزندهٔ زمان\u200cبندی\u200cشده هر دو ساعت تعداد نوبت\u200cهای خالی را با خواندن صفحهٔ عمومی تیم مرکز به\u200cروز می\u200cکند، با fallback پروکسی، منطق retry، و یک فایل lock که از اجراهای هم\u200cزمان جلوگیری می\u200cکند. این تعدادها وارد رتبه\u200cبندی می\u200cشوند، پس موتور کسی را ترجیح می\u200cدهد که کاربر واقعاً می\u200cتواند رزرو کند. `/crawl` هم آن را دستی اجرا می\u200cکند.\n\n## پنل مدیریت داخل خود گفتگو\n\nاین بخشی است که از همه بیشتر دوستش دارم، چون یک اپ وب کامل را از استقرار حذف می\u200cکند. ادمین با `/admin` و رمز عبور وارد می\u200cشود و یک منو می\u200cگیرد: `/stats` برای آمار زنده، `/export` برای خروجی Excel دو شیتی از کاربران و تاریخچهٔ درخواست\u200cها، `/upload` برای جایگزینی فایل Excel مشاوران — که موتور را بدون restart داغ بارگذاری می\u200cکند —، `/broadcast` برای پیام به همهٔ کاربران با مرحلهٔ تأیید، `/crawl` برای اجرای فوری خزنده، `/feedback` و `/learning` برای آموزش و بازرسی موتور، `/myid` برای گرفتن شناسهٔ کاربری بل، و `/logout` برای پایان نشست.\n\nچون پنل مدیریت خودش یک ربات است، کل footprint عملیاتی در یک پروسه، یک مجموعه فایل SQLite و یک مجموعه متغیر محیطی خلاصه می\u200cشود. دسترسی با `ADMIN_USER_IDS` — فهرستی جداشده با کاما از شناسه\u200cهای کاربری بل — محدود می\u200cشود، به\u200cعلاوهٔ `ADMIN_PANEL_PASSWORD` و `BOT_TOKEN` جدا. هیچ secretی در کد ذخیره نمی\u200cشود؛ هر سه از محیط خوانده می\u200cشوند.\n\n## ذخیره\u200cسازی، صادقانه\n\nشش جدول در سه پایگاه دادهٔ SQLite: `users`، `user_requests`، `consultants` و `upload_history` در پایگاه کاربران، `appointments` برای توفّر نوبت\u200cها، و `concept_feedback` برای وزن\u200cهای یادگیری. فهرست مشاوران از یک فایل spreadsheet بارگذاری و به JSON تبدیل می\u200cشود و هر زمان قابل بازسازی از Excel است.\n\n## قدم بعدی چه باشد\n\nقدم بعدیِ صادقانه باز هم ارزیابی است و اینجا هم همین\u200cطور. موتور را می\u200cشود درباره\u200cاش بحث کرد؛ چیزی که لازم دارد مجموعه\u200cای برچسب\u200cخورده از سناریوهای مصاحبه همراه با رتبه\u200cبندی\u200cای است که یک مشاور خوب می\u200cداد، تا تغییر وزن\u200cها اندازه\u200cگیری شود نه فرض. اضافهٔ مفید دیگر مسیر یادآوری برای کسانی است که غربال شدند و بعد ساکت شدند — داده\u200cاش از قبل هست.\n\nکل مستندات فنی به\u200cصورت ویکی منتشر شده است: معماری، موتور تطبیق، غربال GHQ، پنل مدیریت، راه\u200cاندازی و استقرار، مشارکت در توسعه، و عیب\u200cیابی. سورس روی GitHub با مجوز MIT.\n\n- [سورس کد و راهنمای راه\u200cاندازی روی GitHub](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot)\n- [مطالعهٔ کامل ویکی فنی](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot/wiki)\n\n**مرتبط:** همین موتور به\u200cشکل یک ویجت وب تعبیه\u200cشدنی با پنل مدیریت چندمستاجری کامل هم عرضه می\u200cشود — آن مقاله هم در همین سایت هست.',
        'body_ar': 'كل روبوت مشورة وجدته كان قمعاً: قائمة، ثم نموذج، ثم زر «احجز الآن». يعمل هذا حتى يحتاج الزائر إلى وصف مشكلته بكلماته، وهي بالضبط الخطوة التي لا تستطيع القائمة أداؤها.\n\nفبنيت العكس: روبوت ينفّذ مقابلة سريرية حقيقية في حوار، ويفحص الشخص، ثم يرتّب المستشارين المناسبين — بمحرك ترتيب داخل الروبوت نفسه، لا خلف واجهة مزوّد.\n\n## اختيار المنصّة، ولماذا متوافقة مع تيليغرام\n\nيعمل الروبوت على **بل**، وهي خدمة مراسلة إيرانية، ومُنفَّذ بـ `python-telegram-bot==22.8` موجَّه إلى `https://tapi.bale.ai/bot`. Это مقصود: توفّر بل واجهة HTTP متوافقة مع تيليغرام، فتعمل منظومة `python-telegram-bot` كاملةً — المعالِجات و`ConversationHandler` والمرشّحات والمجدول — دون تغيير. المنتج روبوت بل؛ والمكتبة مكتبة تيليغرام.\n\nهذا أهمّ مما يبدو. فـ`ConversationHandler` هو القطعة التي تجعل مقابلة متعدّدة الخطوات ممكنة، وهو مكوّن ناضج ومفهوم، لا شيء مبنيّ يدوياً. كما يعني ذلك أن الشيفرة قابلة للنقل: المعالِجات نفسها تعمل على واجهة تيليغرام بتغيير عنوان القاعدة والمفتاح.\n\n## اثنتا عشرة حالة، حوار واحد\n\nالمقابلة معالج حوار `ConversationHandler` باثنتي عشرة حالة: الاسم، الهاتف، الجنس، العمر، الموضوع، سوابق العلاج، تفاصيل السابقة، التوقّع، جنس المستشار المفضّل، الفرع، عرض GHQ-28، وسؤال GHQ-28 نفسه. لكل حالة معالِجها وتحقّقها الخاص.\n\nالتفصيل التصميمي الذي يستحق الذكر هو مسار الإلغاء. فكل من `/cancel` والرسالة المطابقة لـ`شروع مجدد` يقطعان الحوار بهدوء، ويعيد معالج الاحتياط المستخدم إلى البداية بدل تركه في حالة نصف منتهية — وهو ما يجعل روبوتات المراسلة غير ودّية حين ينكسر شيء.\n\n## الفحص، معروض ومفسر على الخادم\n\nمرحلة GHQ-28 هي الأداة نفسها التي تستخدمها أداة الويب: ٢٨ سؤالاً في أربعة مقاييس — جسدي، قلق، اجتماعي، اكتئاب — تُصحَّح على الخادم وتُفسَّر إلى نطاقات. وينطلق التحذير الرئيسي عند مجموع ٤٣ فأكثر أو مقياس اكتئاب ١٥ فأكثر، ويبدأ تحذير أهدأ من مجموع ٢٢.\n\nوما لا يفعله الروبوت هو التشخيص. تُعرض النتيجة بوصفها إشارة فحص، والتوصية استشارية — والاختيار النهائي للمستخدم. وهذا التمييز في الشيفرة، لا في免责声明 فحسب.\n\n## محرّك المطابقة، وكيف يتعلّم\n\nيعمل `SpiralMatchEngine` على مرحلتين. الأولى مرشّحات صارمة: الجنس والفرع وحدود العمر. والثانية تسجيل مرجّح على تناسب الموضوع والمفاهيم السريرية المستخرجة وعدد المواعيد المتاحة الحيّة. ويعيد قائمة مختصرة، ويأتي كل عنصر مع سطر «لماذا هذا المطابق» — تناسب الموضوع والفئة العمرية وموعد يمكن حجزه فعلاً.\n\nواستخراج المفاهيم يربط النص الحر بأحد عشر مفهوماً سريرياً — القلق، الاكتئاب، وسواس الطهار، العلاقات والخلافات، الزوجية والزواج، الوالد والطفل، الطفل، المراهق والشاب، التطوير الذاتي، القانوني، والطبي النفسي — عبر قاموس مترادفات منقّح يشمل تنوعات فارسية وعربية. والمطابقة بالأسماء ضبابية، فليست كتابة الزائر لاسم المستشار مطلوبة بدقة — فالتشكيل وتنوعات الحروف العربية/الفارسية والألقاب كلها مُعالَجة. وتُستخرج حدود العمر من نص الموضوع الحرّ، فيستقر «لطفل عمره ٧ سنوات» و«مراهق» على الصفوف الصحيحة من القائمة.\n\nوإنّ حلقة التعلّم هي ما يحوّل دالة ترتيب إلى منتج. فكل توصية، وكل تقييم من المشرف عبر `/feedback`، يُكتب في `ai_knowledge.db` كإشارة موجبة أو سالبة، وتعيد تلك الإشارات ضبط أوزان المطابقات القادمة. ويطبع `/learning` الأوزان الحالية، فيصبح التدريب قابلاً للفحص لا صندوقاً أسود.\n\n## التوفّر دون كشط الصفحة يدوياً\n\nيعيد زاحف مجدول تحديث أعداد المواعيد المتاحة كل ساعتين بقراءة صفحة الفريق العامة، مع بديل عبر الوسيط ومنطق إعادة المحاولة وملف قفل يمنع تشغيلات متداخلة. وتدخل هذه الأعداد في الترتيب، فيفضّل المحرّك من يمكن للمستخدم حجزه. ويشغّل `/crawl` ذلك عند الطلب.\n\n## لوحة الإدارة داخل المحادثة\n\nهذا هو الجزء الذي أحبّه أكثر، لأنه يلغي تطبيق ويب كاملاً من النشر. يدخل المشرف بـ`/admin` مع كلمة مرور فيحصل على قائمة: `/stats` للإحصاءات الحيّة، و`/export` لتصدير Excel من ورقتين للمستخدمين وسجل الطلبات، و`/upload` لاستبدال ملف المستشارين — الذي يعيد تحميل المحرّك بلا إعادة تشغيل —، و`/broadcast` لمراسلة كل المستخدمين مع خطوة تأكيد، و`/crawl` لتشغيل الزاحف فوراً، و`/feedback` و`/learning` لتدريب المحرّك وفحصه، و`/myid` للحصول على معرّف المستخدم في بل، و`/logout` لإنهاء الجلسة.\n\nولأن سطح الإدارة روبوت، فإن البصمة التشغيلية كلها عملية واحدة ومجموعة ملفات SQLite واحدة ومجموعة متغيّرات بيئة واحدة. ويُقيَّد الوصول عبر `ADMIN_USER_IDS` — قائمة بمعرّفات مستخدمي بل مفصولة بفواصل — مع `ADMIN_PANEL_PASSWORD` و`BOT_TOKEN` منفصلين. ولا يُخزَّن أي سرّ في الشيفرة؛ الثلاثة تُقرأ من البيئة.\n\n## التخزين، بصدق\n\nستة جداول في ثلاث قواعد SQLite: `users` و`user_requests` و`consultants` و`upload_history` في قاعدة المستخدمين، و`appointments` لتوفّر المواعيد، و`concept_feedback` لأوزان التعلّم. وتُحمَّل قائمة المستشارين من جدول بيانات ثم تُحوَّل إلى JSON، ويمكن إعادة بنائها من Excel في أي وقت.\n\n## ما الذي سأبنيه تالياً\n\nالخطوة التالية الصادقة هي التقييم أيضاً، وهنا كذلك. يمكن الجدال في المحرّك؛ ما يحتاجه مجموعة حالات موسومة من المقابلات مع الترتيب الذي كان مستشار جيد سيقدّمه، ليقيس تغيير الأوزان بدل افتراضه. وإضافة مفيدة أخرى مسار تذكير لمن أُجري لهم الفحص ثم سكتوا —بياناته متاحة أصلاً.\n\nالوثائق التقنية الكاملة منشورة كويكي: البنية، ومحرّك المطابقة، وفحص GHQ، ولوحة الإدارة، والإعداد والنشر، والمساهمة، واستكشاف الأخطاء. والمصدر على GitHub برخصة MIT.\n\n- [الشيفرة المصدرية ودليل الإعداد على GitHub](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot)\n- [قراءة الويكي التقني الكامل](https://github.com/Mohammad-Hasan-Kaman/ai-counseling-bot/wiki)\n\n**ذو صلة:** المحرّك نفسه يصدر أيضاً كأداة ويب مدمجة بلوحة إدارة متعدّدة المستأجرين — وهذه المقالة موجودة في هذا الموقع أيضاً.',
    },
    {
        'slug': 'building-a-persian-first-desktop-translator-for-pdf-and-epub-books',
        'icon': '',
        'published': True,
        'order': 0,
        'cover': '',
        'title_en': 'Building a Persian-first desktop translator for PDF and EPUB books — chunking, rolling context, and a per-book structure template',
        'title_fa': 'ساخت یک ترجمه\u200cگر دسکتاپ فارسی\u200cمحور برای کتاب\u200cهای PDF و EPUB: تکه\u200cتکه\u200cسازی، کانتکست غلتان و تمپلیت ساختار هر کتاب',
        'title_ar': 'بناء مترجم سطح مكتب لفحات PDF وEPUB: تقسيم المقاطع، وسياق متحرك، وبنية خاصة لكل كتاب',
        'excerpt_en': 'Translating a 300-page book in a chat window fails in predictable ways: the model summarizes instead of translating, terminology drifts between chapters, running headers become translated garbage, and one crash loses an hour of work. This is a Windows desktop app that fixes each of those with local, readable code — paragraph-aware chunking, a rolling context tail, per-book structure templates, a DPAPI-encrypted key, and a job store that saves every finished page.',
        'excerpt_fa': 'ترجمهٔ یک کتاب ۳۰۰ صفحه\u200cای در پنجرهٔ چت شکست\u200cهای قابل پیش\u200cبینی دارد: مدل به\u200cجای ترجمه خلاصه می\u200cکند، اصطلاحات بین فصل\u200cها عوض می\u200cشود، سرصفحه\u200cهای تکراری به متن ترجمه\u200cشدهٔ بی\u200cمعنا تبدیل می\u200cشوند و یک کرش، یک ساعت کار را از بین می\u200cبرد. این اپ دسکتاپ ویندوزی هر کدام را با کدی محلی و خوانا حل می\u200cکند: تکه\u200cتکه\u200cسازی روی مرز پاراگراف، کانتکست غلتان، تمپلیت ساختار برای هر کتاب، کلید رمز\u200cشده با DPAPI و ذخیرهٔ کار که هر صفحهٔ تمام\u200cشده را نگه می\u200cدارد.',
        'excerpt_ar': 'فشل ترجمة كتاب من 300 صفحة داخل نافذة محادثة أمر متوقع: النموذج يلخص بدل أن يترجم، والمصطلحات تتفاوت بين الفصول، وتحوّل ترويسات الصفحات المتكررة إلى نص مترجم بلا معنى، وتفقد ساعة عمل كاملة عند أي تعطّل. هذا تطبيق سطح مكتب لويندوز يعالج كلاً من ذلك بشفرة محلية مقروءة: تقسيم المقاطع عند حدود الفقرات، وسياق مترجم متحرك، وبنية خاصة لكل كتاب، ومفتاح مشفّر بـ DPAPI، ومخزن يحفظ كل صفحة مكتملة فوراً.',
        'body_en': 'Translating a 300-page book in a chat window fails in predictable ways. The model summarizes when you asked for a translation. Terminology drifts from chapter to chapter, so the same term appears under three different Persian words. Running headers and page numbers get translated as if they were content. And one crashed session throws away an hour of work.\n\nI wanted to find out what it takes to do this properly, so I built **Kaman AI Translator** — a Windows desktop app that translates PDF and EPUB books page by page into academic Persian, and back into English, with the boring failure modes handled by local code you can read.\n\nThe repository is two Python files and a test suite. The interesting part is not the interface; it is the pipeline underneath it.\n\n## The constraint that shaped everything\n\nThe "AI" is not a hosted service inside the app. It is a thin, replaceable engine layer — the official Google Gemini SDK, or any OpenAI-compatible endpoint (Ollama, LM Studio, llama.cpp, or a cloud aggregator).\n\nThat matters because the translation *strategy* — chunking, context rolling, structure templates, quality control — is local, deterministic code. The model is a tool the strategy calls; it is never the thing making the decisions. That is why the entire pipeline can be tested headlessly with a fake engine and no API key.\n\n## Chunking that never cuts a sentence in half\n\nLong input is the first thing that breaks. The default character budget is **6,000** per request, and the splitter works in three tiers: paragraph boundaries first, then sentence boundaries, then words — never mid-sentence.\n\nThe units are then repacked under the budget, so a request is not wasted on a single oversized paragraph, and no chunk arrives full of fragments.\n\n**A rolling context tail** rides along with each chunk: the last **700 characters** of the previous translation are appended to the prompt, so terminology and prose flow stay consistent across a chapter instead of restarting every page. The setting can be set to zero to turn it off entirely, but the default is on, because it is the single cheapest quality improvement in the whole app.\n\n## The per-book structure template\n\nThe most interesting piece of local logic answers a specific problem: how do you stop the same recurring label from being translated five different ways across a book?\n\nThe app detects, **per book, locally and for free**, two things:\n\n- **Headings** — a chapter title should read as a chapter title, not as body text.\n- **Recurring labels** — things like "Did you know?" or "Activities" that appear dozens of times and must render identically every single time.\n\nBoth are injected into every prompt for that book, so the label is always translated the same way. They are editable by hand in a template editor, and an optional AI pass can read the table of contents and extract a deeper structure for **one extra API request**.\n\nThe detection is cheap: lines that repeat on at least a quarter of the sampled pages near the top or bottom edge of a page are treated as running headers and dropped **before the model ever sees them**. Hyphen-broken words are rejoined — `exam-` plus `ple` becomes `example` — and list numbers and mid-text formulas are protected.\n\n## Completeness-enforcing prompts, and a second pass that checks the work\n\nThe prompts are explicit that a translation must not omit, must not summarize, and must preserve paragraph structure, numbers, equations and citation markers like `[12]`, with one consistent term per concept.\n\nThen there is an optional **QC loop**: a second pass compares the translation against its own source text, flags meaning drift and omissions, and returns a corrected version. It is genuinely a second call, and the interface says so — the cost of the QC pass is roughly double.\n\nThere is also a **JSON-safety layer**. Models sometimes reply with raw JSON, or with a JSON object wrapped in prose. Those replies are unwrapped, repaired, or accepted as plain text, so the user never sees JSON garbage in the output box.\n\n## Scanned pages are not skipped\n\nA scanned book has no text layer. Naive translation treats an empty page as an empty page, and a 300-page scan becomes a 300-page gap.\n\nHere, completely empty extracted text triggers a different path: the page is rendered as a PNG at a **2× zoom** (roughly 144 DPI) and sent to a vision-capable model that reads it and translates it in one step.\n\nTwo honest limits are worth stating. The provider must accept images — a text-only local model cannot do this, which is one reason the scanned path practically points at Gemini. And because the page has no extracted source text, **the QC loop is skipped for scanned pages**: there is nothing independent to verify the translation against. Those pages deserve a human "Reviewed" mark more than text pages do.\n\n## Nothing is lost, ever\n\nThe property I cared about most is that finished work is never lost — not to a crash, not to a quota stop, not to a restart.\n\nEvery book has a JSON state file, named by a hash of its absolute path, written **atomically after every single page**: the data is written to a temporary file and then `os.replace`d into position, so the file is never observed half-written even if the process is killed mid-save. A `threading.Lock` guards the operation.\n\nWhen you reopen a book with saved pages, the app asks an explicit question — continue from the first unfinished page, or start over from the beginning — and **continue is the default**. The structure template survives even a restart, because the book has not changed and re-detecting it would be waste.\n\nThe cost of a lost run is at most the page that was in flight.\n\n## The key is encrypted, and the app talks to nothing else\n\nThe API key is entered once in the settings dialog, masked in the UI, and stored **encrypted with Windows DPAPI** — the Windows Data Protection API, bound to your user account and your machine. A different user on the same machine, or the same user on a different machine, cannot decrypt it.\n\nThere is a fallback for platforms without DPAPI, and the app does not hide it: the key falls back to clearly-labelled base64 storage, and the reason is written to `encrypt_fallback.log` — a timestamp and the error message, **never any part of the secret**. Base64 is encoding, not encryption, and the project says so rather than pretending otherwise.\n\nThe complete network surface is one row: **the provider you configured**. There is no telemetry, no update checker, no crash reporting, no third-party service, and no analytics. The settings dialog shows the exact data folder path and has a one-click button to open it.\n\nIf you want nothing to leave the machine at all, point the OpenAI-compatible provider at Ollama on localhost — that is what the default base URL (`http://localhost:11434/v1`) is for.\n\n## The interface is Persian, and that means RTL all the way down\n\nThis is not an English layout with Persian strings. The whole application is right-to-left, with Persian numerals throughout (`۰۱۲۳۴۵۶۷۸۹`).\n\nThat has real consequences, and they are asserted by the test suite rather than left to chance:\n\n- "Next page" points **left** and "previous" points **right**, because that is the direction of travel in RTL.\n- The source panel is added first in the layout, so it lands on the **right** — where a Persian reader expects the original text.\n- The progress percentage is right-aligned, and the progress bar\'s internal text is hidden because Qt draws it on the left.\n- Spin-box values are right-aligned through a dedicated filter, re-applied on theme changes, because Qt re-lays-out spin boxes and loses the alignment otherwise.\n- The copy button is **blue when the current page has a translation and grey when it does not**, so its state is readable without a tooltip.\n\nDuring a long run the app follows the page being translated, live — but **page navigation stays fully unlocked**. The moment you browse somewhere yourself, the app stops moving the view for you. The batch keeps running; only the auto-follow steps aside.\n\n## Three exports\n\nWhen the book is done, the save menu offers three formats:\n\n- **One page as TXT**, with a header naming the book and the page number, written as `utf-8-sig` so Persian renders correctly in Windows Notepad instead of as mojibake.\n- **The whole book as Markdown**, one `##` section per page in numeric order — version-controllable and diffable.\n- **The whole book as a standalone RTL HTML edition** with a page image beside every translation, inline CSS, and print rules that stop a page from splitting across a printed sheet. Open it in a browser and *Print → Save as PDF* gives a finished Persian PDF with the original page images.\n\nThe HTML route is a deliberate choice: producing a correct right-to-left PDF requires embedding a Persian font and handling bidi layout properly, which a browser already does well. Direct PDF output with embedded RTL font rendering is on the project\'s roadmap, but the HTML export is good today, and it uses the fonts the user already has.\n\n## What I would build next\n\nThe honest next step is not a better model. It is better data: a real evaluation set of books with the translations a good human translator would produce, so the quality of the pipeline can be measured rather than argued about. A glossary export and import — one term list shared across several books — is the feature I would add first, because consistency across a series of books is the thing per-book templates cannot solve.\n\n## The numbers, and where they come from\n\n| Fact | Value |\n|---|---|\n| Application version | 3.0.0 |\n| Core | `kaman_core.py`, ~1,400 lines, Qt-free |\n| UI | `translator_app_v3.py`, ~1,800 lines |\n| Test suite | **302 checks, all passing, fully offline** |\n| Runtime dependencies | 4 — PyQt6, PyMuPDF, Pillow, google-genai |\n| Default chunk budget | 6,000 characters |\n| Default context tail | 700 characters |\n| Scanned-page render | 2× matrix (≈144 DPI) |\n| Key protection | Windows DPAPI, with a logged base64 fallback |\n| Releases | `v3.0.0` (Windows executable + source zip), `v2.0.0` |\n\nThe test suite runs with no network, no API key and no provider account: fake engines stand in, and the user\'s real profile is never touched because `APPDATA` is redirected to a temporary folder before the app modules are imported. A run prints **302 passing checks and zero failures** — that is the measured number, not a rounded-up one.\n\nThe full technical documentation is published as a wiki: the architecture, the translation pipeline, the engines, the structure templates, the scanned-page path, the job store, the exports, the interface, the settings, the security model, the test suite, and the release process.\n\n- [Source code and setup on GitHub](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator)\n- [Read the full technical wiki](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator/wiki)\n- [Download the Windows executable](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator/releases/latest)\n\n**Related:** the same site documents a Persian counseling widget and a messenger bot built on the same ideas — a local, auditable engine with a hosted model only where it earns its place.',
        'body_fa': 'ترجمهٔ یک کتاب ۳۰۰ صفحه\u200cای در پنجرهٔ چت، شکست\u200cهای قابل پیش\u200cبینی دارد. وقتی ترجمه خواسته\u200cای، مدل خلاصه می\u200cکند. اصطلاحات از فصلی به فصل دیگر عوض می\u200cشوند و یک مفهوم، با سه واژهٔ فارسی مختلف ظاهر می\u200cشود. سرصفحه\u200cها و شماره\u200cهای صفحه هم مثل متن اصلی ترجمه می\u200cشوند. و یک نشستِ کرشی، یک ساعت کار را از بین می\u200cبرد.\n\nمی\u200cخواستم بدانم برای انجام درست این کار چه چیزی لازم است، پس **Kaman AI Translator** را ساختم — یک اپ دسکتاپ ویندوزی که کتاب\u200cهای PDF و EPUB را صفحه\u200cبه\u200cصفحه به فارسی دانشگاهی ترجمه می\u200cکند و برعکس، با شکست\u200cهای تکراری که با کد محلی و خوانا حل شده\u200cاند.\n\nریپو دو فایل پایتون و یک مجموعه تست است. بخش جالبش رابط کاربری نیست؛ خط لولهٔ زیر آن است.\n\n## محدودیتی که همه\u200cچیز را شکل داد\n\n«هوش مصنوعی» اینجا یک سرویس میزبان\u200cشده درون اپ نیست. یک لایهٔ موتور نازک و قابل\u200cتعویض است — SDK رسمی گوگل جیمینی، یا هر endpoint سازگار با OpenAI (Ollama، LM Studio، llama.cpp، یا یک تجمیع\u200cکنندهٔ ابری).\n\nاین تفاوت مهم است چون *استراتژی* ترجمه — تکه\u200cتکه\u200cسازی، غلتان کانتکست، تمپلیت ساختار، کنترل کیفیت — کد محلی و قطعی است. مدل ابزاری است که این استراتژی صدایش می\u200cزند؛ هیچ\u200cوقت چیزی نیست که تصمیم بگیرد. به همین دلیل است که کل خط لوله بدون سرور، با یک موتور جعلی و بدون کلید API، قابل تست است.\n\n## تکه\u200cتکه\u200cسازی که جمله را نصف نمی\u200cکند\n\nورودی بلند اولین چیزی است که خراب می\u200cشود. بودجهٔ پیش\u200cفرض هر درخواست **۶۰۰۰** کاراکتر است و شکافنده در سه سطح کار می\u200cکند: اول مرز پاراگراف، بعد مرز جمله، و بعد کلمه — هرگز وسط جمله.\n\nسپس واحدها زیر بودجه دوباره بسته\u200cبندی می\u200cشوند، پس یک درخواست صرفاً صرفِ یک پاراگراف بزرگ نمی\u200cشود و هیچ تکه\u200cای پر از تکه\u200cهای ناقص به مدل نمی\u200cرسد.\n\n**دنبالهٔ کانتکست غلتان** همراه هر تکه می\u200cرود: **۷۰۰** کاراکتر آخر ترجمهٔ قبلی به پرامپت اضافه می\u200cشود تا اصطلاحات و لحن در طول یک فصل یکدست بمانند و هر صفحه از صفر شروع نشود. این تنظیم را می\u200cشود صفر کرد و کل قابلیتش را خاموش کرد، ولی پیش\u200cفرض روشن است چون ارزان\u200cترین بهبود کیفیت در کل اپ است.\n\n## تمپلیت ساختار مخصوص هر کتاب\n\nجذاب\u200cترین بخش منطق محلی، پاسخ به یک مشکل مشخص است: چطور جلوی ترجمه\u200cشدن یک برچسب تکراری به پنج شکل مختلف در یک کتاب را بگیریم؟\n\nاپ، **برای هر کتاب، به\u200cصورت محلی و رایگان**، دو چیز را تشخیص می\u200cدهد:\n\n- **سرفصل\u200cها** — عنوان فصل باید مثل عنوان فصل خوانده شود، نه مثل متن بدنه.\n- **برچسب\u200cهای تکراری** — چیزهایی مثل «آیا می\u200cدانید؟» یا «فعالیت\u200cها» که ده\u200cها بار می\u200cآیند و باید هر بار دقیقاً یکسان ترجمه شوند.\n\nهر دو در پرامپتِ هر درخواستِ آن کتاب تزریق می\u200cشوند، پس هر برچسب همیشه یکسان ترجمه می\u200cشود. هر دو دستی هم قابل ویرایش\u200cاند، و یک پاس AI اختیاری می\u200cتواند فهرست مطالب را بخواند و ساختار عمیق\u200cتری استخراج کند — با **یک درخواست API اضافه**.\n\nتشخیص ارزان است: خط\u200cهایی که دست\u200cکم در یک\u200cچهارم صفحات نمونه\u200cشده، نزدیک لبهٔ بالا یا پایین صفحه تکرار شوند، سرصفحهٔ تکراری در نظر گرفته می\u200cشوند و **پیش از آنکه مدل آن\u200cها را ببیند** حذف می\u200cشوند. کلماتی که با خط تیره شکسته شده\u200cاند دوباره به هم چسبانده می\u200cشوند — `exam-` به\u200cعلاوهٔ `ple` می\u200cشود `example` — و شمارهٔ فهرست\u200cها و فرمول\u200cهای میان\u200cمتن محافظت می\u200cشوند.\n\n## پرامپت\u200cهای الزام\u200cآور و یک دور دوم که کار را بررسی می\u200cکند\n\nپرامپت\u200cها صریح\u200cاند: ترجمه نباید حذف کند، نباید خلاصه کند، و باید ساختار پاراگراف، اعداد، معادلات و نشانه\u200cهای ارجاع مثل `[12]` و یک اصطلاح ثابت برای هر مفهوم را حفظ کند.\n\nبعد از آن، یک **حلقهٔ QC** اختیاری هست: یک دور دوم ترجمه را با متن مبدأ خودش مقایسه می\u200cکند، لغزش معنایی و حذف\u200cها را علامت می\u200cزند و نسخهٔ اصلاح\u200cشده برمی\u200cگرداند. این واقعاً یک فراخوانی دوم است و رابط کاربری هم همین را می\u200cگوید — هزینهٔ این پاس تقریباً دوبرابر است.\n\nیک **لایهٔ ایمنی JSON** هم هست. مدل\u200cها گاهی با JSON خام یا با یک شیء JSON پیچیده در متن پاسخ می\u200cدهند. این پاسخ\u200cها باز می\u200cشوند، ترمیم می\u200cشوند یا به\u200cعنوان متن ساده پذیرفته می\u200cشوند، پس کاربر هرگز آشغال JSON در کادر خروجی نمی\u200cبیند.\n\n## صفحه\u200cهای اسکن\u200cشده رد نمی\u200cشوند\n\nکتاب اسکن\u200cشده لایهٔ متنی ندارد. ترجمهٔ سادهٔ بی\u200cدقت، صفحهٔ خالی را صفحهٔ خالی می\u200cگیرد و کتاب اسکن\u200cشدهٔ ۳۰۰ صفحه\u200cای می\u200cشود ۳۰۰ صفحهٔ گمشده.\n\nاینجا، متن استخراج\u200cشدهٔ کاملاً خالی مسیر دیگری را فعال می\u200cکند: صفحه به\u200cصورت PNG با بزرگ\u200cنمایی **۲×** (حدود ۱۴۴ DPI) رندر می\u200cشود و به مدلی با توانایی دیدن فرستاده می\u200cشود که آن را می\u200cخواند و در یک قدم ترجمه می\u200cکند.\n\nدو محدودیت صادقانه قابل گفتن است. ارائه\u200cدهنده باید بتواند تصویر بگیرد — یک مدل محلی فقط\u200cمتنی این کار را نمی\u200cتواند، و به همین دلیل مسیر صفحهٔ اسکن\u200cشده عملاً به سمت جیمینی می\u200cرود. و چون این صفحه متن مبدأ استخراج\u200cشده ندارد، **حلقهٔ QC برای صفحه\u200cهای اسکن\u200cشده اجرا نمی\u200cشود**: چیزی مستقل برای راستی\u200cآزمایی ترجمه وجود ندارد. این صفحه\u200cها بیش از صفحه\u200cهای متنی به تیک «بازبینی شد» انسانی نیاز دارند.\n\n## هیچ\u200cچیز هرگز گم نمی\u200cشود\n\nمهم\u200cترین چیزی که برایم مهم بود این بود که کار تمام\u200cشده هرگز گم نشود — نه با کرش، نه با توقف سهمیه، نه با ری\u200cاستارت.\n\nهر کتاب یک فایل وضعیت JSON دارد که نامش از هش مسیر مطلق آن ساخته می\u200cشود و **بعد از هر تکه صفحه، به\u200cصورت اتمیک** نوشته می\u200cشود: داده اول در یک فایل موقت نوشته و بعد با `os.replace` جای خود را می\u200cگیرد، پس حتی اگر پروسه وسط ذخیره کشته شود، فایل هرگز نیمه\u200cنوشته دیده نمی\u200cشود. یک `threading.Lock` هم کل عملیات را محافظت می\u200cکند.\n\nوقتی کتابی با صفحه\u200cهای ذخیره\u200cشده را دوباره باز می\u200cکنی، اپ یک سؤال صریح می\u200cپرسد — از اولین صفحهٔ ناتمام ادامه بده یا از اول شروع کن — و **ادامه\u200cدادن پیش\u200cفرض است**. حتی در حالت شروع دوباره، تمپلیت ساختار حفظ می\u200cشود، چون کتاب تغییری نکرده و تشخیص دوباره\u200cاش فقط اتلاف وقت است.\n\nهزینهٔ یک اجرای از\u200cدست\u200cرفته حداکثر همان صفحه\u200cای است که در حال پردازش بود.\n\n## کلید رمز\u200cشده است و اپ با چیز دیگری حرف نمی\u200cزند\n\nکلید API یک\u200cبار در دیالوگ تنظیمات وارد می\u200cشود، در رابط پوشانده است و **با Windows DPAPI رمز می\u200cشود** — همان Data Protection API ویندوز، مقید به حساب کاربری و به سیستم خودت. کاربر دیگری روی همان سیستم، یا همان کاربر روی سیستم دیگر، نمی\u200cتواند آن را رمزگشایی کند.\n\nبرای سکوهای بدون DPAPI یک fallback وجود دارد و اپ آن را پنهان نمی\u200cکند: کلید به ذخیره\u200cسازی base64 با برچسبِ صریح برمی\u200cگردد و دلیلش در `encrypt_fallback.log` نوشته می\u200cشود — مهر زمان و پیام خطا، **و هیچ بخشی از secret**. base64 رمزنگاری نیست، کدگذاری است، و پروژه این را صریح می\u200cگوید به\u200cجای اینکه وانمود کند محافظت شده.\n\nکل سطح شبکهٔ اپ یک سطر است: **ارائه\u200cدهنده\u200cای که خودت تنظیم کرده\u200cای**. نه telemetry، نه بررسی به\u200cروزرسانی، نه گزارش کرش، نه سرویس شخص ثالث، نه آنالیتیک. دیالوگ تنظیمات مسیر دقیق پوشهٔ داده را نشان می\u200cدهد و دکمهٔ یک\u200cکلیکی برای باز کردنش دارد.\n\nاگر می\u200cخواهی هیچ\u200cچیز از دستگاه خارج نشود، ارائه\u200cدهندهٔ سازگار با OpenAI را به Ollama روی لوکال\u200cهاست وصل کن — دقیقاً برای همین، آدرس پیش\u200cفرض (`http://localhost:11434/v1`) همین\u200cجاست.\n\n## رابط کاربری فارسی است، و این یعنی RTL تا ته ته\n\nاین یک چیدمان انگلیسی با رشته\u200cهای فارسی نیست. کل برنامه راست\u200cچین است و در سراسر اپ از ارقام فارسی استفاده می\u200cشود (`۰۱۲۳۴۵۶۷۸۹`).\n\nاین پیامدهای واقعی دارد و به\u200cجای اینکه به شانس واگذار شود، در مجموعه تست assert می\u200cشود:\n\n- «صفحهٔ بعد» به **چپ** اشاره می\u200cکند و «صفحهٔ قبل» به **راست**، چون در RTL جهت حرکت همین است.\n- پنل مبدأ اول به چیدمان اضافه می\u200cشود، پس روی **راست** می\u200cنشیند — جایی که خوانندهٔ فارسی انتظار دارد متن اصلی باشد.\n- درصد پیشرفت راست\u200cچین است و متن داخلی نوار پیشرفت پنهان شده، چون Qt آن را سمت چپ می\u200cکشد.\n- مقدار spin boxها با یک فیلتر اختصاصی راست\u200cچین می\u200cشود که هنگام تغییر تم دوباره اعمال می\u200cشود، چون Qt چیدمان spin box را بازسازی می\u200cکند و این تراز را از دست می\u200cدهد.\n- دکمهٔ کپی وقتی صفحهٔ جاری ترجمه دارد **آبی** است و در غیر این صورت **خاکستری**، پس وضعیتش بدون نیاز به tooltip خوانده می\u200cشود.\n\nدر طول یک اجرای طولانی، اپ صفحه\u200cای را که در حال ترجمه است زنده دنبال می\u200cکند — ولی **ناوبری بین صفحه\u200cها کاملاً آزاد می\u200cماند**. به\u200cمحض اینکه خودت جایی بروی، اپ دیگر نما را برایت جابه\u200cجا نمی\u200cکند. پردازش ادامه دارد؛ فقط دنبال\u200cکردن خودکار کنار می\u200cکشد.\n\n## سه خروجی\n\nوقتی کتاب تمام شد، منوی ذخیره سه قالب پیشنهاد می\u200cدهد:\n\n- **یک صفحه به\u200cصورت TXT**، با سرصفحه\u200cای که نام کتاب و شمارهٔ صفحه را می\u200cنویسد، با کدگذاری `utf-8-sig` تا فارسی در Notepad ویندوز درست نمایش داده شود و به\u200cجای متن به\u200cهم\u200cریخته، فارسی دیده شود.\n- **کل کتاب به\u200cصورت Markdown**، یک بخش `##` برای هر صفحه به ترتیب عددی — مناسب برای version control و diff.\n- **کل کتاب به\u200cصورت یک نسخهٔ HTML مستقل و راست\u200cچین**، با تصویر صفحه کنار هر ترجمه، CSS درون\u200cخطی و قوانین چاپ که نمی\u200cگذارند یک صفحه وسط برگهٔ چاپی نصف شود. در مرورگر باز کن و *Print → Save as PDF* بزن تا یک PDF فارسی تمیز با تصاویر صفحه\u200cهای اصلی بگیری.\n\nمسیر HTML یک انتخاب آگاهانه است: ساخت PDF درستِ راست\u200cچین نیازمند جاسازی فونت فارسی و مدیریت درست چیدمان دوجهته است، و مرورگر این را از قبل خوب انجام می\u200cدهد. خروجی مستقیم PDF با رندر فونت RTL در نقشهٔ راه پروژه هست، ولی خروجی HTML امروز خوب است و از فونت\u200cهایی استفاده می\u200cکند که کاربر از قبل دارد.\n\n## قدم بعدی من\n\nقدم بعدیِ صادقانه یک مدل بهتر نیست. دادهٔ بهتر است: یک مجموعه\u200cارزیابی واقعی از کتاب\u200cها، همراه با ترجمه\u200cهایی که یک مترجم انسانی خوب تولید می\u200cکند، تا کیفیت خط لوله اندازه\u200cگیری شود نه اینکه صرفاً درباره\u200cاش بحث شود. اولین ویژگی\u200cای که اضافه می\u200cکردم، خروجی/ورودی گلاساری است — یک فهرست اصطلاح مشترک بین چند کتاب — چون یکدستی در یک مجموعه کتاب همان چیزی است که تمپلیت\u200cهای per-book حل نمی\u200cکنند.\n\n## اعداد، و منبعشان\n\n| واقعیت | مقدار |\n|---|---|\n| نسخهٔ برنامه | 3.0.0 |\n| هسته | `kaman_core.py`، حدود ۱۴۰۰ خط، بدون Qt |\n| رابط | `translator_app_v3.py`، حدود ۱۸۰۰ خط |\n| مجموعه تست | **۳۰۲ بررسی، همه پاس، کاملاً آفلاین** |\n| وابستگی\u200cهای زمان اجرا | ۴ — PyQt6، PyMuPDF، Pillow، google-genai |\n| بودجهٔ پیش\u200cفرض تکه | ۶۰۰۰ کاراکتر |\n| کانتکست غلتان پیش\u200cفرض | ۷۰۰ کاراکتر |\n| رندر صفحهٔ اسکن\u200cشده | ماتریس ۲× (حدود ۱۴۴ DPI) |\n| محافظت از کلید | Windows DPAPI، با fallback پایه۶۴ که لاگ می\u200cشود |\n| انتشارها | `v3.0.0` (exe ویندوز + zip سورس)، `v2.0.0` |\n\nمجموعه تست بدون شبکه، بدون کلید API و بدون حساب ارائه\u200cدهنده اجرا می\u200cشود: موتورهای جعلی جای واقعی را می\u200cگیرند و پروفایل واقعی کاربر هرگز دست نمی\u200cخورد، چون `APPDATA` قبل از import شدن ماژول\u200cهای اپ به یک پوشهٔ موقت اشاره می\u200cکند. یک اجرا **۳۰۲ بررسی پاس و صفر خطا** چاپ می\u200cکند — این عدد اندازه\u200cگیری\u200cشده است، نه گِرد شده.\n\nمستندات فنی کامل به\u200cصورت ویکی منتشر شده است: معماری، خط لولهٔ ترجمه، موتورها، تمپلیت\u200cهای ساختار، مسیر صفحهٔ اسکن\u200cشده، ذخیرهٔ کار، خروجی\u200cها، رابط کاربری، تنظیمات، مدل امنیتی، مجموعه تست و فرایند انتشار.\n\n- [کد سورس و راه\u200cاندازی در GitHub](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator)\n- [مطالعهٔ ویکی فنی کامل](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator/wiki)\n- [دانلود نسخهٔ ویندوز](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator/releases/latest)\n\n**مرتبط:** همین سایت یک ویجت مشاورهٔ فارسی و یک ربات پیام\u200cرسان را هم مستند کرده که بر همین ایده\u200cها ساخته شده\u200cاند — یک موتور محلی و قابل\u200cممیزی، با مدل میزبان\u200cشده فقط جایی که واقعاً ارزشش را دارد.',
        'body_ar': 'تفشل ترجمة كتاب من 300 صفحة داخل نافذة محادثة بطريقة يمكن التنبؤ بها. عندما تطلب ترجمة، يلخّص النموذج. وتتبدّل المصطلحات من فصل إلى آخر، فيظهر المفهوم الواحد بثلاثة مصطلحات عربية مختلفة. كما تُترجم ترويسات الصفحات وأرقامها وكأنها نص. وأي جلسة تنتهي بعطل تُهدر ساعة عمل كاملة.\n\nأردت أن أعرف ما الذي يلزم للقيام بذلك على الوجه الصحيح، فبنيت **Kaman AI Translator** — تطبيق سطح مكتب لويندوز يترجم كتب PDF وEPUB صفحةً صفحة إلى الفارسية الأكاديمية والعكس، مع معالجة الإخفاقات المتكررة بشفرة محلية قابلة للقراءة.\n\nالمستودع ملفا بايثون ومجموعة اختبارات. الجزء المثير ليس الواجهة، بل خط الأنابيب تحتها.\n\n## القيد الذي شكّل كل شيء\n\n"الذكاء الاصطناعي" هنا ليس خدمة مستضافة داخل التطبيق. إنه طبقة محرك رفيعة قابلة للاستبدال — حزمة Gemini الرسمية من Google، أو أي نقطة نهاية متوافقة مع OpenAI (Ollama، LM Studio، llama.cpp، أو مزوّد سحابي).\n\nالأمر مهم لأن *استراتيجية* الترجمة — التقسيم، والسياق المتحرك، وبنية الكتاب، وضبط الجودة — شفرة محلية حتمية. النموذج أداة تستدعيها هذه الاستراتيجية؛ ليس هو من يقرّر أبدًا. ولهذا السبب يمكن اختبار خط الأنابيب بالكامل دون خادم، بمحرّك وهمي ودون مفتاح API.\n\n## تقسيم لا يقطع الجملة في نصفها\n\nالمدخل الطويل هو أول ما ينكسر. الحد الافتراضي هو **6000** حرف لكل طلب، ويعمل المُقسِّم على ثلاث مستويات: حدود الفقرات أولاً، ثم حدود الجمل، ثم الكلمات — لا في منتصف الجملة أبدًا.\n\nثم تُعاد تغليف الوحدات ضمن الحد، فلا يُهدر طلب على فقرة واحدة ضخمة، ولا تصل قطعة مليئة بالشظايا إلى النموذج.\n\nويصل **ذيل سياق متحرك** مع كل قطعة: آخر **700** حرف من الترجمة السابقة تُضاف إلى الأمر، فيبقى المصطلح والأسلوب متسقين عبر الفصل بدل أن يبدأ كل صفحة من الصفر. يمكن تصفير هذا الإعداد وتعطيل الميزة كليًا، لكن الوضع الافتراضي مفعّل لأنه أرخص تحسين جودة في التطبيق كله.\n\n## قالب بنية خاص بكل كتاب\n\nأكثر أجزاء الشفرة المحلية إثارةً يجيب على سؤال محدد: كيف نمنع تكرار التسمية نفسها في الكتاب الواحد خمس صيغ مختلفة؟\n\nيكتشف التطبيق، **لكل كتاب، محليًا ومجانًا**، أمرين:\n\n- **العناوين** — عنوان الفصل ينبغي أن يُقرأ كعنوان فصل لا كنص عادي.\n- **التسميات المتكررة** — مثل "هل تعلم؟" أو "الأنشطة"، التي تتكرر عشرات المرات ويجب أن تُترجَم متطابقة في كل مرة.\n\nيُدرَج الاثنان في كل أمر خاص بذلك الكتاب، فتُترجَم التسمية دائمًا بالطريقة نفسها. والاثنان قابلان للتعديل يدويًا، ويمرّ تمرير اختياري بالذكاء الاصطناعي يقرأ فهرس المحتويات ويستخرج بنية أعمق مقابل **طلب API إضافي واحد فقط**.\n\nالكشف رخيص: الأسطر التي تتكرر في ربع الصفحات المُعاينة على الأقل، قرب الحافة العليا أو السفلى للصفحة، تُعد ترويسات متكررة وتُحذف **قبل أن يراها النموذج أصلًا**. وتُجمع الكلمات المكسورة بشرطة — `exam-` مع `ple` تصير `example` — بينما تُحمى أرقام القوائم والصيغ داخل النص.\n\n## أوامر ملزمة، وجولة ثانية تتحقق من العمل\n\nالأوامر صريحة: يجب ألّا تحذف الترجمة، وألّا تلخّص، وأن تحفظ بنية الفقرات والأرقام والمعادلات وعلامات الإحالة مثل `[12]`، وأن تستخدم مصطلحًا واحدًا متسقًا لكل مفهوم.\n\nثم هناك **حلقة ضبط الجودة** الاختيارية: جولة ثانية تقارن الترجمة بنصها المصدر، وتُعلّم الانزياح المعنوي والمحذوفات، وتعيد نسخة مصحّحة. هذه نداء ثانٍ حقيقي، والواجهة تقول ذلك — تكلفة هذه الجولة تكاد تكون الضعف.\n\n وهناك أيضًا **طبقة أمان بصيغة JSON**. ردود النماذج تصل أحيانًا بصيغة JSON خام، أو بكائن JSON ملفوف بنص. تُفكّ هذه الردود أو تُصلَح أو تُقبل كنص عادي، فلا يرى المستخدم مخرجات JSON مشوّهة في صندوق الإخراج.\n\n## الصفحات الممسوحة ضوئيًا لا تُترك\n\nالكتاب الممسوح لا طبقة نصية له. والترجمة الساذجة تتعامل مع الصفحة الفارغة كصفحة فارغة، فيصبح كتاب من 300 صفحة مسحًا هو 300 صفحة مفقودة.\n\nهنا، النص المستخرج الفارغ تمامًا يُطلق مسارًا آخر: تُرسم الصفحة PNG بتكبير **2×** (نحو 144 DPI) وتُرسَل إلى نموذج قادر على الرؤية يقرأها يترجمها في خطوة واحدة.\n\nومحدودان يجب ذكرهما بصراحة: يجب أن يقبل المزوّد الصور — النموذج المحلي النصي فقط لا يستطيع ذلك، ولهذا السبب يتّجه مسار الصفحة المسوحة عمليًا نحو Gemini. ولأن هذه الصفحة بلا نص مصدر مستخرج، **تُخطّى حلقة ضبط الجودة فيها**: لا يوجد مرجع مستقل للتحقق من الترجمة. وهذه الصفحات تستحق علامة "تمت المراجعة" البشرية أكثر من الصفحات النصية.\n\n## لا يُفقد شيء، أبدًا\n\nأهم ما اهتممت به كان أن العمل المنجز لا يضيع أبدًا — لا بعطل، ولا بتوقف الحصة، ولا بإعادة تشغيل.\n\nلكل كتاب ملف حالة JSON، اسمه مشتق من تجزئة مساره المطلق، ويُكتب **ذرّيًا بعد كل صفحة**: تُكتب البيانات إلى ملف مؤقت ثم تستبدل به `os.replace`، فلا يُرى الملف نصف مكتوب حتى لو قُتلت العملية أثناء الحفظ. ويحرس `threading.Lock` العملية كلها.\n\nوحين تفتح كتابًا بصفحات محفوظة، يسأل التطبيق سؤالًا صريحًا — هل تكمل من أول صفحة غير مكتملة، أم تبدأ من جديد — و**«متابعة» هو الافتراضي**. وحتى عند البدء من جديد، يبقى قالب البنية سليمًا، فالكتاب لم يتغيّر وإعادة اكتشافه ليس سوى إهدار للوقت.\n\nأقصى خسارة لتشغيل واحد تساوي على الأكثر الصفحة التي كانت قيد التنفيذ.\n\n## المفتاح مشفَّر، والتطبيق لا يتحدث إلى غير المزوّد\n\nيُدخَل مفتاح API مرة واحدة في نافذة الإعدادات، ويُقنَّع في الواجهة، ويُخزَّن **مشفَّرًا عبر Windows DPAPI** — واجهة حماية بيانات ويندوز، مربوطة بحسابك وبجهازك. ولا يستطيع مستخدم آخر على الجهاز نفسه، ولا المستخدم نفسه على جهاز آخر، فك تشفيره.\n\nوهناك مسار بديل للمنصّات التي لا تدعم DPAPI، والتطبيق لا يخفيه: يعود المفتاح إلى تخزين base64 موسوم بوضوح، ويُكتب السبب في `encrypt_fallback.log` — طابع زمني ورسالة الخطأ، **ولا أي جزء من السر**. وbase64 ترميز لا تشفير، والمشروع يصرّح بذلك بدل أن يدّعي غير ذلك.\n\nسطح الشبكة بالكامل سطر واحد: **المزوّد الذي اضبطته أنت**. لا تتبّع، ولا فحص تحديثات، ولا تقارير أعطال، ولا خدمة طرف ثالث، ولا تحليلات. تعرض نافذة الإعدادات مسار مجلد البيانات بالضبط وزرًّا يفتحه بنقرة.\n\nوإن أردت ألّا يغادر شيء الجهاز، فوجّه مزوّد OpenAI المتوافق إلى Ollama على localhost — لهذا بالضبط يوجد العنوان الافتراضي (`http://localhost:11434/v1`).\n\n## الواجهة فارسية، وهذا يعني RTL من الرأس إلى القدم\n\nهذه ليست تخطيطًا إنجليزيًا حشوته نصوص فارسية. التطبيق كله يعمل من اليمين إلى اليسار، وبالأرقام الفارسية في كل مكان (`۰۱۲۳۴۵۶۷۸۹`).\n\nولهذا نتائج حقيقية، والمجموعة الاختبارية تُثبّتها بدل تركها للصدفة:\n\n- «الصفحة التالية» تشير **يسارًا** و«السابقة» تشير **يمينًا**، لأن اتجاه السير في RTL كذلك.\n- تُضاف لوحة المصدر أولًا في التخطيط، فتستقر على **اليمين** — حيث يتوقع القارئ الفارسي النص الأصلي.\n- نسبة التقدم محاذاة إلى اليمين، ونص شريط التقدم الداخلي مخفي لأن Qt ترسمه على اليسار.\n- قيم حقول الأرقام محاذاة إلى اليمين عبر مرشّح مخصّص، يُعاد تطبيقه عند تغيّر السمة، لأن Qt تعيد بناء تخطيط حقول الأرقام وتفقد المحاذاة لولا ذلك.\n- زر النسخ **أزرق** عندما تكون للصفحة الحالية ترجمة و**رمادي** عندما لا تكون، فتُقرأ حالته دون تلميح.\n\nأثناء التشغيل الطويل يتبع التطبيق الصفحة قيد الترجمة مباشرةً — لكن **التنقل بين الصفحات يبقى حرًا تمامًا**. بمجرد أن تتصفّح بنفسك، يتوقف التطبيق عن تحريك العرض. المتابعة تستمر؛ فقط التتبع التلقائي يتراجع.\n\n## ثلاثة تصديرات\n\nعند انتهاء الكتاب، يقدّم قائمة الحفظ ثلاثة صيغ:\n\n- **صفحة واحدة بصيغة TXT**، بترويسة تذكر اسم الكتاب ورقم الصفحة، ومكتوبة بـ `utf-8-sig` لتُعرض الفارسية صحيحة في Notepad بدل أن تظهر مشوّهة.\n- **الكتاب كاملًا بصيغة Markdown**، قسم `##` لكل صفحة بترتيب رقمي — مناسب للتتبّع والإصدار.\n- **الكتاب كاملًا كنسخة HTML مستقلة تعمل من اليمين لليسار**، بصورة الصفحة بجوار كل ترجمة، وCSS مضمّن، وقواعد طباعة تمنع انقسام الصفحة بين ورقتين. افتحها في متصفح واطبع «حفظ كـ PDF» لتحصل على PDF فارسي مرتّب مع صور الصفحات الأصلية.\n\nمسار HTML اختيار مقصود: فإخراج PDF صحيح من اليمين لليسار يستلزم تضمين خط فارسي والتعامل الصحيح مع تخطيط ثنائي الاتجاه، والمتصفح يؤدي ذلك جيدًا أصلًا. وإخراج PDF مباشر مع رندر خط RTL في خارطة طريق المشروع، لكن تصدير HTML جيد اليوم، ويستخدم الخطوط التي يملكها المستخدم بالفعل.\n\n## ما سأبنيه تاليًا\n\nالخطوة التالية الصادقة ليست نموذجًا أفضل، بل بيانات أفضل: مجموعة تقييم حقيقية من الكتب مع الترجمات التي ينتجها مترجم بشري جيد، لتصبح جودة خط الأنابيب قابلة للقياس لا مجرد جدل. وأول ميزة سأضيفها هي تصدير واستيراد مسرد — قائمة مصطلحات واحدة مشتركة بين عدة كتب — لأن الاتساق عبر سلسلة من الكتب هو ما لا تحله القوالب الخاصة بكل كتاب.\n\n## الأرقام، ومن أين أتت\n\n| الحقيقة | القيمة |\n|---|---|\n| إصدار التطبيق | 3.0.0 |\n| النواة | `kaman_core.py`، نحو 1400 سطر، بلا Qt |\n| الواجهة | `translator_app_v3.py`، نحو 1800 سطر |\n| مجموعة الاختبارات | **302 فحصًا، كلها ناجحة، بلا اتصال تمامًا** |\n| اعتماديات وقت التشغيل | 4 — PyQt6، PyMuPDF، Pillow، google-genai |\n| حد القطعة الافتراضي | 6000 حرف |\n| ذيل السياق المتحرك الافتراضي | 700 حرف |\n| رسم الصفحة المسوحة | مصفوفة 2× (نحو 144 DPI) |\n| حماية المفتاح | Windows DPAPI، مع بديل base64 يُسجَّل |\n| الإصدارات | `v3.0.0` (ملف تنفيذي لويندوز + أرشيف مصدر)، `v2.0.0` |\n\nتعمل مجموعة الاختبارات بلا شبكة وبلا مفتاح API وبلا حساب مزوّد: محرّكات وهمية تحل محل الحقيقية، وملف المستخدم الحقيقي لا يُمَسّ أبدًا لأن `APPDATA` يُعاد توجيهه إلى مجلد مؤقت قبل استيراد وحدات التطبيق. وتطبع الجولة الواحدة **302 فحصًا ناجحًا وصفر إخفاق** — هذا رقم مقيس، لا مقرَّب.\n\nوالتوثيق التقني الكامل منشور في ويكي المستودع: البنية، وخط أنابيب الترجمة، والمحرّكات، وقوالب البنية، ومسار الصفحة المسوحة، ومخزن العمل، والتصديرات، والواجهة، والإعدادات، ونموذج الأمان، ومجموعة الاختبارات، وعملية الإصدار.\n\n- [الشيفرة المصدرية والإعداد على GitHub](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator)\n- [اقرأ الويكي التقني الكامل](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator/wiki)\n- [نزّل ملف ويندوز التنفيذي](https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator/releases/latest)\n\n**ذو صلة:** يوثّق هذا الموقع أيضًا أداة استشارة فارسية وبوت مراسلة مبنيين على الأفكار نفسها — محرّك محلي قابل للتدقيق، مع نموذج مستضاف حيث يستحق فقط.',
    },
]


class Command(BaseCommand):
    help = 'Seed the database with Mohammad Hasan Kaman portfolio data.'

    def handle(self, *args, **options):
        self._sync_profile()
        self._sync_projects()
        self._sync_skills()
        self._sync_services()
        self._sync_testimonials()
        self._sync_articles()
        self._sync_experiences()
        self._sync_educations()
        self._sync_cv_languages()
        self.stdout.write(self.style.SUCCESS('[DONE] Seeding complete!'))

    # ------------------------------------------------------------------ profile
    def _sync_profile(self):
        p = Profile.objects.first()
        if not p:
            p = Profile.objects.create(**ABOUT, **TAGLINE, **CORE_COMPETENCIES, **CV_SUMMARY)
            self.stdout.write('[OK] Profile created')
        else:
            changed = []
            for k, v in {**ABOUT, **TAGLINE, **CORE_COMPETENCIES, **CV_SUMMARY}.items():
                if getattr(p, k, None) != v:
                    setattr(p, k, v)
                    changed.append(k)
            if changed:
                p.save(update_fields=changed)
                self.stdout.write(f'[OK] Profile updated ({len(changed)} fields)')

        # The counter claims must match reality: 12 public project repos and
        # 4 years of shipping software (2022 → 2026). The client counter is
        # not displayed anywhere and no client count is verifiable, so it
        # stays at zero instead of carrying an invented number.
        p.years_experience = 4
        p.projects_completed = len(PROJECTS)
        p.happy_clients = 0
        p.save(update_fields=['years_experience', 'projects_completed', 'happy_clients'])
        self.stdout.write(f'[OK] Stats: {p.years_experience} years, {p.projects_completed} projects')

    # ----------------------------------------------------------------- projects
    def _sync_projects(self):
        created = updated = 0
        for data in PROJECTS:
            obj, was_created = Project.objects.get_or_create(slug=data['slug'], defaults=data)
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in data.items():
                if getattr(obj, k, None) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        # Remove rows that are no longer real projects (e.g. duplicates).
        stale = Project.objects.exclude(slug__in=[p['slug'] for p in PROJECTS]).delete()
        self.stdout.write(f'[OK] Projects: {created} created, {updated} updated, '
                          f'{stale[0]} removed, {Project.objects.count()} total')

    # ------------------------------------------------------------------- skills
    def _sync_skills(self):
        created = updated = 0
        for name, tier, icon, order in SKILLS:
            obj, was_created = Skill.objects.get_or_create(
                name=name, defaults={'tier': tier, 'icon': icon, 'order': order})
            if was_created:
                created += 1
                continue
            changed = []
            if obj.tier != tier:
                obj.tier = tier
                changed.append('tier')
            if obj.icon != icon:
                obj.icon = icon
                changed.append('icon')
            if obj.order != order:
                obj.order = order
                changed.append('order')
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        stale = Skill.objects.exclude(name__in=[s[0] for s in SKILLS]).delete()
        self.stdout.write(f'[OK] Skills: {created} created, {updated} updated, '
                          f'{stale[0]} removed, {Skill.objects.count()} total')

    # ----------------------------------------------------------------- services
    def _sync_services(self):
        created = updated = 0
        for icon, t_en, t_fa, t_ar, d_en, d_fa, d_ar, order in SERVICES:
            obj, was_created = Service.objects.get_or_create(
                title_en=t_en,
                defaults={'icon': icon, 'title_fa': t_fa, 'title_ar': t_ar,
                          'description_en': d_en, 'description_fa': d_fa,
                          'description_ar': d_ar, 'order': order})
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in (('icon', icon), ('title_fa', t_fa), ('title_ar', t_ar),
                         ('description_en', d_en), ('description_fa', d_fa),
                         ('description_ar', d_ar), ('order', order)):
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        self.stdout.write(f'[OK] Services: {created} created, {updated} updated, '
                          f'{Service.objects.count()} total')

    # ------------------------------------------------------------- testimonials
    def _sync_testimonials(self):
        created = updated = 0
        for name, r_en, r_fa, r_ar, x_en, x_fa, x_ar, order in TESTIMONIALS:
            obj, was_created = Testimonial.objects.get_or_create(
                name=name,
                defaults={'role_en': r_en, 'role_fa': r_fa, 'role_ar': r_ar,
                          'text_en': x_en, 'text_fa': x_fa, 'text_ar': x_ar,
                          'order': order})
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in (('role_en', r_en), ('role_fa', r_fa), ('role_ar', r_ar),
                         ('text_en', x_en), ('text_fa', x_fa), ('text_ar', x_ar),
                         ('order', order)):
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        self.stdout.write(f'[OK] Testimonials: {created} created, {updated} updated, '
                          f'{Testimonial.objects.count()} total')

    # ----------------------------------------------------------------- articles
    def _sync_articles(self):
        created = updated = 0
        for data in ARTICLES:
            obj, was_created = Article.objects.get_or_create(
                slug=data['slug'], defaults=data)
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in data.items():
                if getattr(obj, k, None) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        self.stdout.write(f'[OK] Articles: {created} created, {updated} updated, '
                          f'{Article.objects.count()} total')

    # -------------------------------------------------------------- experiences
    def _sync_experiences(self):
        created = updated = 0
        for data in EXPERIENCES:
            obj, was_created = Experience.objects.get_or_create(
                title_en=data['title_en'], defaults=data)
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in data.items():
                if getattr(obj, k, None) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        # Drop duplicates that the old seed produced (the same project twice)
        # and rows that describe a project which no longer exists.
        known = {e['title_en'].strip().lower() for e in EXPERIENCES}
        seen = set()
        removed = 0
        for e in Experience.objects.order_by('order', 'id'):
            key = e.title_en.strip().lower()
            if key in seen or key not in known:
                e.delete()
                removed += 1
            else:
                seen.add(key)
        self.stdout.write(f'[OK] Experiences: {created} created, {updated} updated, '
                          f'{removed} duplicates removed, {Experience.objects.count()} total')

    # --------------------------------------------------------------- educations
    def _sync_educations(self):
        created = updated = 0
        for data in EDUCATIONS:
            obj, was_created = Education.objects.get_or_create(
                degree_en=data['degree_en'], defaults=data)
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in data.items():
                if getattr(obj, k, None) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        self.stdout.write(f'[OK] Educations: {created} created, {updated} updated, '
                          f'{Education.objects.count()} total')

    # ------------------------------------------------------------- cv languages
    def _sync_cv_languages(self):
        created = updated = 0
        for n_en, l_en, n_fa, l_fa, n_ar, l_ar, order in CV_LANGUAGES:
            obj, was_created = CvLanguage.objects.get_or_create(
                name_en=n_en,
                defaults={'level_en': l_en, 'name_fa': n_fa, 'level_fa': l_fa,
                          'name_ar': n_ar, 'level_ar': l_ar, 'order': order})
            if was_created:
                created += 1
                continue
            changed = []
            for k, v in (('level_en', l_en), ('name_fa', n_fa), ('level_fa', l_fa),
                         ('name_ar', n_ar), ('level_ar', l_ar), ('order', order)):
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    changed.append(k)
            if changed:
                obj.save(update_fields=changed)
                updated += 1
        self.stdout.write(f'[OK] CV languages: {created} created, {updated} updated, '
                          f'{CvLanguage.objects.count()} total')
