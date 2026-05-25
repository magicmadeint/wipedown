# 🛡️ WipeDown — Zero-Trust Semantic Scraper (v0.2.0)

Prevents prompt injections from web pages & tweets **before** they reach your local coding agent (Hermes, Qwen Code, Cursor, Claude Code, etc.).

WipeDown acts as an automated security proxy firewall. It fetches messy web content, strips malicious formatting manipulation blocks, detects known injection signatures, and uses a local LLM stream to safely neutralize imperative commands into secure, passive documentation context.

---

## 🐳 Quick Start (Docker)

```bash
docker build -t wipedown .
docker run --rm -v $(pwd)/wipedown_output:/app/wipedown_output wipedown fetch [https://example.com](https://example.com) --strict
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
Run the background proxy server once to let your agents automatically clean web data on-the-fly:
```bash
wipedown serve
```
The server spins up at `http://127.0.0.1:8010`. You can now configure your coding agent (Aider, Cursor, etc.) to use this endpoint as its web fetch utility destination:
```text
[http://127.0.0.1:8010/fetch?url=https://x.com/username/status/123456789](http://127.0.0.1:8010/fetch?url=https://x.com/username/status/123456789)
```

### Mode B: Manual CLI Commands
```bash
# Fetch and sanitize a standard webpage
wipedown fetch [https://example.com](https://example.com)

# Fetch an X/Twitter link via automatic proxy mirror rotation
wipedown fetch [https://x.com/username/status/123456789](https://x.com/username/status/123456789) --strict

# Load and process a local file securely
wipedown fetch file:///path/to/your/document.html

# Pure deterministic mode (structural HTML strip only, no LLM layer)
wipedown fetch [https://example.com](https://example.com) --no-sanitize
```

---

## ⚖️ Legal Disclaimer & Security Notice

**WipeDown is provided for educational, informational, and experimental purposes only.**

### 1. No Guarantee of Absolute Security
Adversarial AI exploitation techniques, indirect prompt injections, and LLM jailbreaks evolve rapidly. While WipeDown utilizes a multi-stage deterministic and semantic sanitization pipeline to aggressively minimize the attack surface of untrusted web data, **there is no guarantee that it will detect, trap, or neutralize 100% of all past, current, or future adversarial payloads.**

### 2. File Traversal Surface Notice
By utilizing the explicit `file://` parser protocol, users acknowledge they are authorizing the engine context to evaluate files from the local storage boundary directly. Run with caution.

### 3. Human-in-the-Loop Requirement
WipeDown is designed to function as an edge-defense utility and should **never** be used as a standalone, fully autonomous security boundary. Users are strictly advised to maintain an active "Human-in-the-Loop" verification process. Never run connected AI coding agents or terminal execution tools in auto-approve (`--yolo`) modes when feeding web content, regardless of whether the text has been processed by WipeDown.
