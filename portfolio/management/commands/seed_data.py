from django.core.management.base import BaseCommand

from portfolio.models import (Article, CvLanguage, Education, Experience, Profile,
                              Project, Service, Skill, Testimonial)

PROJECTS = [
    {
        'title_en': 'Agent Stream Doctor', 'slug': 'agent-stream-doctor', 'category': 'ai', 'icon': '🩺',
        'title_fa': 'ایجنت استریم داکتر', 'title_ar': 'دكتور البث للوكلاء',
        'description_en': 'A zero-dependency diagnostic toolkit that explains why an LLM stream returned nothing — reasoning-only responses, missing finish_reason, malformed SSE, truncated tool calls. Born from real-world debugging of LLM routers.',
        'description_fa': 'جعبه‌ابزار تشخیصی بدون وابستگی که توضیح می‌دهد چرا یک استریم LLM خالی برگشته — پاسخ‌های فقط-استدلالی، فقدان finish_reason، SSE خراب و فراخوانی ابزار ناقص.',
        'description_ar': 'عدة تشخيص بدون تبعيات تشرح لماذا لم يُرجع بث LLM أي شيء — ردود استدلالية فقط، غياب finish_reason، SSE تالف واستدعاءات أدوات مبتورة.',
        'tech_stack': 'Python, SSE, OpenAI API, Streaming, LLM',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/agent-stream-doctor',
        'featured': True, 'order': 1,
    },
    {
        'title_en': 'Kaman AI Translator', 'slug': 'kaman-ai-translator', 'category': 'ai', 'icon': '📚',
        'title_fa': 'مترجم هوشمند کَمَن', 'title_ar': 'مترجم كَمَن الذكي',
        'description_en': 'AI-powered desktop application that translates PDF and EPUB books from English to academic Persian using Google Gemini. Built with PyQt6 with a polished modern interface.',
        'description_fa': 'اپلیکیشن دسکتاپ مبتنی بر هوش مصنوعی برای ترجمه کتاب‌های PDF و EPUB از انگلیسی به فارسی آکادمیک با گوگل جمینای. ساخته‌شده با PyQt6 و رابط کاربری مدرن.',
        'description_ar': 'تطبيق سطح مكتب مدعوم بالذكاء الاصطناعي لترجمة كتب PDF و EPUB من الإنجليزية إلى الفارسية الأكاديمية باستخدام Google Gemini. مبني بـ PyQt6.',
        'tech_stack': 'Python, PyQt6, Google Gemini, PDF, EPUB',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-ai-translator',
        'featured': True, 'order': 2,
    },
    {
        'title_en': 'Kaman Messenger', 'slug': 'kaman-messenger', 'category': 'security', 'icon': '🔐',
        'title_fa': 'پیام‌رسان کَمَن', 'title_ar': 'مرسال كَمَن',
        'description_en': 'A real-time encrypted messenger built completely from scratch: raw TCP sockets, AES (Fernet) encryption, bcrypt authentication, rate limiting and SQLite storage — with a CustomTkinter GUI.',
        'description_fa': 'پیام‌رسان رمزنگاری‌شده بلادرنگ که کاملاً از صفر ساخته شده: سوکت TCP خام، رمزنگاری AES (Fernet)، احراز هویت bcrypt، محدودسازی نرخ و پایگاه داده SQLite — با رابط CustomTkinter.',
        'description_ar': 'مرسال مشفّر فوري مبني بالكامل من الصفر: مقابس TCP الخام، تشفير AES (Fernet)، مصادقة bcrypt، تحديد المعدل وقاعدة بيانات SQLite — بواجهة CustomTkinter.',
        'tech_stack': 'Python, TCP Sockets, AES/Fernet, bcrypt, SQLite, CustomTkinter',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-messenger',
        'featured': True, 'order': 3,
    },
    {
        'title_en': 'Dr-Kaman Site', 'slug': 'dr-kaman-site', 'category': 'web', 'icon': '🌐',
        'title_fa': 'سایت دکتر کَمَن', 'title_ar': 'موقع د. كَمَن',
        'description_en': 'A multimedia archive website — audio, video, books and articles — running in production at drkaman.ir with Django, nginx and gunicorn on a Linux VPS.',
        'description_fa': 'وب‌سایت آرشیو چندرسانه‌ای — صدا، ویدیو، کتاب و مقاله — که در حال حاضر در drkaman.ir با جنگو، nginx و gunicorn روی سرور لینوکسی در حال اجراست.',
        'description_ar': 'موقع أرشيف وسائط متعددة — صوت وفيديو وكتب ومقالات — يعمل في الإنتاج على drkaman.ir باستخدام Django و nginx و gunicorn.',
        'tech_stack': 'Django, nginx, gunicorn, Linux VPS, JavaScript',
        'live_url': 'https://drkaman.ir',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site',
        'featured': True, 'order': 4,
    },
    {
        'title_en': 'Planikaa Portal', 'slug': 'planikaa-portal', 'category': 'web', 'icon': '🎓',
        'title_fa': 'پورتال پلنیکا', 'title_ar': 'بوابة بلانيكا',
        'description_en': 'A comprehensive educational platform with an exam-analytics dashboard, blog and student resources — built with Django.',
        'description_fa': 'پلتفرم آموزشی جامع با داشبورد تحلیل آزمون، وبلاگ و منابع دانشجویی — ساخته‌شده با جنگو.',
        'description_ar': 'منصة تعليمية شاملة مع لوحة تحليلات الاختبارات ومدونة وموارد للطلاب — مبنية بـ Django.',
        'tech_stack': 'Django, PostgreSQL, Chart.js, HTML/CSS',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/planikaa-portal',
        'featured': True, 'order': 5,
    },
    {
        'title_en': 'Kaman AI Chat', 'slug': 'kaman-ai-chat', 'category': 'ai', 'icon': '💬',
        'title_fa': 'چت هوشمند کَمَن', 'title_ar': 'دردشة كَمَن الذكية',
        'description_en': 'A C# desktop chat assistant running DeepSeek models via OpenModel API, with Google Cloud Text-to-Speech voice output for natural conversations. Built with Bunifu UI.',
        'description_fa': 'دستیار گفتگوی دسکتاپ با C# که مدل‌های DeepSeek را از طریق OpenModel API اجرا می‌کند و با خروجی صدای Google Cloud TTS گفتگوی طبیعی ارائه می‌دهد. ساخته‌شده با Bunifu UI.',
        'description_ar': 'مساعد دردشة سطح مكتب بـ C# يشغل نماذج DeepSeek عبر OpenModel API مع مخرجات صوتية من Google Cloud TTS. مبني بواجهة Bunifu.',
        'tech_stack': 'C#, DeepSeek, OpenModel API, Google Cloud TTS, Bunifu UI',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-ai-chat',
        'featured': False, 'order': 6,
    },
    {
        'title_en': 'Kaman Web Browser', 'slug': 'kaman-web-browser', 'category': 'desktop', 'icon': '🧭',
        'title_fa': 'مرورگر وب کَمَن', 'title_ar': 'متصفح كَمَن',
        'description_en': 'A lightweight multi-tab Windows web browser built on Microsoft Edge WebView2 (Chromium) with C#.',
        'description_fa': 'مرورگر وب سبک ویندوزی ساخته‌شده روی Microsoft Edge WebView2 (کرومیوم) با سی‌شارپ.',
        'description_ar': 'متصفح ويندوز خفيف متعدد التبويبات مبني على Microsoft Edge WebView2 (Chromium) بلغة C#.',
        'tech_stack': 'C#, .NET, WebView2, Chromium',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/kaman-web-browser',
        'featured': False, 'order': 7,
    },
    {
        'title_en': 'Quran Group Bot', 'slug': 'quran-group-bot', 'category': 'desktop', 'icon': '🕌',
        'title_fa': 'ربات گروه قرآن', 'title_ar': 'بوت مجموعة القرآن',
        'description_en': 'Serverless bot for weekly Quran juz reading groups on Bale Messenger — Cloudflare Workers + KV, cron-scheduled posts and automatic hadith sharing.',
        'description_fa': 'ربات بدون سرور برای گروه‌های هفتگی قرائت جزء قرآن در پیام‌رسان بله — Cloudflare Workers و KV با زمان‌بندی کرون و اشتراک خودکار حدیث.',
        'description_ar': 'بوت بلا خادم لمجموعات قراءة جزء القرآن الأسبوعية على مرسال Bale — Cloudflare Workers و KV مع جدولة cron ومشاركة الأحاديث.',
        'tech_stack': 'Bale Messenger, Cloudflare Workers, KV, JavaScript, Cron',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/quran-group-bot',
        'featured': False, 'order': 8,
    },
    {
        'title_en': 'YouTube Downloader', 'slug': 'youtube-downloader', 'category': 'desktop', 'icon': '⬇️',
        'title_fa': 'دانلودر یوتیوب', 'title_ar': 'محمّل يوتيوب',
        'description_en': 'Professional YouTube downloader with a modern Persian RTL interface, live progress and quality selection. Built with Python, CustomTkinter and yt-dlp.',
        'description_fa': 'دانلودر حرفه‌ای یوتیوب با رابط کاربری مدرن راست‌به‌چپ فارسی، نمایش زنده پیشرفت و انتخاب کیفیت. ساخته‌شده با Python، CustomTkinter و yt-dlp.',
        'description_ar': 'محمّل يوتيوب احترافي بواجهة عصرية من اليمين لليسار بالفارسية، مع تتبع التقدم المباشر واختيار الجودة. مبني بـ Python و CustomTkinter و yt-dlp.',
        'tech_stack': 'Python, CustomTkinter, yt-dlp, RTL UI',
        'repo_url': 'https://github.com/Mohammad-Hasan-Kaman/youtube-downloader',
        'featured': False, 'order': 9,
    },
]

