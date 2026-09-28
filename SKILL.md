---
name: travel-video-auto-editor
description: Analyze a folder of travel photos and videos, choose the dominant aspect ratio, and produce a ready-to-render short-video edit plan or draft. Use for automated travel reels, Douyin/TikTok-style edits, voiceover, captions, and Jianying/CapCut workflows; support platform-cleared, user-supplied, or separately licensed audio.
---

# Travel Video Auto Editor

Turn a user-selected folder of travel media into a reproducible edit. The deliverable is an `edit-manifest.json`, a bilingual shot list, and—when the local runtime is available—a rendered draft or a Jianying/CapCut import package.

## Operating contract

- Treat the user-provided folder as the only source of media unless they explicitly add a library or URL.
- Inspect every image/video before editing. Preserve the source files and write generated files to a separate `output/` directory.
- Choose the canvas from measured media: use 16:9 when its weighted share is greater than or equal to 55%, 3:4 when portrait 3:4 media reaches 55%, otherwise use 9:16 for short-video distribution. Explain the decision in the manifest. Users can override this with `--aspect`.
- Support short excerpts from a platform-cleared Douyin/TikTok/Jianying music catalog when the user intends to publish through that platform. Accept a user-provided audio clip or provider track id; do not scrape chart pages or bypass platform access controls. Record platform, track id, excerpt start/end, territory, and usage context in `audio.license`.
- Keep the edit deterministic: stable sort by capture time then filename, seeded transition selection, and a manifest containing all decisions.
- Never claim that an export is a native Jianying draft unless the target Jianying/CapCut schema and runtime are actually available. Otherwise provide an importable edit plan and an FFmpeg draft.

## Workflow

1. Resolve the folder and validate supported extensions (`.jpg`, `.jpeg`, `.png`, `.webp`, `.heic`, `.mp4`, `.mov`, `.m4v`, `.webm`, `.mkv`). Reject missing folders with a concrete fix.
2. Run `scripts/analyze_media.py <folder> --output <output-dir>`. Read its JSON; do not infer dimensions from filenames. It records duration, dimensions, orientation, timestamps where available, and a safe-to-share relative path.
3. Group clips into a simple travel story: hook (best establishing shot), arrival/context, detail/food/people, movement, and closing. Prefer sharp, well-exposed, non-duplicate media; preserve all rejected items in `selection.rejected` with reasons.
4. Create voiceover in the requested language. Keep claims grounded in visible media and user-provided facts. If no TTS engine is configured, write `voiceover/script.txt` and mark synthesis as pending.
5. Select music from the supplied file, a platform music catalog, or a licensed provider. Match tempo and mood, and allow incomplete excerpts. Store the track id, provider, platform, excerpt timing, usage context, and volume ducking in the manifest.
6. Generate the bilingual shot list and render with the configured backend. The default backend is FFmpeg for a portable draft; a Jianying backend may consume the same manifest through `references/jianying-adapter.md`.
7. Validate the output with `ffprobe` when available: canvas ratio, duration, audio stream, and that no source path escaped the selected folder. Report warnings instead of silently dropping media.

## Commands

```bash
python3 scripts/analyze_media.py ./my-trip --output ./output
python3 scripts/analyze_media.py ./my-trip --output ./output --aspect 9:16 --language zh-CN
```

Read [references/manifest-schema.md](references/manifest-schema.md) when creating or consuming the manifest, [references/jianying-adapter.md](references/jianying-adapter.md) for a Jianying/CapCut integration, and [references/README.en.md](references/README.en.md) or [references/README.zh-CN.md](references/README.zh-CN.md) when packaging or publishing this skill.

## Quality gates

- Every selected item has a source path, start/end or still duration, crop policy, and reason.
- Canvas choice is measurable and documented; portrait images are not stretched.
- Voiceover and music are ducked under narration, with an explicit source and platform-usage record.
- Output is reviewable before any upload or publication. Never publish to a platform without the user's explicit request.
