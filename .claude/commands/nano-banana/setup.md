---
name: setup
description: "Setup the Gemini API key for Nano Banana"
allowed-tools: Bash, AskUserQuestion
---

# Nano Banana — API Key Setup

Configure the Gemini API key to enable image generation.

## Steps

1. Check if key was passed as argument: `$ARGUMENTS`
2. If not provided, ask the user with AskUserQuestion:
   - "Paste your Gemini API key (get one free at https://aistudio.google.com/apikey)"
3. Run:
```bash
CLAUDE_PLUGIN_ROOT="$(pwd)/.claude/plugins/nano-banana" python "$(pwd)/.claude/plugins/nano-banana/scripts/setup_key.py" <key>
```
4. Confirm setup is complete and the user can now use `/genimage`.