SKILLS = [
    ('Python', 95, '🐍', 1), ('Django', 92, '🎸', 2), ('C#', 88, '🎯', 3),
    ('JavaScript', 85, '⚡', 4), ('REST API Design', 92, '🔗', 5),
    ('LLM APIs (OpenAI / Gemini / DeepSeek)', 90, '🤖', 6),
    ('SSE Streaming & Tool Calling', 88, '📡', 7),
    ('PyQt6 / CustomTkinter', 88, '🖥️', 8), ('C# WinForms / Bunifu', 84, '🪟', 9),
    ('Edge WebView2 (Chromium)', 80, '🧭', 10),
    ('TCP Socket Programming', 90, '🔌', 11), ('AES / Fernet Encryption', 86, '🔐', 12),
    ('bcrypt & Auth Systems', 85, '🔑', 13), ('Rate Limiting & Hardening', 82, '🛡️', 14),
    ('SQLite / SQL Databases', 88, '🗄️', 15), ('nginx + gunicorn Deployment', 84, '🚀', 16),
    ('Linux VPS Administration', 82, '🐧', 17), ('BIND9 DNS', 75, '🌐', 18),
    ('Cloudflare Workers / KV', 80, '☁️', 19), ('Git & GitHub', 92, '🌱', 20),
    ('yt-dlp / Automation', 85, '⚙️', 21), ('HTML5 / CSS3', 86, '🎨', 22),
    ('OOP & Clean Architecture', 90, '🏛️', 23), ('Multithreading & Concurrency', 80, '🧵', 24),
]

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

