# law-monitoring
law monitoring service

## Cloud Deployment

1. Copy `.env.example` to `.env` and fill in the required secrets.
2. Use writable paths such as `/tmp/law-monitoring-data` for SQLite, PDF output, and cache files.
3. Start the app with `./run_cloud.sh web` for the web server or `./run_cloud.sh monitor` for a monitoring run.

Example environment values:

```env
LAW_API_KEY=your_law_api_key_here
SECRET_KEY=change-this-in-production
WEB_HOST=0.0.0.0
WEB_PORT=5000
WEB_DEBUG=false
LAW_MONITOR_DATA_DIR=/tmp/law-monitoring-data
DB_PATH=/tmp/law-monitoring-data/law_monitor.db
PDF_OUTPUT_DIR=/tmp/law-monitoring-data/pdf
LAW_ID_CACHE_PATH=/tmp/law-monitoring-data/cache/law_ids.json
LOG_LEVEL=INFO
LOG_FILE_PATH=
MAIL_HOST=smtp.gmail.com
MAIL_PORT=465
MAIL_USER=your_mail_account
MAIL_PASSWORD=your_app_password
MAIL_TO=alerts@example.com
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini
OPENAI_API_BASE=https://api.openai.com/v1
```

Quick start:

```bash
cd /home/lhh/workspace/law-monitoring
cp .env.example .env
chmod +x run_cloud.sh
./run_cloud.sh web
```

If your platform injects `PORT`, `run_cloud.sh` will use it automatically.
