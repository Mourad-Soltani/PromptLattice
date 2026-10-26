# PromptLattice

**Offline CLI for forging structured, high-quality agent prompts.**

Signature: Mourad.Soltani

## What you get

A single-file (plus tests) Python CLI that turns a rough task description into a polished, sectioned prompt ready for Claude, GPT, Gemini, or any coding agent. Includes rough token estimate and quality heuristic. Fully offline, zero dependencies beyond stdlib.

## How to run

```bash
python main.py "Write a secure password generator in Python"
python main.py --role "security engineer" --json "Audit this code for secrets"
python main.py --file task.txt
```

## Requirements

- Python 3.8+
- No external packages

## Health tests

```bash
python -m unittest tests/test_health.py
```

Must pass cleanly.

## License

MIT — Built by Mourad.Soltani
