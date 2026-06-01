# 🛡️ WipeDown — Zero-Trust Semantic Scraper (v1.0.0)

Prevents prompt injections from web pages & tweets **before** they reach your local coding agent (Hermes, Qwen Code, Cursor, Claude Code, etc.).

WipeDown acts as an automated security proxy firewall. It fetches messy web content, strips malicious formatting manipulation blocks, detects known injection signatures, and uses a local LLM stream to safely neutralize imperative commands into secure, passive documentation context.

---

## 🧠 Programmatic Usage (Recommended for Agents & Brain Stacks)

If you're building or integrating with agentic systems (BrainFood, Cursor, Aider, custom agents, etc.), the recommended way to use WipeDown is through the `WipeDown` class. It provides a clean, silent, and structured interface designed for programmatic consumption.

```python
from wipedown import WipeDown

# Initialize once
firewall = WipeDown(
    model="qwen-3.6",
    api_url="http://127.0.0.1:8080/v1"
)

# Clean any URL or local file
result = firewall.wipe_url("https://example.com/some-article")

print(result["status"])           # "success" or "flagged"
print(result["source"])           # original URL
print(result["content"])          # pristine sanitized text only
print(result["metadata"]["safety_report"])
```

### Structured Output Contract

When using the `WipeDown` class (or `structured=True`), you receive a clean, agent-friendly data contract:

```json
{
  "status": "success",
  "source": "https://...",
  "content": "The actual cleaned, raw text content...",
  "metadata": {
    "timestamp": "...",
    "signatures_checked": [...],
    "sanitization_events": [...],
    "safety_report": "Human-readable safety summary..."
  },
  "error": null
}
```

**Key guarantees:**
- `content` contains **only** the sanitized text (no synthetic headers or safety reports mixed in).
- All operational metadata lives in the `metadata` object.
- Fully malicious input returns `status: "flagged"` with an empty `content`.

This design makes it trivial and safe to pipe WipeDown output directly into knowledge bases, curators, or agent memory systems like BrainFood.

> **Note for existing users:** All previous usage of `wipe_text()`, `wipe_url()`, the CLI, and Docker remains fully supported and unchanged. The new structured path is additive.

---

## 🐳 Quick Start (Docker)

```bash
docker build -t wipedown .
docker run --rm -v $(pwd)/wipedown_output:/app/wipedown_output wipedown fetch https://example.com --strict
```

---

## 💻 Local Install

1. **Open your terminal and navigate to your main project folder:**
   ```bash
   cd /path/to/your/wipedown
   ```

2. **Install the tool locally in "editable" development mode:**
   ```bash
   pip install -e .
   ```

3. **Run the built-in self-test to verify the local inference pipeline:**
   ```bash
   wipedown test
   ```

---

## 🚀 Usage

### Mode A: Local HTTP Proxy (Recommended for Agents)
WipeDown is built to protect autonomous agents (like `Cline`, `Roo Code`, or custom LangChain setups) from web-based prompt injections. Spin up the background defense proxy:

```bash
wipedown serve --port 8010
```

The server spins up at `http://127.0.0.1:8010`. Once running, configure your agent's browser or data-fetching tool to route all external URLs through the WipeDown endpoint:

```text
http://127.0.0.1:8010/fetch?url=https://example.com/untrusted-page
```

You can now configure your coding agent (Aider, Cursor, etc.) to use this endpoint as its web fetch utility destination. WipeDown will securely intercept the page, structurally strip layouts, execute signature tracking, semantically neutralize hidden injection threats, and return a clean, safe Markdown payload to your agent.

### Mode B: Manual CLI Commands

```bash
# Fetch and sanitize a standard webpage
wipedown fetch https://example.com

# Fetch an X/Twitter link via automatic proxy mirror rotation
wipedown fetch https://x.com/username/status/123456789 --strict

# Load and process a local file securely
wipedown fetch file:///path/to/your/document.html

# Pure deterministic mode (structural HTML strip only, no LLM layer)
wipedown fetch https://example.com --no-sanitize
```

