# 🛡️ WipeDown — Zero-Trust Semantic Scraper (v0.1.0)

Prevents prompt injections from web pages & tweets **before** they reach your local coding agent (Aider, Cursor, Claude Code, etc.).

WipeDown acts as an automated security proxy firewall. It fetches messy web content, strips malicious formatting manipulation blocks, and normalizes active command injections into passive factual markdown documentation.

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

2. **Verify or create the mandatory missing local python structure file:**
   ```bash
   touch wipedown/__init__.py
   ```

3. **Install the tool locally in "editable" development mode:**
   ```bash
   pip install -e .
   ```

4. **Run the built-in self-test to verify the local inference pipeline:**
   ```bash
   wipedown test
   ```

---

## 🚀 Usage

```bash
# Fetch a standard web page
wipedown fetch [https://example.com](https://example.com)

# Fetch an X/Twitter link (Experimental Best-Effort Mirroring)
wipedown fetch [https://x.com/username/status/123456789](https://x.com/username/status/123456789)

# Load and process a local file securely
wipedown fetch file:///path/to/your/document.html
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