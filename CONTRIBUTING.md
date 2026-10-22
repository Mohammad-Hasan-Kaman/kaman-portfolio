# Contributing to kaman-portfolio

Thanks for taking the time to contribute. This guide explains how to get a
change merged.

## Before you start

- **Search the issues first.** The bug or feature may already be tracked.
- **Open an issue before a large change.** A short discussion up front avoids
  duplicated work.
- **One topic per pull request.** Mixed changes are hard to review and hard to
  revert.

## Development setup

```bash
git clone https://github.com/Mohammad-Hasan-Kaman/kaman-portfolio.git
cd kaman-portfolio
```

Create a virtual environment, install the dependencies and run the
development server:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`kaman_portfolio/settings.py` is the development settings module and keeps its
values inline. The production module, `kaman_portfolio/settings_prod.py`, reads
its configuration from the environment — `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`,
`DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`, `DJANGO_SSL_REDIRECT`,
`DJANGO_HSTS_SECONDS`, `DJANGO_DB_NAME`, the `DJANGO_EMAIL_*` values and
`DJANGO_SERVER_EMAIL` — with a `.env` file next to `manage.py` as the fallback
source. Copy `.env.example` to `.env` and fill it in; never commit the real
file. Run the production stack with:

```bash
DJANGO_SETTINGS_MODULE=kaman_portfolio.settings_prod gunicorn kaman_portfolio.wsgi
```


## Making a change

1. Create a branch from `main`:

   ```bash
   git checkout -b feature/short-description
   ```

2. Make the change, keeping it focused.

3. Commit with a clear message:

   ```bash
   git add -A
   git commit -m "feat: describe the change in one line"
   ```

4. Push and open a pull request:

   ```bash
   git push -u origin feature/short-description
   ```

## Commit message format

Use the conventional prefixes, in the past tense:

| Prefix | Use it for |
| --- | --- |
| `feat:` | A new feature. |
| `fix:` | A bug fix. |
| `docs:` | Documentation only. |
| `refactor:` | A change that neither fixes a bug nor adds a feature. |
| `chore:` | Build, dependency or housekeeping changes. |
| `test:` | Adding or correcting tests. |

## Pull request checklist

- [ ] The change works on a clean checkout.
- [ ] Tests pass, and new behaviour comes with a test.
- [ ] The README is updated if behaviour or configuration changed.
- [ ] No credentials, API keys, `.env` files or local paths are committed.
- [ ] The diff contains only the files this pull request is meant to change.

## Security

Do not commit secrets, tokens, passwords or private URLs. If you find a
vulnerability, report it privately through GitHub's security advisory form
rather than a public issue.

## License

By contributing you agree that your contribution is licensed under the
[MIT License](LICENSE) of this repository.