ABOUT = {
    'about_en': "I'm a freelance full-stack developer focused on AI applications, developer tooling and secure systems. "
                "I build end-to-end software in Python and C# — from TCP-level encrypted messengers to production Django "
                "platforms serving real users, to diagnostics for LLM streaming APIs. I care about shipping reliable, "
                "well-engineered products that solve real problems.",
    'about_fa': "من یک توسعه‌دهنده فریلنسِ فول‌استک هستم و روی اپلیکیشن‌های هوش مصنوعی، ابزارهای توسعه‌دهنده و سیستم‌های امن تمرکز دارم. "
                "نرم‌افزارهای کامل با پایتون و سی‌شارپ می‌سازم — از پیام‌رسان‌های رمزنگاری‌شده در سطح TCP تا پلتفرم‌های جنگو در محیط "
                "پروداکشن با کاربران واقعی، و ابزارهای تشخیص خطا برای APIهای استریم LLM. برای من مهم است که محصولاتی قابل‌اعتماد بسازم که مشکل واقعی را حل کنند.",
    'about_ar': "أنا مطوّر برمجيات متكاملة مستقل، أركّز على تطبيقات الذكاء الاصطناعي وأدوات المطورين والأنظمة الآمنة. "
                "أبني برمجيات كاملة بلغتي Python و C# — من رسائل مشفّرة بمستوى TCP إلى منصات Django تعمل في الإنتاج لمستخدمين حقيقيين، "
                "وأدوات تشخيص لـ APIs البث في نماذج LLM. أهتم بإنتاج برمجيات موثوقة ومهندسة جيداً تحل مشكلات حقيقية.",
}