---

## ⚙️ Configuration (Bring Your Own Model)

WipeDown is entirely engine-agnostic and interfaces with any OpenAI-compatible API endpoint. You can configure your runtime globally via environment variables or pass them dynamically inline using CLI flags.

| Environment Variable | CLI Flag | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `WIPEDOWN_API_URL` | `-u`, `--api-url` | `http://127.0.0.1:8080/v1` | The base endpoint of your LLM server. |
| `WIPEDOWN_MODEL`   | `-m`, `--model`   | `qwen-3.6` | The specific model identifier to target. |
| `WIPEDOWN_API_KEY` | *N/A* | *None* | Secure bearer token (required for cloud endpoints). |

---

### 🔌 Provider Setup Examples

#### 1. Local `llama.cpp` / `llama-server` (High-Performance Workstation)
If you are running self-hosted hardware via a native server binary:
```bash
export WIPEDOWN_API_URL="http://127.0.0.1:8080/v1"
export WIPEDOWN_MODEL="your-local-model-name"
wipedown test
```

#### 2. Local Ollama Daemon

If you are running Ollama locally in the background, remember to append the `/v1` compatibility layer to the route:

```bash
export WIPEDOWN_API_URL="http://127.0.0.1:11434/v1"
export WIPEDOWN_MODEL="qwen2.5:7b" # Or your preferred local pull
wipedown test
```

#### 3. Cloud Providers (e.g., OpenAI, Groq)

To offload sanitization processing workloads entirely to cloud-hosted acceleration endpoints:

```bash
export WIPEDOWN_API_URL="https://api.openai.com/v1"
export WIPEDOWN_MODEL="gpt-4o-mini"
export WIPEDOWN_API_KEY="sk-proj-..."
wipedown test
```

---

## 🧠 Native Deep Reasoning Model Support

WipeDown features an advanced, multi-key hybrid stream parser engineered specifically for modern reasoning models (such as `Qwen 3.6`, `DeepSeek`, etc.).

When routing data through a reasoning engine, WipeDown isolates and renders the hidden internal thought structures (`reasoning_content`) natively in your console stream before processing the final text output wrapper. This allows you to audit the model's defensive calculations in real-time.

---

## 🤖 Agent Auto-Configuration (Zero-Tinkering)

WipeDown features a native workstation auto-discovery engine designed to let your coding agent configure the environment completely hands-free.

If you are using an autonomous agent (like `Cline` or `Roo Code`), simply instruct it to initialize the system:

```bash
wipedown configure --auto
```

WipeDown will dynamically check for active local inference setups (scanning `llama-server` allocations, checking `Ollama` daemon registers, and evaluating hardware bounds) and write a perfectly tailored, accelerated `.env` file to your workspace instantly.

---

## ⚖️ Legal Disclaimer & Security Notice

**WipeDown is provided for educational, informational, and experimental purposes only.**

### 1. No Guarantee of Absolute Security
Adversarial AI exploitation techniques, indirect prompt injections, and LLM jailbreaks evolve rapidly. While WipeDown utilizes a multi-stage deterministic and semantic sanitization pipeline to aggressively minimize the attack surface of untrusted web data, **there is no guarantee that it will detect, trap, or neutralize 100% of all past, current, or future adversarial payloads.**

### 2. File Traversal Surface Notice
By utilizing the explicit `file://` parser protocol, users acknowledge they are authorizing the engine context to evaluate files from the local storage boundary directly. Run with caution.

### 3. Human-in-the-Loop Requirement
WipeDown is designed to function as an edge-defense utility and should **never** be used as a standalone, fully autonomous security boundary. Users are strictly advised to maintain an active "Human-in-the-Loop" verification process. Never run connected AI coding agents or terminal execution tools in auto-approve (`--yolo`) modes when feeding web content, regardless of whether the text has been processed by WipeDown.