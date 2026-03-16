import os
import json

# Domains
DOMAIN1 = "https://practice.automationtesting.in/"
DOMAIN2 = "https://demoqa.com/"

# NOTE:
# - Do NOT commit real credentials to the repository.
# - Provide credentials and large headers/cookies via environment variables (or a local .env that is in .gitignore).
# - You can put an example file .env.example in repo to show keys.

def _load_json_env(name, default=None):
    raw = os.getenv(name)
    if not raw:
        return default or {}
    try:
        return json.loads(raw)
    except Exception:
        # fallback: try simple key=value pairs (optional)
        return default or {}

class Data:
    # Load cookies/headers/data from environment so we never commit them into the repo
    # Example usage locally:
    # export API_COOKIES='{"wordpress_test_cookie":"WP Cookie check"}'
    # export API_HEADERS='{"user-agent":"my-agent"}'
    # export API_DATA='{"username":"me@example.com","password":"secret"}'
    cookies = _load_json_env("API_COOKIES", {})
    headers = _load_json_env("API_HEADERS", {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
    })
    data = _load_json_env("API_DATA", {
        # Provide defaults or empty strings; do not hardcode real credentials here.
        "username": os.getenv("API_USER", ""),
        "password": os.getenv("API_PASS", ""),
        "login": "Login",
    })
