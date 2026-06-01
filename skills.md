# WipeDown CLI Skill

This skill allows agents to use WipeDown via the command line for secure web content fetching and sanitization.

## Installation

```bash
pip install -e .
```

## Core Commands

### `wipedown fetch <url>`
Fetch and sanitize a URL (or local file).

**Examples:**
```bash
wipedown fetch https://example.com/article
wipedown fetch https://x.com/user/status/123 --strict
wipedown fetch file:///path/to/local.html
```

**Useful Flags:**
- `--strict`: Abort on any signature match
- `--no-sanitize`: Skip LLM sanitization (structural strip only)
- `--content-only`: Return only clean content (no safety report)

### `wipedown serve`
Start the local HTTP proxy server (recommended for agents).

```bash
wipedown serve --port 8010
```

Agents can then route requests through:
`http://127.0.0.1:8010/fetch?url=...`

### `wipedown test`
Run the built-in validation suite.

### `wipedown configure --auto`
Auto-detect local LLM setup and write `.env` file.

## Environment Variables

| Variable              | Description                          | Default                  |
|-----------------------|--------------------------------------|--------------------------|
| `WIPEDOWN_API_URL`    | OpenAI-compatible endpoint           | `http://127.0.0.1:8080/v1` |
| `WIPEDOWN_MODEL`      | Model name                           | `qwen-3.6`                 |
| `WIPEDOWN_API_KEY`    | API key (for cloud providers)        | *(none)*                   |

## Common Agent Patterns

**1. Proxy Mode (Best for Agents)**
Start once in background, then route all web requests through WipeDown.

**2. One-shot Fetch**
Use `wipedown fetch` when you need clean content from a specific URL.

**3. Strict Mode**
Use `--strict` when you want to fail fast on any detected injection attempt.

## Notes for Agents

- WipeDown is designed to be safe and silent.
- When using programmatically, prefer the `WipeDown` Python class over shelling out.
- The CLI is great for quick tasks or when an agent needs to shell out for isolation.