# Flask Boilerplate with Tailwind Integration

## Installation

Create and activate the virtualenv, then install all dependencies

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set environment variables

```bash
cp .env.example .env
```

Compile tailwind styles

```bash
yarn css:dev (for watch mode)
yarn css:prod (for non-watch mode)
```

Run the application

```bash
python -m main
```