TAGLINE = {
    'tagline_en': 'I build end-to-end software — from TCP-level encrypted messengers to production Django platforms and AI-powered developer tools.',
    'tagline_fa': 'من نرم‌افزارهای کامل می‌سازم — از پیام‌رسان‌های رمزنگاری‌شده در سطح TCP تا پلتفرم‌های جنگو در محیط پروداکشن و ابزارهای توسعه مبتنی بر هوش مصنوعی.',
    'tagline_ar': 'أبني برمجيات متكاملة — من رسائل مشفّرة بمستوى TCP إلى منصات Django في بيئة الإنتاج وأدوات تطوير مدعومة بالذكاء الاصطناعي.',
}

CORE_COMPETENCIES = {
    'core_competencies_en': 'Backend Development & Automation\nAPI Integration & Management\nDatabase Design & Architecture\nAI Application Development\nWeb Application Architecture\nNetwork Infrastructure & Troubleshooting',
    'core_competencies_fa': 'توسعه بک‌اند و اتوماسیون\nیکپارچه‌سازی و مدیریت API\nطراحی و معماری پایگاه داده\nتوسعه اپلیکیشن‌های هوش مصنوعی\nمعماری اپلیکیشن وب\nزیرساخت شبکه و عیب‌یابی',
    'core_competencies_ar': 'تطوير الواجهات الخلفية والأتمتة\nتكامل وإدارة واجهات برمجة التطبيقات\nتصميم وهندسة قواعد البيانات\nتطوير تطبيقات الذكاء الاصطناعي\nهندسة تطبيقات الويب\nالبنية التحتية للشبكات واستكشاف الأخطاء',
}

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

CV_SUMMARY = {
    'summary_en': 'Highly motivated and self-taught developer with a strong foundation in Python and JavaScript. '
                  'Experienced in engineering custom AI-powered applications, backend automation tools and full-stack '
                  'web solutions, with a passion for solving algorithmic and system-level problems. Eager to contribute '
                  'to remote junior backend or full-stack roles in collaborative development teams.',
    'summary_fa': 'توسعه‌دهنده باانگیزه و خودآموخته با پایه‌ای قوی در پایتون و جاوااسکریپت. تجربه ساخت اپلیکیشن‌های سفارشی مبتنی '
                  'بر هوش مصنوعی، ابزارهای اتوماسیون بک‌اند و راه‌حل‌های فول‌استک وب، با علاقه به حل مسائل الگوریتمی و سطح-سیستم. '
                  'مشتاق به همکاری در تیم‌های توسعه برای نقش‌های جونیور بک‌اند یا فول‌استک دورکار.',
    'summary_ar': 'مطوّر واثق من نفسه ومتعلّم ذاتياً بأساس متين في Python و JavaScript. لدي خبرة في بناء تطبيقات AI مخصصة '
                'وأدوات أتمتة للواجهات الخلفية وحلول ويب متكاملة، مع شغف بحل المشكلات الخوارزمية ومستوى النظام. '
                'أطمح للمساهمة في أدوار مطوّر مبتدئ بالواجهة الخلفية أو متكامل ضمن فرق تعاونية.',
}

