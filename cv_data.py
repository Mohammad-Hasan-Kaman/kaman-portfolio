"""Updated CV content (2026) for Mohammad Hasan Kaman — EN / FA / AR.
Changes vs. the 2024 original:
  - Title "Junior Full-Stack Developer" -> "Full-Stack Developer (Remote)"
  - Portfolio website (mhkaman.com) added to contact info
  - Summary refreshed for 2026 (production experience, freelancing for international clients)
  - Agent Stream Doctor (open-source, 2025-2026) added to projects
  - Fixed reversed Persian/Arabic date digits (e.g. 4202 -> 2024)
"""

DATA = {
    'en': {
        'file': 'Mohammad_Hasan_Kaman_CV.pdf',
        'rtl': False,
        'name': 'Mohammad Hasan Kaman',
        'role': 'Full-Stack Developer (Remote)',
        'contact': 'mohammadhasankaman@gmail.com   |   Germany (Remote)   |   Portfolio: mhkaman.com',
        'links': 'linkedin.com/in/kaman-programmer    |    github.com/Mohammad-Hasan-Kaman    |    t.me/mohaka0975',
        'summary': 'Self-taught Full-Stack Developer with strong foundations in Python, C# and JavaScript, and 3+ years of '
                   'hands-on experience shipping production-ready software — from AI-powered desktop applications and LLM '
                   'integrations to Django platforms deployed on Linux VPS with nginx and gunicorn. Passionate about solving '
                   'algorithmic and system-level problems and building database-driven platforms. Currently completing '
                   'secondary education (expected graduation mid-2028) while freelancing for international clients. '
                   'Seeking remote backend or full-stack roles in collaborative teams.',
        'core': ['Backend Development & Automation', 'API Integration & Management (REST & LLM)',
                 'Database Design & Architecture', 'AI Application Development (LLM APIs & Streaming)',
                 'Web Application Architecture', 'Network Infrastructure & Troubleshooting'],
        'sections': [
            ('Professional Projects', [
                ('AI-Powered PDF Translation & Automation Platform', '2024 — 2026  ·  Freelance',
                 'Commercial Python desktop application that translates academic and technical PDF/Epub documents over '
                 '500 pages into Farsi using the Gemini API. Includes support for 20+ languages, advanced API key '
                 'management and automated licensing verification, optimized for stable long-document rendering.'),
                ('Agent Stream Doctor — LLM Streaming Diagnostics', '2025 — 2026  ·  Open Source',
                 'Zero-dependency Python toolkit that diagnoses why an LLM stream returns nothing: reasoning-only '
                 'responses, missing finish_reason, malformed SSE framing and truncated tool calls. Built from '
                 'real-world debugging of LLM router integrations.'),
                ('Custom Counseling Center AI Bot', '2024  ·  Freelance',
                 'Designed and integrated an intelligent automated assistant for a counseling center using modern LLM '
                 'APIs to handle client queries and automate interaction workflows, measurably reducing human-agent '
                 'workload for frequent inquiries.'),
                ('Educational Website & CMS (Django)', '2023 — 2024  ·  Client Project  ·  Live at drkaman.ir',
                 'Django-based CMS platform with secure user authentication, PostgreSQL integration, multi-format '
                 'media management (video/audio playback) and dynamic categorized content delivery, deployed with '
                 'nginx and gunicorn on a Linux VPS.'),
                ('Exam Analysis & Statistics System', '2023  ·  Client Project',
                 'Data-focused web application that ingests student test scores, calculates statistical variances and '
                 'standard deviations, and exports PDF reports with visual analytics for performance evaluation.'),
                ('KamanBrowser — Desktop Web Browser', '2022 — 2023  ·  Personal',
                 'Modern desktop web browser built with C# and Windows Forms on Edge WebView2 (Chromium): tab '
                 'management, bookmarks, custom UI components and smooth navigation with a minimal memory footprint.'),
                ('Kaman Messenger — Encrypted Real-Time Chat', 'Personal',
                 'Real-time encrypted messenger built completely from scratch: raw TCP sockets, AES (Fernet) encryption, '
                 'bcrypt authentication, rate limiting and SQLite storage, with a CustomTkinter GUI.'),
                ('Planikaa Portal — Educational Platform', 'Web Platform',
                 'Comprehensive educational platform with an exam-analytics dashboard, blog and student resources, '
                 'built with Django.'),
                ('Kaman AI Chat — Desktop Voice Assistant', 'Personal',
                 'C# desktop chat assistant running DeepSeek models via OpenModel API, with Google Cloud Text-to-Speech '
                 'voice output for natural conversations. Built with Bunifu UI.'),
                ('Quran Group Bot — Serverless Bale Bot', 'Personal',
                 'Serverless bot for weekly Quran juz reading groups on Bale Messenger: Cloudflare Workers + KV, '
                 'cron-scheduled posts and automatic hadith sharing.'),
                ('YouTube Downloader — Desktop Utility', 'Personal',
                 'Professional YouTube downloader with a modern Persian RTL interface, live progress and quality '
                 'selection. Built with Python, CustomTkinter and yt-dlp.'),
            ]),
            ('Technical Skills', [
                ('Programming Languages', '', 'Python, C#, JavaScript, HTML, CSS'),
                ('Frameworks & Libraries', '', 'Django, Windows Forms, PyQt6, CustomTkinter, Bootstrap'),
                ('Databases', '', 'SQLite, PostgreSQL'),
                ('AI & LLM Engineering', '', 'Gemini API, OpenAI API, DeepSeek, SSE Streaming, Tool Calling, Bot Integration, PDF/Epub Processing'),
                ('Tools & Infrastructure', '', 'Git, nginx, gunicorn, Linux VPS, Cloudflare Workers/KV, REST APIs, VS Code, PyCharm, Visual Studio'),
                ('Networking', '', 'Infrastructure Troubleshooting, Proxy Configurations, Network+ Concepts'),
            ]),
            ('Education', [
                ('Secondary Education (High School)', 'Expected Graduation: Mid-2028',
                 'Data Structures & Algorithms  ·  Machine Learning Fundamentals (freeCodeCamp Track)  ·  '
                 'Advanced Mathematics, Logic and Statistics  ·  Networking Concepts (Network+ Preparation)'),
            ]),
            ('Languages', [
                ('Persian (Farsi)', '', 'Native'),
                ('Arabic', '', 'Fluent — strong communication and understanding'),
                ('English', '', 'Upper-Intermediate (technical documentation & professional communication)'),
            ]),
        ],
    },
    'fa': {
        'file': 'Mohammad_Hasan_Kaman_CV_fa.pdf',
        'rtl': True,
        'name': 'محمد حسن کَمَن',
        'role': 'توسعه‌دهنده فول‌استک (دورکاری)',
        'contact': 'mohammadhasankaman@gmail.com   |   آلمان (دورکاری)   |   نمونه‌کار: mhkaman.com',
        'links': 'linkedin.com/in/kaman-programmer    |    github.com/Mohammad-Hasan-Kaman    |    t.me/mohaka0975',
        'summary': 'توسعه‌دهنده فول‌استکِ خودآموخته با پایه‌ای قوی در پایتون، سی‌شارپ و جاوااسکریپت و بیش از ۳ سال تجربه '
                   'عملی در ساخت نرم‌افزارهای آماده پروداکشن — از اپلیکیشن‌های دسکتاپ مبتنی بر هوش مصنوعی و یکپارچه‌سازی LLM '
                   'تا پلتفرم‌های جنگو مستقر روی سرور لینوکس با nginx و gunicorn. علاقه‌مند به حل مسائل الگوریتمی و سطح-سیستم '
                   'و ساخت پلتفرم‌های دیتابیس‌محور. در حال تکمیل تحصیلات متوسطه (فراغت: اواسط ۲۰۲۸) و همکاری با مشتریان '
                   'بین‌المللی به‌صورت فریلنس. جویای نقش‌های دورکار بک‌اند یا فول‌استک در تیم‌های همکار.',
        'core': ['توسعه بک‌اند و اتوماسیون', 'یکپارچه‌سازی و مدیریت API (REST و LLM)',
                 'طراحی و معماری پایگاه داده', 'توسعه اپلیکیشن‌های هوش مصنوعی (LLM و Streaming)',
                 'معماری اپلیکیشن وب', 'زیرساخت شبکه و عیب‌یابی'],
        'sections': [
            ('پروژه‌های حرفه‌ای', [
                ('پلتفرم ترجمه و اتوماسیون PDF با هوش مصنوعی', '۲۰۲۴ — ۲۰۲۶  ·  فریلنس',
                 'اپلیکیشن دسکتاپ تجاری پایتون برای ترجمه اسناد آکادمیک و فنی PDF/Epub بالای ۵۰۰ صفحه به فارسی با '
                 'Gemini API. شامل پشتیبانی از بیش از ۲۰ زبان، مدیریت پیشرفته کلید API و اعتبارسنجی خودکار لایسنس.'),
                ('ایجنت استریم داکتر — تشخیص خطای استریم LLM', '۲۰۲۵ — ۲۰۲۶  ·  متن‌باز',
                 'جعبه‌ابزار پایتونی بدون وابستگی که علت خالی بودن پاسخ استریم LLM را تشخیص می‌دهد: پاسخ‌های '
                 'فقط-استدلالی، فقدان finish_reason، فریم‌بندی خراب SSE و فراخوانی ابزار ناقص.'),
                ('ربات هوشمند اختصاصی مرکز مشاوره', '۲۰۲۴  ·  فریلنس',
                 'طراحی و یکپارچه‌سازی دستیار هوشمند خودکار برای یک مرکز مشاوره با APIهای مدرن LLM برای پاسخ به '
                 'سوالات مشتریان و خودکارسازی گردش کار، با کاهش محسوس حجم کاری کارشناسان.'),
                ('وب‌سایت آموزشی و سیستم مدیریت محتوا (جنگو)', '۲۰۲۳ — ۲۰۲۴  ·  پروژه مشتری  ·  drkaman.ir',
                 'پلتفرم CMS مبتنی بر جنگو با احراز هویت امن، PostgreSQL، مدیریت رسانه چندرسانه‌ای (ویدیو/صوت) و '
                 'ارائه محتوای پویا؛ مستقر روی سرور لینوکس با nginx و gunicorn.'),
                ('سیستم تحلیل آزمون و آمار', '۲۰۲۳  ·  پروژه مشتری',
                 'اپلیکیشن وب داده‌محور که نمرات آزمون را پردازش، واریانس و انحراف معیار را محاسبه و گزارش PDF با '
                 'نمودارهای تحلیلی برای ارزیابی عملکرد تولید می‌کند.'),
                ('کَمَن‌براوزر — مرورگر دسکتاپ', '۲۰۲۲ — ۲۰۲۳  ·  شخصی',
                 'مرورگر دسکتاپ مدرن با C# و Windows Forms روی WebView2 (کرومیوم): مدیریت تب، بوکمارک، کامپوننت‌های '
                 'سفارشی و ناوبری روان با کمترین مصرف حافظه.'),
                ('پیام‌رسان کَمَن — گفتگوی رمزنگاری‌شده بلادرنگ', 'شخصی',
                 'پیام‌رسان رمزنگاری‌شده بلادرنگ که کاملاً از صفر ساخته شده: سوکت TCP خام، رمزنگاری AES (Fernet)، '
                 'احراز هویت bcrypt، محدودسازی نرخ و پایگاه داده SQLite — با رابط CustomTkinter.'),
                ('پورتال پلنیکا — پلتفرم آموزشی', 'پلتفرم وب',
                 'پلتفرم آموزشی جامع با داشبورد تحلیل آزمون، وبلاگ و منابع دانشجویی — ساخته‌شده با جنگو.'),
                ('چت هوشمند کَمَن — دستیار صوتی دسکتاپ', 'شخصی',
                 'دستیار گفتگوی دسکتاپ با C# که مدل‌های DeepSeek را از طریق OpenModel API اجرا می‌کند و با خروجی صدای '
                 'Google Cloud TTS گفتگوی طبیعی ارائه می‌دهد. ساخته‌شده با Bunifu UI.'),
                ('ربات گروه قرآن — ربات بدون سرور بله', 'شخصی',
                 'ربات بدون سرور برای گروه‌های هفتگی قرائت جزء قرآن در پیام‌رسان بله — Cloudflare Workers و KV با '
                 'زمان‌بندی کرون و اشتراک خودکار حدیث.'),
                ('دانلودر یوتیوب — ابزار دسکتاپ', 'شخصی',
                 'دانلودر حرفه‌ای یوتیوب با رابط کاربری مدرن راست‌به‌چپ فارسی، نمایش زنده پیشرفت و انتخاب کیفیت. '
                 'ساخته‌شده با Python، CustomTkinter و yt-dlp.'),
            ]),
            ('مهارت‌های فنی', [
                ('زبان‌های برنامه‌نویسی', '', 'Python، C#، JavaScript، HTML، CSS'),
                ('فریم‌ورک‌ها و کتابخانه‌ها', '', 'Django، Windows Forms، PyQt6، CustomTkinter، Bootstrap'),
                ('پایگاه داده', '', 'SQLite، PostgreSQL'),
                ('مهندسی هوش مصنوعی و LLM', '', 'Gemini API، OpenAI API، DeepSeek، SSE Streaming، Tool Calling، پردازش PDF/Epub'),
                ('ابزارها و زیرساخت', '', 'Git، nginx، gunicorn، لینوکس VPS، Cloudflare Workers/KV، REST API'),
                ('شبکه', '', 'عیب‌یابی زیرساخت، پیکربندی پراکسی، مفاهیم Network+'),
            ]),
            ('تحصیلات', [
                ('تحصیلات متوسطه (دبیرستان)', 'فراغت متوقع: اواسط ۲۰۲۸',
                 'ساختار داده و الگوریتم‌ها  ·  مبانی یادگیری ماشین (freeCodeCamp)  ·  ریاضیات پیشرفته، منطق و آمار  ·  مفاهیم شبکه (Network+)'),
            ]),
            ('زبان‌ها', [
                ('فارسی', '', 'زبان مادری'),
                ('عربی', '', 'مسلط — ارتباط و درک قوی'),
                ('انگلیسی', '', 'بالاتر از متوسط (مستندات فنی و ارتباط حرفه‌ای)'),
            ]),
        ],
    },
    'ar': {
        'file': 'Mohammad_Hasan_Kaman_CV_ar.pdf',
        'rtl': True,
        'name': 'محمد حسن كَمَن',
        'role': 'مطوّر برمجيات متكاملة (عن بُعد)',
        'contact': 'mohammadhasankaman@gmail.com   |   ألمانيا (عن بُعد)   |   الأعمال: mhkaman.com',
        'links': 'linkedin.com/in/kaman-programmer    |    github.com/Mohammad-Hasan-Kaman    |    t.me/mohaka0975',
        'summary': 'مطوّر برمجيات متكاملة متعلّم ذاتياً بأساس متين في Python و C# و JavaScript وأكثر من ٣ سنوات من الخبرة '
                   'العملية في بناء برمجيات جاهزة للإنتاج — من تطبيقات سطح المكتب المدعومة بالذكاء الاصطناعي وتكاملات LLM '
                   'إلى منصات Django العاملة على خوادم Linux مع nginx و gunicorn. شغوف بحل المشكلات الخوارزمية ومستوى '
                   'النظام وبناء منصات قائمة على قواعد البيانات. أُكمل حالياً التعليم الثانوي (التخرج المتوقع منتصف ٢٠٢٨) '
                   'وأعمل مستقلاً مع عملاء دوليين. أبحث عن أدوار خلفية أو متكاملة عن بُعد ضمن فرق تعاونية.',
        'core': ['تطوير الواجهات الخلفية والأتمتة', 'تكامل وإدارة واجهات البرمجة (REST و LLM)',
                 'تصميم وهندسة قواعد البيانات', 'تطوير تطبيقات الذكاء الاصطناعي (LLM والبث)',
                 'هندسة تطبيقات الويب', 'البنية التحتية للشبكات واستكشاف الأخطاء'],
        'sections': [
            ('المشاريع المهنية', [
                ('منصة ترجمة PDF والأتمتة بالذكاء الاصطناعي', '٢٠٢٤ — ٢٠٢٦  ·  عمل حر',
                 'تطبيق سطح مكتب تجاري بلغة Python لترجمة مستندات PDF/EPUB الأكاديمية والفنية التي تتجاوز 500 صفحة إلى '
                 'الفارسية عبر Gemini API، مع دعم أكثر من 20 لغة وإدارة متقدمة لمفاتيح API والتحقق التلقائي من الترخيص.'),
                ('Agent Stream Doctor — تشخيص بث LLM', '٢٠٢٥ — ٢٠٢٦  ·  مفتوح المصدر',
                 'عدة Python بدون تبعيات تشخّص سبب عودة بث LLM فارغاً: الردود الاستدلالية فقط، غياب finish_reason، '
                 'تلف إطارات SSE واستدعاءات الأدوات المبتورة.'),
                ('بوت ذكاء اصطناعي مخصص لمركز استشارات', '٢٠٢٤  ·  عمل حر',
                 'تصميم ودمج مساعد آلي ذكي لمركز استشارات باستخدام LLM APIs حديثة للتعامل مع استفسارات العملاء '
                 'وأتمتة سير العمل، مع تقليص عبء العمل البشري بشكل ملموس.'),
                ('موقع تعليمي ونظام إدارة محتوى (Django)', '٢٠٢٣ — ٢٠٢٤  ·  مشروع عميل  ·  يعمل على drkaman.ir',
                 'منصة CMS مبنية على Django مع مصادقة آمنة وتكامل PostgreSQL وإدارة وسائط متعددة الصيغ وتقديم محتوى '
                 'ديناميكي مصنّف، عاملة على خادم Linux مع nginx و gunicorn.'),
                ('نظام تحليل الاختبارات والإحصاء', '٢٠٢٣  ·  مشروع عميل',
                 'تطبيق ويب موجّه للبيانات يدخل درجات الاختبارات ويحسب التباينات والانحرافات المعيارية ويصدر تقارير PDF '
                 'مع تحليلات مرئية لتقييم الأداء.'),
                ('كَمَن براوزر — متصفح سطح مكتب', '٢٠٢٢ — ٢٠٢٣  ·  شخصي',
                 'متصفح ويب حديث بـ C# و Windows Forms على Edge WebView2 (Chromium): إدارة تبويبات وعلامات مرجعية '
                 'ومكونات واجهة مخصصة وتنقل سلس بأقل استهلاك للذاكرة.'),
                ('مرسال كَمَن — محادثة مشفّرة فورية', 'شخصي',
                 'مرسال مشفّر فوري مبني بالكامل من الصفر: مقابس TCP الخام، تشفير AES (Fernet)، مصادقة bcrypt، '
                 'تحديد المعدل وقاعدة بيانات SQLite — بواجهة CustomTkinter.'),
                ('بوابة بلانيكا — منصة تعليمية', 'منصة ويب',
                 'منصة تعليمية شاملة مع لوحة تحليلات الاختبارات ومدونة وموارد للطلاب — مبنية بـ Django.'),
                ('دردشة كَمَن الذكية — مساعد صوتي لسطح المكتب', 'شخصي',
                 'مساعد دردشة سطح مكتب بـ C# يشغل نماذج DeepSeek عبر OpenModel API مع مخرجات صوتية من Google Cloud '
                 'TTS لمحادثات طبيعية. مبني بواجهة Bunifu.'),
                ('بوت مجموعة القرآن — بوت بلا خادم على Bale', 'شخصي',
                 'بوت بلا خادم لمجموعات قراءة جزء القرآن الأسبوعية على مرسال Bale — Cloudflare Workers و KV مع '
                 'جدولة cron ومشاركة الأحاديث.'),
                ('محمّل يوتيوب — أداة سطح مكتب', 'شخصي',
                 'محمّل يوتيوب احترافي بواجهة عصرية من اليمين لليسار بالفارسية، مع تتبع التقدم المباشر واختيار '
                 'الجودة. مبني بـ Python و CustomTkinter و yt-dlp.'),
            ]),
            ('المهارات التقنية', [
                ('لغات البرمجة', '', 'Python، C#، JavaScript، HTML، CSS'),
                ('الأطر والمكتبات', '', 'Django، Windows Forms، PyQt6، CustomTkinter، Bootstrap'),
                ('قواعد البيانات', '', 'SQLite، PostgreSQL'),
                ('هندسة الذكاء الاصطناعي و LLM', '', 'Gemini API، OpenAI API، DeepSeek، SSE Streaming، معالجة PDF/EPUB'),
                ('الأدوات والبنية التحتية', '', 'Git، nginx، gunicorn، خوادم Linux، Cloudflare Workers/KV، REST APIs'),
                ('الشبكات', '', 'استكشاف أخطاء البنية التحتية، إعدادات البروكسي، مفاهيم Network+'),
            ]),
            ('التعليم', [
                ('التعليم الثانوي', 'التخرج المتوقع: منتصف ٢٠٢٨',
                 'هياكل البيانات والخوارزميات  ·  أساسيات تعلم الآلة (freeCodeCamp)  ·  رياضيات متقدمة ومنطق وإحصاء  ·  مفاهيم الشبكات (Network+)'),
            ]),
            ('اللغات', [
                ('الفارسية', '', 'لغة أم'),
                ('العربية', '', 'بطلاقة — تواصل وفهم قويان'),
                ('الإنجليزية', '', 'فوق المتوسط (التوثيق التقني والتواصل المهني)'),
            ]),
        ],
    },
}
