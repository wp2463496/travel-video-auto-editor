# Edit manifest schema / 编辑清单结构

`edit-manifest.json` is the contract between analysis, story selection, Jianying/CapCut adapters, and the renderer. Required keys are `schema_version`, `source`, `canvas`, `analysis`, `items`, `selection`, `audio`, and `voiceover`.

`canvas.aspect` is `16:9`, `3:4`, or `9:16`; `analysis.shares` contains the measured evidence. Each `items[]` entry has a relative `path`, media kind, dimensions, duration, and orientation. Selected entries should add `start_s`, `end_s`, `crop` (`cover`, `contain`, or `blur-fill`), transition, and reason. Audio should include provider, track id, platform, excerpt start/end, territory, and usage context (for example `in_platform_publish` or `external_export`). Adapters must reject missing licenses and paths outside `source.folder`.
