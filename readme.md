# 🛡️ WipeDown — Zero-Trust Semantic Scraper (v0.1.0)

Prevents adversarial prompt injections from untrusted web pages, blogs, and tweets *before* they hit your local AI coding agents (Aider, Cursor, Claude Code, Qwen CLI, etc.).

WipeDown acts as an automated security proxy firewall. It fetches messy web content, strips malicious formatting and hidden structures, runs signature detection, and normalizes active command injections into passive factual data blocks — protecting your local file system and terminal tools from being hijacked.

---

## ⚙️ How It Works (The 4-Stage Pipeline)

1. **Stage 1: Structural Strip** — Aggressively strips non-prose HTML elements (scripts, iframes, hidden CSS blocks, tracking styles, SVGs) and normalizes obfuscated or malicious Unicode/homoglyph characters.
2. **Stage 1.5: Signature Defenses** — Scans raw text blocks using high-speed heuristics for common explicit injection payloads (*"ignore previous instructions"*, *"system override"*, etc.).
3. **Stage 2: Semantic Sanitization** — Pipes text blocks through a lightweight, localized model (`qwen2.5:1.5b`) to translate active imperative commands (*"Download this script and run it"*) into neutral declarative descriptions (*"The text mentions a script"*).
4. **Stage 4: Universal Markdown Output** — Saves clean, distraction-free markdown files straight to your workspace folder for seamless agent ingestion.

If Ollama is not running, WipeDown gracefully falls back to deterministic structural cleaning only.

---

## 📋 Prerequisites

WipeDown runs completely locally for total data privacy. For the **Semantic Sanitization pass (Stage 2)**, you need a local instance of [Ollama](https://ollama.com/) running with the lightweight model:

```bash
ollama pull qwen2.5:1.5b
```

---

## 🐳 Quick Start (Docker — Most Isolated)

```bash
docker build -t wipedown .
docker run --rm -v $(pwd)/wipedown_output:/app/wipedown_output wipedown fetch https://x.com/elonmusk --strict
```

Output will be saved to `./wipedown_output/`.

---

## 💻 Local Install

1. Open your terminal and navigate to your main project folder:

```bash
cd /path/to/your/wipedown
```

(To verify you are in the right place, run `ls` — you should see your `pyproject.toml` file listed.)

2. Install the tool locally in "editable" development mode:

```bash
pip install -e .
```

3. Run the built-in self-test to verify the pipeline is working:

```bash
wipedown test
```

---

## 🚀 CLI Usage Options

```bash
wipedown fetch https://example.com                    # default full pipeline
wipedown fetch https://example.com --strict           # abort on any injection
wipedown fetch https://example.com --no-sanitize      # deterministic only
wipedown fetch https://example.com --raw              # pure structural strip
wipedown fetch https://x.com/someuser/status/123456 -o ./my-safe-context/
```

---

## 🤖 Zero-Friction Agent Integration Recipes

### Pattern A: Watched Workspace Folder (Cursor / Aider)

```bash
wipedown fetch https://x.com/user/status/123456 -o ~/projects/my-app/.wipedown/
```

Your agent can now be prompted with: *"Review the sanitized context in the .wipedown directory and update the schema tracker accordingly."*

### Pattern B: Terminal Script Pipeline (Qwen Code CLI / Claude Code)

Add this helper to your `~/.bashrc` or `~/.zshrc`:

```bash
qwen-swipe() {
    wipedown fetch "$1" --output ./tmp_ctx/ --strict
    qwen-code --message "Read the sanitized text file in ./tmp_ctx/ and apply the optimization concepts directly to our codebase."
}
```

Usage:

```bash
qwen-swipe https://x.com/username/status/123456789
```

---

## 🎯 "Shoulders, Chest, Pants, Shoes" Pipeline Telemetry

You may notice WipeDown printing fun stage markers during a fetch:

- **Shoulders** 🪞 — Stage 1: Structural HTML strip complete
- **Chest** 🛡️ — Stage 1.5: Signature detection pass
- **Pants** 👖 — Stage 2: Semantic sanitization pass
- **Shoes** 👟 — Output saved to disk

It's just your terminal keeping time with the pipeline.

---

## ⚖️ Legal Disclaimer & Security Notice

**WipeDown is provided for educational, informational, and experimental purposes only.**

### 1. No Guarantee of Absolute Security

Adversarial AI exploitation techniques, indirect prompt injections, and LLM jailbreaks evolve rapidly. While WipeDown utilizes a multi-stage deterministic and semantic sanitization pipeline to aggressively minimize the attack surface of untrusted web data, **there is no guarantee that it will detect, trap, or neutralize 100%, or any, of all past, current, or future adversarial payloads.**

### 2. Human-in-the-Loop Requirement

WipeDown is designed to function as an edge-defense utility and should **never** be used as a standalone, fully autonomous security boundary. Users are strictly advised to maintain an active "Human-in-the-Loop" verification process. Never run connected AI coding agents or terminal execution tools in auto-approve (`--yolo`) modes when feeding web content, regardless of whether the text has been processed by WipeDown.

### 3. Limitation of Liability

In no event shall Magic Made Intelligence LLC, its developers, or its contributors be held liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

---

this may have been vibe coded btw ;)