EXPERIENCES = [
    {
        'title_en': 'AI-Powered PDF Translation & Automation Platform',
        'title_fa': 'پلتفرم ترجمه و اتوماسیون PDF با هوش مصنوعی',
        'title_ar': 'منصة ترجمة PDF والأتمتة بالذكاء الاصطناعي',
        'org_en': 'Freelance', 'org_fa': 'فریلنس', 'org_ar': 'مستقل',
        'period_en': '2024 — 2026', 'period_fa': '۲۰۲۴ — ۲۰۲۶', 'period_ar': '2024 — 2026',
        'description_en': 'Commercial Python desktop application that translates academic and technical PDF/Epub documents over 500 pages into Farsi using the Gemini API. Includes multi-language support (20+ languages), advanced API key management and automated licensing verification.',
        'description_fa': 'اپلیکیشن دسکتاپ تجاری پایتون که اسناد آکادمیک و فنی PDF/Epub بالای ۵۰۰ صفحه را با Gemini API به فارسی ترجمه می‌کند. شامل پشتیبانی از ۲۰+ زبان، مدیریت پیشرفته کلید API و اعتبارسنجی خودکار لایسنس.',
        'description_ar': 'تطبيق سطح مكتب تجاري بلغة Python يترجم مستندات أكاديمية وفنية PDF/EPUB تتجاوز 500 صفحة إلى الفارسية عبر Gemini API، مع دعم أكثر من 20 لغة وإدارة مفاتيح API والتحقق التلقائي من الترخيص.',
        'order': 1,
    },
    {
        'title_en': 'Agent Stream Doctor — LLM Streaming Diagnostics',
        'title_fa': 'ایجنت استریم داکتر — تشخیص خطای استریم LLM',
        'title_ar': 'Agent Stream Doctor — تشخيص بث LLM',
        'org_en': 'Open Source', 'org_fa': 'متن‌باز', 'org_ar': 'مفتوح المصدر',
        'period_en': '2025 — 2026', 'period_fa': '۲۰۲۵ — ۲۰۲۶', 'period_ar': '2025 — 2026',
        'description_en': 'Zero-dependency Python toolkit that diagnoses why an LLM stream returns nothing: reasoning-only responses, missing finish_reason, malformed SSE framing and truncated tool calls. Built from real-world debugging of LLM router integrations.',
        'description_fa': 'جعبه‌ابزار پایتونی بدون وابستگی که علت خالی بودن پاسخ استریم LLM را تشخیص می‌دهد: پاسخ‌های فقط-استدلالی، فقدان finish_reason، فریم‌بندی خراب SSE و فراخوانی ابزار ناقص.',
        'description_ar': 'عدة Python بدون تبعيات تشخّص سبب عودة بث LLM فارغاً: الردود الاستدلالية فقط، غياب finish_reason، تلف إطارات SSE واستدعاءات الأدوات المبتورة.',
        'order': 2,
    },
    {
        'title_en': 'Custom Counseling Center AI Bot',
        'title_fa': 'ربات هوشمند اختصاصی مرکز مشاوره',
        'title_ar': 'بوت ذكاء اصطناعي مخصص لمركز استشارات',
        'org_en': 'Freelance', 'org_fa': 'فریلنس', 'org_ar': 'مستقل',
        'period_en': '2024', 'period_fa': '۲۰۲۴', 'period_ar': '2024',
        'description_en': 'Designed and integrated an intelligent automated assistant for a counseling center using modern LLM APIs to handle client queries and automate interaction workflows, measurably reducing human-agent workload.',
        'description_fa': 'طراحی و یکپارچه‌سازی دستیار هوشمند خودکار برای یک مرکز مشاوره با استفاده از APIهای مدرن LLM برای پاسخ به سوالات مشتریان و خودکارسازی گردش کار، با کاهش قابل اندازه‌گیری حجم کاری کارشناسان.',
        'description_ar': 'تصميم ودمج مساعد آلي ذكي لمركز استشارات باستخدام LLM APIs حديثة للتعامل مع استفسارات العملاء وأتمتة سير العمل، مع تقليص عبء العمل البشري بشكل ملموس.',
        'order': 3,
    },
    {
        'title_en': 'Educational Website & CMS (Django)',
        'title_fa': 'وب‌سایت آموزشی و سیستم مدیریت محتوا (Django)',
        'title_ar': 'موقع تعليمي ونظام إدارة محتوى (Django)',
        'org_en': 'Client Project', 'org_fa': 'پروژه مشتری', 'org_ar': 'مشروع عميل',
        'period_en': '2023 — 2024', 'period_fa': '۲۰۲۳ — ۲۰۲۴', 'period_ar': '2023 — 2024',
        'description_en': 'Django-based CMS platform with secure user authentication, PostgreSQL integration, multi-format media management (video/audio playback) and dynamic categorized content delivery.',
        'description_fa': 'پلتفرم CMS مبتنی بر Django با احراز هویت امن، یکپارچه‌سازی PostgreSQL، مدیریت رسانه چندقالبه (پخش ویدیو/صوت) و ارائه محتوای پویا و دسته‌بندی‌شده.',
        'description_ar': 'منصة CMS مبنية على Django مع مصادقة آمنة وتكامل PostgreSQL وإدارة وسائط متعددة الصيغ (تشغيل فيديو/صوت) وتقديم محتوى ديناميكي مصنّف.',
        'order': 4,
    },
    {
        'title_en': 'Exam Analysis & Statistics System',
        'title_fa': 'سیستم تحلیل آزمون و آمار',
        'title_ar': 'نظام تحليل الاختبارات والإحصاء',
        'org_en': 'Client Project', 'org_fa': 'پروژه مشتری', 'org_ar': 'مشروع عميل',
        'period_en': '2023', 'period_fa': '۲۰۲۳', 'period_ar': '2023',
        'description_en': 'Data-focused web application that ingests student test scores, calculates statistical variances and standard deviations, and exports PDF reports with visual analytics for performance evaluation.',
        'description_fa': 'اپلیکیشن وب داده‌محور که نمرات آزمون دانش‌آموزان را پردازش، واریانس و انحراف معیار را محاسبه و گزارش PDF با نمودارهای تحلیلی برای ارزیابی عملکرد تولید می‌کند.',
        'description_ar': 'تطبيق ويب موجّه للبيانات يدخل درجات الاختبارات ويحسب التباينات والانحرافات المعيارية ويصدر تقارير PDF مع تحليلات مرئية لتقييم الأداء.',
        'order': 5,
    },
    {
        'title_en': 'KamanBrowser — Desktop Web Browser',
        'title_fa': 'کَمَن‌براوزر — مرورگر دسکتاپ',
        'title_ar': 'كَمَن براوزر — متصفح سطح مكتب',
        'org_en': 'Personal Project', 'org_fa': 'پروژه شخصی', 'org_ar': 'مشروع شخصي',
        'period_en': '2022 — 2023', 'period_fa': '۲۰۲۲ — ۲۰۲۳', 'period_ar': '2022 — 2023',
        'description_en': 'Modern desktop web browser built with C# and Windows Forms on Edge WebView2 (Chromium): tab management, bookmarks, custom UI components and smooth navigation with a minimal memory footprint.',
        'description_fa': 'مرورگر دسکتاپ مدرن با C# و Windows Forms روی WebView2 (کرومیوم): مدیریت تب، بوکمارک، کامپوننت‌های سفارشی و ناوبری روان با کمترین مصرف حافظه.',
        'description_ar': 'متصفح ويب حديث بـ C# و Windows Forms على Edge WebView2 (Chromium): إدارة تبويبات وعلامات مرجعية ومكونات واجهة مخصصة وتنقل سلس.',
        'order': 6,
    },
    {
        'title_en': 'KamanBrowser',
        'title_fa': 'کامن‌براوزر',
        'title_ar': 'كامن براوزر',
        'org_en': 'Personal Project', 'org_fa': 'پروژه شخصی', 'org_ar': 'مشروع شخصي',
        'period_en': '2022 — 2023', 'period_fa': '۲۰۲۲ — ۲۰۲۳', 'period_ar': '2022 — 2023',
        'description_en': 'Modern desktop web browser built with C# and Windows Forms. Implemented tab management, bookmark support, custom UI components and smooth navigation controls to ensure minimal memory footprint and light resource allocation.',
        'description_fa': 'مرورگر وب دسکتاپ مدرن ساخته‌شده با C# و Windows Forms. شامل مدیریت تب، پشتیبانی از بوکمارک، اجزای رابط کاربری سفارشی و ناوبری روان برای حداقل مصرف حافظه و منابع سبک.',
        'description_ar': 'متصفح ويب سطح مكتب حديث مبني بـ C# و Windows Forms. يتضمن إدارة علامات التبويب ودعم الإشارات المرجعية ومكونات واجهة مخصصة وتنقلاً سلساً لضمان أقل استهلاك للذاكرة وموارد خفيفة.',
        'order': 5,
    },
]

