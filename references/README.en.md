# Travel Video Auto Editor — English Documentation

Travel Video Auto Editor is a reproducible editing skill for travel creators. Give it a folder of photos and videos; it measures real media metadata, chooses the dominant canvas, plans a story-shaped sequence, and writes an `edit-manifest.json` for FFmpeg, Jianying, or CapCut adapters.

## Core capabilities

- Scan nested folders containing JPG, PNG, WebP, HEIC, MP4, MOV, M4V, WebM, and MKV
- Read dimensions, duration, orientation, and codec information with `ffprobe`
- Automatically choose 16:9, 3:4, or 9:16 from measured media shares
- Override the target canvas with `--aspect`
- Structure a travel story as hook → arrival → details → movement → closing
- Prepare captions, bilingual voiceover scripts, TTS, transitions, and rendering backends
- Use user-selected excerpts from Douyin, TikTok, or Jianying in-platform music catalogs
- Support local audio and separately licensed tracks
- Keep FFmpeg and Jianying/CapCut integrations behind one manifest contract

## Quick start

```bash
cd travel-video-auto-editor
python3 scripts/analyze_media.py ./travel-assets --output ./output
```

Force a vertical short-video canvas:

```bash
python3 scripts/analyze_media.py ./travel-assets \
  --output ./output \
  --aspect 9:16 \
  --language en-US
```

The generated file is:

```text
output/edit-manifest.json
```

## Aspect-ratio rules

- If 16:9 media reaches 55% or more, choose 16:9.
- If 3:4 media reaches 55% or more, choose 3:4.
- Otherwise choose 9:16, suitable for short-video platforms.
- An explicit `--aspect` override always wins.

Images should never be stretched. An adapter should use the manifest crop policy: `cover`, `contain`, or `blur-fill`.

## Music and platform usage

The workflow supports short excerpts selected from music catalogs available inside Douyin, TikTok, or Jianying, as well as local audio files. The manifest records the platform, track ID, excerpt range, target publishing context, and voiceover ducking settings.

The project does not scrape chart pages or bypass platform access controls. In-platform availability can depend on the account, region, and publishing surface.

## Related documentation

- [中文文档](README.zh-CN.md)
- [Manifest schema](../travel-video-auto-editor/references/manifest-schema.md)
- [Jianying / CapCut adapter guide](../travel-video-auto-editor/references/jianying-adapter.md)
- [Skill instructions](../travel-video-auto-editor/SKILL.md)
