# Video Downloader API (Flask + yt-dlp)

Small Flask API for downloading media through `yt-dlp` on systems you control.

> **Development project:** Do not expose this service publicly without authentication, strict URL/network restrictions, quotas and download storage limits. Download content only where you have permission and comply with the source platform's terms.

## Requirements

- Python environment compatible with the installed `requirements.txt`
- ffmpeg when required by chosen media formats
- Sufficient local disk space

## Local setup

```bash
git clone https://github.com/Kelumsameera/myvd_api.git
cd myvd_api
python -m venv .venv
# Activate .venv for your shell
pip install -r requirements.txt
python app.py
```

The current application uses Flask's development server; it is not suitable for serving untrusted internet traffic.

## API

### POST /download

Request body:

```json
{ "url": "https://example.com/your-authorized-media" }
```

On success, the API returns a title, a saved filename and status. Downloaded media is stored under `downloads/`.

The currently published implementation does not fully validate URLs or restrict download targets; never send untrusted URLs to it. Basic JSON validation is now included, and running `python app.py` uses `debug=False`. These changes do **not** prevent SSRF, resource exhaustion or unauthorized downloads.

## Before any real deployment

- Add login/API authentication and rate limiting.
- Enforce permitted URL schemes, known-safe destinations, safe redirects and outbound-network isolation.
- Restrict file sizes, timeouts, concurrency and storage growth; handle cleanup.
- Review platform terms and copyright permissions.
- Add automated tests for malformed input and denied network targets.

## Status

This README documents the code and limitations. It is not a claim that the service has passed production security testing.
