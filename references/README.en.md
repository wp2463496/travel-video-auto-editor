# Travel Video Auto Editor

Turn a folder of travel photos and videos into a reproducible short-video edit plan. The skill measures dimensions and durations, chooses 16:9, 3:4, or 9:16 from the dominant media share, and writes an `edit-manifest.json` for FFmpeg or a Jianying/CapCut adapter.

```bash
python3 scripts/analyze_media.py ./travel-assets --output ./output
```

The workflow supports user-selected excerpts from Douyin, TikTok, or Jianying in-platform music catalogs, as well as local audio files. It records the track, excerpt timing, target platform, and usage context; it does not scrape chart pages or bypass access controls. Availability depends on the account, territory, and publishing surface. Document separate licenses for FFmpeg, adapters, TTS, and third-party music.
