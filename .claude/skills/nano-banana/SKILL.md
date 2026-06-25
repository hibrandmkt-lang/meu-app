---
name: nano-banana
description: "Nano Banana — Generate and edit images via Google Gemini. Supports text-to-image, image editing, style transfer, multi-image composition, and high-resolution (2K/4K) output."
---

# Nano Banana — Image Generation

Generate and edit images via the Gemini API. If the API key is missing, run `/nano-banana:setup`.

## Workflow

1. **Determine the mode** from the user's request:
   - **Creating a new image from text?** → Text-to-image (no `--images`)
   - **Editing/retouching an existing image?** → Image editing (`--images source.png`)
   - **Applying one image's style to another?** → Style transfer (`--images style.png target.png`)
   - **Combining or referencing multiple images?** → Multi-image (`--images a.png b.png ...`, up to 14)
   - **Need 2K or 4K output?** → Add `--resolution 2K|4K` to any mode above

2. **Craft the prompt** — describe the desired result narratively.

3. **Run the script:**
```bash
CLAUDE_PLUGIN_ROOT="$(pwd)/.claude/plugins/nano-banana" python "$(pwd)/.claude/plugins/nano-banana/scripts/genimage.py" --prompt "..." [options]
```

4. **Show the result** — read the output image and present it to the user.

## Flags

| Flag | Required | Purpose |
|------|----------|---------|
| `--prompt "text"` | Yes | Describe the desired image |
| `--output file.png` | No | Output path (default: `generated_image.png`) |
| `--images path [...]` | No | Input image(s) — omit for text-to-image |
| `--aspect-ratio RATIO` | No | `1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9` |
| `--resolution RES` | No | `1K` `2K` `4K` (uppercase K required, triggers Pro model) |

## Models

- **Nano Banana 2** (`gemini-3.1-flash-image-preview`): Default. Fast, high-quality.
- **Nano Banana Pro** (`gemini-3-pro-image-preview`): Auto-selected when `--resolution` is set. 4K output.

## Common Use Cases

| Use case | Example |
|----------|---------|
| Website hero image | `--prompt "..." --aspect-ratio 16:9` |
| Instagram post | `--prompt "..." --aspect-ratio 1:1` |
| Stories/Reels | `--prompt "..." --aspect-ratio 9:16` |
| Edit existing photo | `--prompt "remove background" --images photo.png` |
| Style transfer | `--prompt "Apply watercolor style" --images style.png photo.png` |
| High-res asset | `--prompt "..." --resolution 4K` |
