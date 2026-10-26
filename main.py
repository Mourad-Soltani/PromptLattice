"""
PromptLattice — Offline structured agent prompt forger.
Signature: Mourad.Soltani
"""
import argparse
import json
import re
import sys
from typing import Dict, Any

SIGNATURE = "Mourad.Soltani"

def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token."""
    return max(1, len(text) // 4)

def forge_prompt(task: str, role: str = "expert assistant", constraints: list = None) -> Dict[str, Any]:
    """Forge a structured prompt from a rough task."""
    if constraints is None:
        constraints = ["Be precise and actionable", "Use clear sections", "Avoid hallucination"]
    
    sections = {
        "role": f"You are a {role} specializing in high-quality outputs.",
        "task": task.strip(),
        "goals": [
            "Produce a complete, usable result",
            "Follow the constraints strictly",
            "Output in the requested format"
        ],
        "constraints": constraints,
        "output_format": "Use markdown with clear headings. End with a summary bullet list."
    }
    
    # Build full prompt text
    full = f"""# Role
{sections['role']}

# Task
{sections['task']}

# Goals
{chr(10).join(f'- {g}' for g in sections['goals'])}

# Constraints
{chr(10).join(f'- {c}' for c in sections['constraints'])}

# Output Format
{sections['output_format']}

Signature: {SIGNATURE}
"""
    
    result = {
        "signature": SIGNATURE,
        "task": task,
        "role": role,
        "sections": sections,
        "full_prompt": full.strip(),
        "estimated_tokens": estimate_tokens(full),
        "quality_score": min(100, 60 + len(task.split()) * 2)  # simple heuristic
    }
    return result

def main():
    parser = argparse.ArgumentParser(description="PromptLattice — Forge structured agent prompts offline.")
    parser.add_argument("task", nargs="?", help="Rough task description")
    parser.add_argument("--role", default="expert assistant", help="Role for the agent")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--file", help="Read task from file")
    args = parser.parse_args()
    
    task = args.task
    if args.file:
        with open(args.file) as f:
            task = f.read().strip()
    if not task:
        print("Usage: python main.py 'your task' or --file task.txt", file=sys.stderr)
        sys.exit(1)
    
    result = forge_prompt(task, args.role)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["full_prompt"])
        print(f"\n---\nEstimated tokens: {result['estimated_tokens']} | Quality score: {result['quality_score']}/100")
        print(f"Built by {SIGNATURE}")

if __name__ == "__main__":
    main()