EDUCATIONS = [
    {
        'degree_en': 'Secondary Education (High School)',
        'degree_fa': 'تحصیلات متوسطه (دبیرستان)',
        'degree_ar': 'التعليم الثانوي',
        'period_en': 'Expected Graduation: Mid-2028',
        'period_fa': 'فارغ\u200cالتحصیلی پیش\u200cبینی\u200cشده: اواسط ۲۰۲۸',
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
        'title_en': 'Why is my LLM stream empty? A field guide to broken SSE responses',
        'slug': 'why-is-my-llm-stream-empty',
        'icon': '🩺',
        'title_fa': 'چرا استریم LLM من خالی است؟ راهنمای تشخیص پاسخ‌های خراب SSE',
        'title_ar': 'لماذا بث LLM فارغ؟ دليل عملي لاستجابات SSE المعطلة',
        'excerpt_en': 'Reasoning-only replies, missing finish_reason, malformed SSE frames — the four most common reasons a streaming LLM call returns nothing, and how to diagnose each one.',
        'excerpt_fa': 'پاسخ‌های فقط-استدلالی، فقدان finish_reason و فریم‌های خراب SSE — چهار دلیل رایجی که یک فراخوانی استریم LLM خالی برمی‌گرداند و روش تشخیص هر کدام.',
        'excerpt_ar': 'ردود استدلالية فقط، غياب finish_reason وإطارات SSE تالف — الأسباب الأربعة الأكثر شيوعاً لعودة استدلال البث فارغاً وكيفية تشخيص كل منها.',
        'body_en': "If you have ever called an OpenAI-compatible API with streaming enabled and received... nothing, you are not alone. After debugging dozens of these cases (and building agent-stream-doctor to automate it), I keep seeing the same four failure modes.\n\n"
                   "1. Reasoning-only responses. Some models emit their entire answer inside a reasoning channel and mark the content channel as empty. The stream 'works' but your UI shows nothing. Always inspect the delta fields, not just the content.\n\n"
                   "2. Missing finish_reason. When a proxy truncates the final chunk, finish_reason disappears and many clients silently drop the message. Treat a missing finish_reason as a red flag, not a quirk.\n\n"
                   "3. Malformed SSE framing. Multi-byte UTF-8 split across chunk boundaries, or a proxy that rewrites 'data:' prefixes, will break parsers quietly. Log raw frames before parsing.\n\n"
                   "4. Truncated tool calls. Partial tool_call deltas that never merge into a complete call leave your agent hanging. Accumulate and validate arguments before executing.\n\n"
                   "The fix is always the same: observe the raw stream first, then reason about the protocol. That is exactly what my diagnostic toolkit does — check it out on GitHub.",
        'body_fa': "اگر تا به حال با API سازگار با OpenAI و استریم کار کرده باشید و هیچ خروجی نگرفته باشید، تنها نیستید. پس از دیباگ ده‌ها مورد از این دست (و ساخت ابزار agent-stream-doctor برای خودکارسازی آن)، همیشه چهار حالت خرابی تکراری می‌بینم.\n\n"
                   "۱. پاسخ‌های فقط-استدلالی: برخی مدل‌ها کل پاسخ را در کانال reasoning می‌فرستند و کانال content را خالی می‌گذارند. استریم «کار می‌کند» ولی رابط کاربری شما چیزی نشان نمی‌دهد. همیشه فیلدهای delta را بررسی کنید.\n\n"
                   "۲. فقدان finish_reason: وقتی پراکسی چانک آخر را قطع می‌کند، finish_reason حذف می‌شود و خیلی از کلاینت‌ها بی‌صدا پیام را دور می‌ریزند. نبودِ finish_reason را یک زنگ خطر جدی بدانید.\n\n"
                   "۳. فریم‌بندی خراب SSE: چندبایتی بودن UTF-8 روی مرز چانک‌ها یا بازنویسی پیشوند data: توسط پراکسی، پارسرها را بی‌صدا می‌شکند. قبل از پارس، فریم‌های خام را لاگ کنید.\n\n"
                   "۴. فراخوانی ابزار ناقص: دلتاهای نیمه‌کاره tool_call که هرگز کامل نمی‌شوند، ایجنت شما را معلق می‌گذارند. قبل از اجرا، آرگومان‌ها را جمع‌آوری و اعتبارسنجی کنید.\n\n"
                   "راه‌حل همیشه یکی است: اول استریم خام را ببین، بعد درباره پروتکل فکر کن. جعبه‌ابزار تشخیصی من دقیقاً همین کار را می‌کند — روی گیت‌هاب ببینید.",
        'body_ar': "إذا سبق لك استدعاء API متوافق مع OpenAI مع تمكين البث ولم يتِك شيء، فأنت لست وحدك. بعد تصحيح عشرات الحالات (وبناء أداة agent-stream-doctor لأتمتتها)، أرى دائماً نفس أنماط الفشل الأربعة.\n\n"
                   "١. الردود الاستدلالية فقط: بعض النماذج ترسل الإجابة كاملة في قناة reasoning وتترك قناة content فارغة. البث «يعمل» لكن واجهتك لا تعرض شيئاً. افحص حقول delta دائماً.\n\n"
                   "٢. غياب finish_reason: عندما يقتطع البروكسي القطعة الأخيرة يختفي finish_reason ويستكتب عملاء كثيرون الرسالة بصمت. اعتبر غيابه علامة خطر.\n\n"
                   "٣. تلف إطار SSE: انقسام أحرف UTF-8 متعددة البايتات عبر حدود القطع أو إعادة كتابة البادئة data: تكسر المحللات بصمت. سجّل الإطارات الخام قبل التحليل.\n\n"
                   "٤. استدعاءات أدوات مبتورة: دلتا tool_call الجزئية التي لا تكتمل تُعلّق الوكيل. جمّع الحجج وتحقق منها قبل التنفيذ.\n\n"
                   "الحل واحد دائماً: راقب البث الخام أولاً ثم فكّر في البروتوكول. هذا بالضبط ما تفعله أداتي التشخيصية — راجعها على GitHub.",
    },
]


