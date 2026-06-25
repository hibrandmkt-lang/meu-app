---
name: genimage
description: "Generate, edit, or create any image — photos, illustrations, website visuals, placeholders, icons, thumbnails, banners, or any graphic asset."
allowed-tools: Bash
---

# Nano Banana — Generate Image

Invoke the Nano Banana image generation pipeline using the user's description.

## Instructions

Parse `$ARGUMENTS` to determine mode and flags, then run:

```bash
cd "$(pwd)" && CLAUDE_PLUGIN_ROOT="$(pwd)/.claude/plugins/nano-banana" python "$(pwd)/.claude/plugins/nano-banana/scripts/genimage.py" --prompt "$ARGUMENTS" [options]
```

After generation, read and display the output image file.

If API key error appears, instruct user to run `/nano-banana:setup`.
