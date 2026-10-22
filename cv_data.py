"""CV content (2026) for Mohammad Hasan Kaman — EN / FA / AR.

This is the single source of truth for the PDF CV. It is regenerated into
media/cv/*.pdf by generate_cv.py -> portfolio/cv_pdf.py.

Every project below maps 1:1 to a public GitHub repository, and every claim
is backed by that repository's README, release tags or live URL. Claims that
could not be verified were removed rather than softened:
  - "500+ pages / 20+ languages / automated licensing"  -> the translator
    actually ships whole-book EN<->FA PDF/EPUB translation with a QC loop
  - "PostgreSQL" -> the Django projects use SQLite
  - "Google Cloud TTS / Bunifu UI" -> kaman-ai-chat uses the Windows SAPI
    speech engine and plain WinForms
  - "3+ years" -> 4 years of shipped software (2022-2026)
"""

DATA = {
    'en': {
        'file': 'Mohammad_Hasan_Kaman_CV.pdf',
        'rtl': False,
        'name': 'Mohammad Hasan Kaman',
        'role': 'Full-Stack Developer (Remote)',
        'contact': 'mohammadhasankaman@gmail.com   |   Germany (Remote)   |   Portfolio: mhkaman.com',
        'links': 'linkedin.com/in/kaman-programmer    |    github.com/Mohammad-Hasan-Kaman    |    t.me/mohaka0975',
        'summary': 'Self-taught Full-Stack Developer with strong foundations in Python, C# and JavaScript, and 4 years of '
                   'hands-on experience shipping production-ready software — from AI-driven clinical screening '
                   'pipelines, LLM streaming diagnostics and encrypted desktop messengers to Django platforms deployed on '
                   'Linux VPS with nginx and gunicorn. Passionate about solving algorithmic and system-level problems and '
                   'building database-driven platforms. Currently completing secondary education (expected graduation '
                   'mid-2028) while freelancing for international clients. Seeking remote backend or full-stack roles in '
                   'collaborative teams.',
        'core': ['Backend Development & Automation', 'API Integration & Management (REST & LLM)',
                 'Database Design & Architecture', 'AI Application Development (LLM APIs & Streaming)',
                 'Web Application Architecture', 'Network Infrastructure & Troubleshooting'],
        'sections': [
            ('Professional Projects', [
                ('Kaman AI Translator — Whole-Book PDF & EPUB Translation', '2024 — 2026  ·  Freelance  ·  v3.0.0',
                 'Commercial PyQt6 desktop studio that translates complete academic and technical PDF/EPUB books into '
                 'fluent Persian and back into English — page by page or fully unattended. Per-book structure templates '
                 'keep terminology consistent, a QC loop flags meaning drift, work is stored per page with pause/resume, '
                 'API keys are encrypted with Windows DPAPI. 303 offline tests; ships as a Windows .exe.'),
                ('Agent Stream Doctor — LLM Streaming Diagnostics', '2025 — 2026  ·  Open Source  ·  v0.2.0',
                 'Zero-dependency Python toolkit that diagnoses why an LLM stream returns nothing: reasoning-only '
                 'responses, missing finish_reason, malformed SSE framing and truncated tool calls. Twelve named checks '
                 'with explanations, a tolerant parser that turns malformed input into findings instead of exceptions, '
                 'JSON output for CI and a clean library API.'),
                ('AI Counseling Widget — Intake & Consultant Matching', '2024  ·  Freelance  ·  Live at kahaai.ir  ·  v1.0.0',
                 'Multi-tenant AI intake system for counselling centres, shipped as a Persian RTL chat widget embedded '
                 'with a single script tag. Runs a conversational intake, the GHQ-28 wellbeing screen, clinical concept '
                 'extraction from free text and a self-re-weighting consultant matching engine. No hosted LLM, no '
                 'per-message cost, no visitor data leaving the server.'),
                ('AI Counseling Bot — Bale Messenger Intake', '2024  ·  Freelance  ·  v1.0.0',
                 'The same clinical intake intelligence as a Bale messenger bot: a 12-state guided conversation, the '
                 'GHQ-28 wellbeing screen and a SpiralMatchEngine that re-weights itself from panel feedback. Admins run '
                 'statistics, Excel import/export, broadcasts and engine training from inside the chat. No external API, '
                 'no cloud LLM.'),
                ('Kaman Portfolio — Trilingual Django Portfolio & CV Generator', '2024 — 2026  ·  Personal  ·  Live at mhkaman.com',
                 'The portfolio behind this CV: a trilingual (EN/FA/AR) Django site where every page is editable from the '
                 'Django admin, with a trilingual PDF CV generator that shapes RTL text with HarfBuzz, privacy-friendly '
                 'server-side analytics, and sitemap, robots.txt and llms.txt built in.'),
                ('Kaman Messenger — Encrypted Real-Time Chat', '2022 — 2023  ·  Personal',
                 'Real-time encrypted messenger built completely from scratch: raw TCP sockets, AES (Fernet) encryption, '
                 'bcrypt authentication, rate limiting and SQLite storage, with a CustomTkinter GUI. Ships as a client '
                 'and a server executable.'),
                ('Dr-Kaman Site — Multimedia Archive (Django)', '2023 — 2024  ·  Client Project  ·  Live at drkaman.ir',
                 'Django-based CMS with secure user authentication and SQLite storage, multi-format media management '
                 '(video/audio playback) and dynamic categorized content delivery, deployed with nginx and gunicorn on a '
                 'Linux VPS.'),
                ('Planikaa Portal — Educational Platform (Django)', '2023  ·  Client Project',
                 'Django educational platform for exam and competition analysis: visual dashboards, an educational blog, '
                 'a review and feedback system, Jalali (Persian) calendar support and django-allauth accounts. SQLite '
                 'storage.'),
                ('Kaman Web Browser — Desktop Web Browser', '2023  ·  Personal',
                 'A desktop web browser built in C# on the Edge WebView2 (Chromium) engine: tabbed navigation, address '
                 'bar with search fallback, back/forward history, bookmarks and a native Windows shell around a real '
                 'browser engine.'),
                ('Kaman AI Chat — Desktop Chat Assistant (C#)', '2023  ·  Personal',
                 'C# WinForms chat assistant running DeepSeek models via the OpenModel API, with voice output through the '
                 'Windows built-in text-to-speech engine. The API key is resolved at runtime from an environment variable, '
                 'app.config or a per-user settings file — never baked into the source. Single dependency-free .exe.'),
                ('Quran Group Bot — Serverless Bale Bot', '2023  ·  Personal',
                 'Serverless bot for weekly Quran juz reading groups on Bale Messenger: Cloudflare Workers + KV, '
                 'cron-scheduled posts, rotating juz assignment and a weekly hadith. No server, no hosting bill.'),
                ('YouTube Downloader — Desktop Utility', '2023  ·  Personal',
                 'Windows YouTube downloader built on yt-dlp with a Persian dark-mode GUI, three live progress bars, '
                 'video and audio format selection and browser-cookie support for age-restricted or private links.'),
            ]),
            ('Technical Skills', [
                ('Programming Languages', '', 'Python, C#, JavaScript, HTML, CSS'),
                ('Frameworks & Libraries', '', 'Django, Windows Forms, Edge WebView2, PyQt6, CustomTkinter, Bootstrap'),
                ('Databases', '', 'SQLite, SQL, Cloudflare KV'),
                ('AI & LLM Engineering', '', 'Gemini API, OpenAI-compatible APIs, DeepSeek, SSE Streaming, Tool Calling, GHQ-28 screening, concept extraction, PDF/EPUB processing'),
                ('Tools & Infrastructure', '', 'Git, nginx, gunicorn, Linux VPS, Cloudflare Workers/KV, REST APIs, VS Code, PyCharm, Visual Studio'),
                ('Networking & Security', '', 'TCP Sockets, AES/Fernet encryption, bcrypt, rate limiting, proxy configuration, Network+ concepts'),
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
        'summary': 'توسعه‌دهنده فول‌استکِ خودآموخته با پایه‌ای قوی در پایتون، سی‌شارپ و جاوااسکریپت و ۴ سال تجربه '
                   'عملی در ساخت نرم‌افزارهای آمادهٔ پروداکشن — از خط لوله‌های غربال بالینی مبتنی بر هوش مصنوعی، '
                   'ابزارهای تشخیص خطای استریم LLM و پیام‌رسان‌های رمزنگاری‌شده تا پلتفرم‌های جنگو مستقر روی سرور '
                   'لینوکس با nginx و gunicorn. علاقه‌مند به حل مسائل الگوریتمی و سطح-سیستم و ساخت پلتفرم‌های '
                   'دیتابیس‌محور. در حال تکمیل تحصیلات متوسطه (فراغت: اواسط ۲۰۲۸) و همکاری با مشتریان '
                   'بین‌المللی به‌صورت فریلنس. جویای نقش‌های دورکار بک‌اند یا فول‌استک در تیم‌های همکار.',
        'core': ['توسعه بک‌اند و اتوماسیون', 'یکپارچه‌سازی و مدیریت API (REST و LLM)',
                 'طراحی و معماری پایگاه داده', 'توسعه اپلیکیشن‌های هوش مصنوعی (LLM و Streaming)',
                 'معماری اپلیکیشن وب', 'زیرساخت شبکه و عیب‌یابی'],
        'sections': [
            ('پروژه‌های حرفه‌ای', [
                ('مترجم هوشمند کَمَن — ترجمهٔ کامل کتاب‌های PDF و EPUB', '۲۰۲۴ — ۲۰۲۶  ·  فریلنس  ·  v3.0.0',
                 'استودیوی دسکتاپ تجاری با PyQt6 که کتاب‌های آکادمیک و فنی PDF/EPUB را به‌طور کامل به فارسی روان و '
                 'برعکس به انگلیسی ترجمه می‌کند — صفحه‌به‌صفحه یا یک کتاب کامل بدون دخالت. تمپلیت ساختار اختصاصی '
                 'هر کتاب اصطلاحات را یکدست نگه می‌دارد، حلقهٔ QC انحراف معنایی را علامت می‌زند، کار هر صفحه ذخیره '
                 'می‌شود و قابل توقف/ادامه است، و کلید API با Windows DPAPI رمزنگاری می‌شود. ۳۰۳ تست آفلاین؛ '
                 'به‌صورت فایل اجرایی ویندوز.'),
                ('ایجنت استریم داکتر — تشخیص خطای استریم LLM', '۲۰۲۵ — ۲۰۲۶  ·  متن‌باز  ·  v0.2.0',
                 'جعبه‌ابزار پایتونی بدون وابستگی که علت خالی بودن پاسخ استریم LLM را تشخیص می‌دهد: پاسخ‌های '
                 'فقط-استدلالی، فقدان finish_reason، فریم‌بندی خراب SSE و فراخوانی ابزار ناقص. ۱۲ بررسی '
                 'نام‌گذاری‌شده با توضیح، پارسر مقاوم که ورودی خراب را به یافته تبدیل می‌کند نه استثنا، خروجی JSON '
                 'برای CI و API کتابخانه‌ای تمیز.'),
                ('ویجت مشاورهٔ هوشمند — پذیرش و تطبیق مشاور', '۲۰۲۴  ·  فریلنس  ·  زنده در kahaai.ir  ·  v1.0.0',
                 'سامانهٔ پذیرش هوشمند چندمستاجری برای مراکز مشاوره، به‌شکل ویجت چت فارسی و راست‌چین که با یک تگ '
                 'اسکریپت روی هر سایتی می‌نشیند. پذیرش مکالمه‌ای، تست سلامت GHQ-28، استخراج مفاهیم بالینی از متن '
                 'آزاد و موتور تطبیق مشاورِ خودتنظیم را اجرا می‌کند. بدون LLM ابری، بدون هزینهٔ هر پیام و بدون خروج '
                 'دادهٔ مراجع از سرور.'),
                ('ربات مشاورهٔ هوشمند — پذیرش روی بله', '۲۰۲۴  ·  فریلنس  ·  v1.0.0',
                 'همان هوش پذیرش بالینی، این بار به‌شکل ربات پیام‌رسان بله: گفتگوی هدایت‌شده با ۱۲ وضعیت، تست '
                 'GHQ-28 و موتور SpiralMatchEngine که از بازخورد پنل خودش را بازتنظیم می‌کند. مدیران آمار، ورود/خروج '
                 'اکسل، پیام همگانی و آموزش موتور را از داخل گفتگو انجام می‌دهند. بدون API خارجی، بدون LLM ابری.'),
                ('پورتفولیوی کَمَن — سایت سه‌زبانهٔ جنگو و تولیدکنندهٔ CV', '۲۰۲۴ — ۲۰۲۶  ·  شخصی  ·  زنده در mhkaman.com',
                 'پورتفولیویی که همین رزومه در آن قرار دارد: سایت سه‌زبانهٔ (انگلیسی/فارسی/عربی) جنگو که همهٔ '
                 'صفحه‌هایش از پنل ادمین قابل ویرایش است، به‌همراه تولیدکنندهٔ CV سه‌زبانهٔ PDF با شکل‌دهی متن '
                 'راست‌به‌چپ توسط HarfBuzz، تحلیل حریم‌خصوصی سمت سرور و sitemap، robots.txt و llms.txt آماده.'),
                ('پیام‌رسان کَمَن — گفتگوی رمزنگاری‌شده بلادرنگ', '۲۰۲۲ — ۲۰۲۳  ·  شخصی',
                 'پیام‌رسان رمزنگاری‌شدهٔ بلادرنگ که کاملاً از صفر ساخته شده: سوکت TCP خام، رمزنگاری AES (Fernet)، '
                 'احراز هویت bcrypt، محدودسازی نرخ و پایگاه داده SQLite — با رابط CustomTkinter. به‌صورت اجرایی '
                 'کلاینت و سرور منتشر می‌شود.'),
                ('سایت دکتر کَمَن — آرشیو چندرسانه‌ای (جنگو)', '۲۰۲۳ — ۲۰۲۴  ·  پروژه مشتری  ·  زنده در drkaman.ir',
                 'پلتفرم CMS مبتنی بر جنگو با احراز هویت امن و ذخیره‌سازی SQLite، مدیریت رسانه چندقالبه (پخش '
                 'ویدیو/صوت) و ارائهٔ محتوای پویا و دسته‌بندی‌شده، مستقر با nginx و gunicorn روی سرور لینوکسی.'),
                ('پورتال پلنیکا — پلتفرم آموزشی (جنگو)', '۲۰۲۳  ·  پروژه مشتری',
                 'پلتفرم آموزشی جنگو برای تحلیل آزمون‌ها و مسابقات: داشبوردهای بصری، وبلاگ آموزشی، سیستم نظرات و '
                 'بازخورد، پشتیبانی از تقویم هجری شمسی و حساب‌های django-allauth. ذخیره‌سازی با SQLite.'),
                ('مرورگر وب کَمَن — مرورگر دسکتاپ', '۲۰۲۳  ·  شخصی',
                 'مرورگر وب دسکتاپی ساخته‌شده با C# روی موتور Edge WebView2 (Chromium): ناوبری با زبانه‌ها، نوار '
                 'آدرس با جست‌وجوی جایگزین، تاریخچهٔ رفت‌وبرگشت، نشانک‌ها و پوستهٔ بومی ویندوز دور یک موتور مرورگر واقعی.'),
                ('چت هوشمند کَمَن — دستیار گفتگوی دسکتاپ (C#)', '۲۰۲۳  ·  شخصی',
                 'دستیار گفتگوی دسکتاپ با C# و WinForms که مدل‌های DeepSeek را از طریق OpenModel API اجرا می‌کند و '
                 'پاسخ را با موتور گفتار داخلی ویندوز می‌خواند. کلید API در زمان اجرا از متغیر محیطی، app.config یا '
                 'فایل تنظیمات کاربر خوانده می‌شود — هرگز در سورس قرار نمی‌گیرد. یک فایل اجرایی مستقل و بدون وابستگی.'),
                ('ربات گروه قرآن — ربات بدون سرور بله', '۲۰۲۳  ·  شخصی',
                 'ربات بدون سرور برای گروه‌های هفتگی قرائت جزء قرآن در پیام‌رسان بله — Cloudflare Workers و KV با '
                 'زمان‌بندی کرون، نوبت‌بندی چرخشی جزء و حدیث هفتگی. بدون سرور و بدون فاکتور هاستینگ.'),
                ('دانلودر یوتیوب — ابزار دسکتاپ', '۲۰۲۳  ·  شخصی',
                 'دانلودر یوتیوب ویندوزی بر پایهٔ yt-dlp با رابط گرافیکی تیره و فارسی، سه نوار پیشرفت زنده، انتخاب '
                 'قالب ویدیو و صدا و پشتیبانی از کوکی مرورگر برای لینک‌های محدودشده یا خصوصی.'),
            ]),
            ('مهارت‌های فنی', [
                ('زبان‌های برنامه‌نویسی', '', 'Python، C#، JavaScript، HTML، CSS'),
                ('فریم‌ورک‌ها و کتابخانه‌ها', '', 'Django، Windows Forms، Edge WebView2، PyQt6، CustomTkinter، Bootstrap'),
                ('پایگاه داده', '', 'SQLite، SQL، Cloudflare KV'),
                ('مهندسی هوش مصنوعی و LLM', '', 'Gemini API، APIهای سازگار با OpenAI، DeepSeek، SSE Streaming، Tool Calling، غربال GHQ-28، استخراج مفهوم، پردازش PDF/EPUB'),
                ('ابزارها و زیرساخت', '', 'Git، nginx، gunicorn، لینوکس VPS، Cloudflare Workers/KV، REST API'),
                ('شبکه و امنیت', '', 'سوکت TCP، رمزنگاری AES/Fernet، bcrypt، محدودسازی نرخ، پیکربندی پراکسی، مفاهیم Network+'),
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
        'summary': 'مطوّر برمجيات متكاملة متعلّم ذاتياً بأساس متين في Python و C# و JavaScript وأربع سنوات من الخبرة '
                   'العملية في بناء برمجيات جاهزة للإنتاج — من خطوط فحص سريري مدعومة بالذكاء الاصطناعي، وأدوات تشخيص '
                   'بث LLM، ورسائل مشفّرة سطح المكتب، إلى منصات Django المنشورة على خوادم Linux مع nginx و gunicorn. '
                   'شغوف بحل المشكلات الخوارزمية ومستوى النظام وبناء منصات قائمة على قواعد البيانات. أُكمل حالياً '
                   'التعليم الثانوي (التخرج المتوقع منتصف ٢٠٢٨) وأعمل مستقلاً مع عملاء دوليين. أبحث عن أدوار خلفية أو '
                   'متكاملة عن بُعد ضمن فرق تعاونية.',
        'core': ['تطوير الواجهات الخلفية والأتمتة', 'تكامل وإدارة واجهات البرمجة (REST و LLM)',
                 'تصميم وهندسة قواعد البيانات', 'تطوير تطبيقات الذكاء الاصطناعي (LLM والبث)',
                 'هندسة تطبيقات الويب', 'البنية التحتية للشبكات واستكشاف الأخطاء'],
        'sections': [
            ('المشاريع المهنية', [
                ('مترجم كَمَن الذكي — ترجمة كتب PDF وEPUB كاملة', '٢٠٢٤ — ٢٠٢٦  ·  عمل حر  ·  v3.0.0',
                 'استوديو سطح مكتب تجاري بـ PyQt6 يترجم الكتب الأكاديمية والفنية PDF/EPUB كاملة إلى فارسية سليمة وإلى '
                 'الإنجليزية — صفحةً صفحة أو كتاباً كاملاً دون إشراف. قوالب بنية خاصة لكل كتاب تحافظ على اتساق '
                 'المصطلحات، وحلقة QC تُعلّم الانحراف المعنى، ويُحفظ العمل لكل صفحة مع إيقاف/استئناف، وتُشفَّر مفاتيح '
                 'API بـ Windows DPAPI. 303 اختباراً دون اتصال؛ يُنشر كملف تنفيذي لويندوز.'),
                ('Agent Stream Doctor — تشخيص بث LLM', '٢٠٢٥ — ٢٠٢٦  ·  مفتوح المصدر  ·  v0.2.0',
                 'عدة Python بدون تبعيات تشخّص سبب عودة بث LLM فارغاً: الردود الاستدلالية فقط، غياب finish_reason، '
                 'تلف إطارات SSE واستدعاءات الأدوات المبتورة. اثنا عشر فحصاً مسمّاة مع شرح، ومحلّل متسامٍ يحوّل المدخلات '
                 'التالفة إلى اكتشافات بدل استثناءات، ومخرج JSON للاستخدام في CI، وواجهة مكتبة نظيفة.'),
                ('أداة مشورة ذكية — الاستقبال ومطابقة المستشارين', '٢٠٢٤  ·  عمل حر  ·  يعمل على kahaai.ir  ·  v1.0.0',
                 'نظام استقبال ذكي متعدد المستأجرين لمراكز الاستشارات، يُطرح كأداة محادثة فارسية كاملة الاتجاه تُدمج عبر '
                 'وسم واحد. يشغّل مقابلة محادثية، وفحص GHQ-28، واستخراج المفاهيم السريرية من النص الحر، ومحرك مطابقة '
                 'مستشارين يعيد ضبط نفسه. دون نموذج سحابي ولا تكلفة لكل رسالة ولا خروج بيانات الزائر من الخادم.'),
                ('بوت مشورة ذكي — الاستقبال عبر مراسلة Bale', '٢٠٢٤  ·  عمل حر  ·  v1.0.0',
                 'نفس ذكاء الاستقبال السريري، لكن كبوت على مراسلة Bale: محادثة موجّهة باثنتي عشرة حالة، وفحص GHQ-28، '
                 'ومحرك SpiralMatchEngine يعيد ضبط نفسه من تغذية راجعة اللوحة. يدير المشرفون الإحصاءات واستيراد/'
                 'تصدير Excel والبثّ وتدريب المحرك من داخل المحادثة. دون API خارجي ولا نموذج سحابي.'),
                ('ملف أعمال كَمَن — موقع Django ثلاثي اللغات ومولّد السيرة الذاتية', '٢٠٢٤ — ٢٠٢٦  ·  مشروع شخصي  ·  يعمل على mhkaman.com',
                 'ملف الأعمال الذي تضمه هذه السيرة الذاتية: موقع Django ثلاثي اللغات (EN/FA/AR) تُحرَّر كل صفحاته من '
                 'لوحة الإدارة، مع مولّد سيرة ذاتية PDF ثلاثي اللغات يشكّل النص من اليمين إلى اليسار عبر HarfBuzz، '
                 'وتحليلات تحافظ على الخصوصية، وsitemap وrobots.txt وllms.txt مدمجة.'),
                ('مرسال كَمَن — محادثة مشفّرة فورية', '٢٠٢٢ — ٢٠٢٣  ·  شخصي',
                 'مرسال مشفّر فوري مبني بالكامل من الصفر: مقابس TCP الخام، تشفير AES (Fernet)، مصادقة bcrypt، تحديد '
                 'المعدل وقاعدة بيانات SQLite — بواجهة CustomTkinter. يُنشر كملفَّذي عميل وخادم.'),
                ('موقع د. كَمَن — أرشيف وسائط متعددة (Django)', '٢٠٢٣ — ٢٠٢٤  ·  مشروع عميل  ·  يعمل على drkaman.ir',
                 'منصة CMS مبنية على Django مع مصادقة آمنة وتخزين SQLite، وإدارة وسائط متعددة الصيغ (تشغيل فيديو/صوت)، '
                 'وتقديم محتوى ديناميكي مصنّف، منشورة مع nginx و gunicorn على خادم Linux.'),
                ('بوابة بلانيكا — منصة تعليمية (Django)', '٢٠٢٣  ·  مشروع عميل',
                 'منصة تعليمية Django لتحليل الاختبارات والمسابقات: لوحات بصرية، ومدونة تعليمية، ونظام مراجعات وتغذية '
                 'راجعة، ودعم التقويم الهجري Solar، وحسابات django-allauth. التخزين عبر SQLite.'),
                ('متصفح كَمَن — متصفح سطح مكتب', '٢٠٢٣  ·  شخصي',
                 'متصفح ويب لسطح المكتب مبني بـ C# على محرك Edge WebView2 (Chromium): تنقّل بتبويبات، شريط عنوان مع '
                 'بحث احتياطي، سجل رجوع وتقدّم، مفضّلة، وغلاف أصلي لويندوز حول محرك متصفح حقيقي.'),
                ('دردشة كَمَن الذكية — مساعد سطح مكتب (C#)', '٢٠٢٣  ·  شخصي',
                 'مساعد دردشة سطح مكتب بـ C# و WinForms يشغّل نماذج DeepSeek عبر OpenModel API وينطق الردّ بمحرك النطق '
                 'المدمج في ويندوز. تُقرأ مفتاح API عند التشغيل من متغيّر بيئة أو app.config أو ملف إعدادات المستخدم — ولا '
                 'تُدمج في الشيفرة أبداً. ملف تنفيذي واحد بلا تبعيات.'),
                ('بوت مجموعة القرآن — بوت بلا خادم على Bale', '٢٠٢٣  ·  شخصي',
                 'بوت بلا خادم لمجموعات قراءة جزء القرآن الأسبوعية على مراسلة Bale — Cloudflare Workers و KV مع جدولة '
                 'cron، وإسناد متناوب للأجزاء، وحديث أسبوعي. دون خادم ولا فاتورة استضافة.'),
                ('محمّل يوتيوب — أداة سطح مكتب', '٢٠٢٣  ·  شخصي',
                 'محمّل يوتيوب لويندوز مبني على yt-dlp بواجهة داكنة فارسية، وثلاثة أشرطة تقدّم حيّة، واختيار صيغة '
                 'الفيديو والصوت، ودعم ملفات تعريف الارتباط للمتصفح للروابط المقيّدة أو الخاصة.'),
            ]),
            ('المهارات التقنية', [
                ('لغات البرمجة', '', 'Python، C#، JavaScript، HTML، CSS'),
                ('الأطر والمكتبات', '', 'Django، Windows Forms، Edge WebView2، PyQt6، CustomTkinter، Bootstrap'),
                ('قواعد البيانات', '', 'SQLite، SQL، Cloudflare KV'),
                ('هندسة الذكاء الاصطناعي و LLM', '', 'Gemini API، واجهات متوافقة مع OpenAI، DeepSeek، SSE Streaming، Tool Calling، فحص GHQ-28، استخراج المفاهيم، معالجة PDF/EPUB'),
                ('الأدوات والبنية التحتية', '', 'Git، nginx، gunicorn، خوادم Linux، Cloudflare Workers/KV، REST APIs'),
                ('الشبكات والأمان', '', 'مقابس TCP، تشفير AES/Fernet، bcrypt، تحديد المعدل، إعدادات البروكسي، مفاهيم Network+'),
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