class Command(BaseCommand):
    help = 'Seed the database with Mohammad Hasan Kaman portfolio data.'

    def handle(self, *args, **options):
        if not Profile.objects.exists():
            Profile.objects.create(**ABOUT, **TAGLINE, **CORE_COMPETENCIES)
            self.stdout.write('[OK] Profile created')

        # Update core competencies if profile exists but they're empty
        p = Profile.objects.first()
        if not p.core_competencies_en:
            for k, v in CORE_COMPETENCIES.items():
                setattr(p, k, v)
            p.save(update_fields=list(CORE_COMPETENCIES.keys()))
            self.stdout.write('[OK] Core competencies added')

        if Project.objects.count() == 0:
            for p in PROJECTS:
                Project.objects.create(**p)
            self.stdout.write(f'[OK] {len(PROJECTS)} projects created')

        if Skill.objects.count() == 0:
            for name, level, icon, order in SKILLS:
                Skill.objects.create(name=name, level=level, icon=icon, order=order)
            self.stdout.write(f'[OK] {len(SKILLS)} skills created')
        else:
            # add any skills that do not exist yet (keeps the site in sync without duplicating)
            existing = set(Skill.objects.values_list('name', flat=True))
            added = 0
            for name, level, icon, order in SKILLS:
                if name not in existing:
                    Skill.objects.create(name=name, level=level, icon=icon, order=order)
                    added += 1
            self.stdout.write(f'[OK] {added} new skills added ({Skill.objects.count()} total)')

        if Service.objects.count() == 0:
            for icon, t_en, t_fa, t_ar, d_en, d_fa, d_ar, order in SERVICES:
                Service.objects.create(
                    icon=icon, title_en=t_en, title_fa=t_fa, title_ar=t_ar,
                    description_en=d_en, description_fa=d_fa, description_ar=d_ar, order=order)
            self.stdout.write(f'[OK] {len(SERVICES)} services created')

        if Testimonial.objects.count() == 0:
            for name, r_en, r_fa, r_ar, x_en, x_fa, x_ar, order in TESTIMONIALS:
                Testimonial.objects.create(
                    name=name, role_en=r_en, role_fa=r_fa, role_ar=r_ar,
                    text_en=x_en, text_fa=x_fa, text_ar=x_ar, order=order)
            self.stdout.write(f'[OK] {len(TESTIMONIALS)} testimonials created')

        if Article.objects.count() == 0:
            for a in ARTICLES:
                Article.objects.create(**a)
            self.stdout.write(f'[OK] {len(ARTICLES)} articles created')

        if not Profile.objects.first().summary_en:
            p = Profile.objects.first()
            for k, v in CV_SUMMARY.items():
                setattr(p, k, v)
            p.save(update_fields=list(CV_SUMMARY.keys()))
            self.stdout.write('[OK] CV summary added')

        if Experience.objects.count() == 0:
            for e in EXPERIENCES:
                Experience.objects.create(**e)
            self.stdout.write(f'[OK] {len(EXPERIENCES)} experiences created')

        if Education.objects.count() == 0:
            for e in EDUCATIONS:
                Education.objects.create(**e)
            self.stdout.write(f'[OK] {len(EDUCATIONS)} educations created')

        if CvLanguage.objects.count() == 0:
            for n_en, l_en, n_fa, l_fa, n_ar, l_ar, order in CV_LANGUAGES:
                CvLanguage.objects.create(name_en=n_en, level_en=l_en, name_fa=n_fa,
                                          level_fa=l_fa, name_ar=n_ar, level_ar=l_ar, order=order)
            self.stdout.write(f'[OK] {len(CV_LANGUAGES)} cv languages created')

        self.stdout.write('[DONE] Seeding complete!')
