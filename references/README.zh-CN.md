# Travel Video Auto Editor

把旅行照片和视频文件夹变成可复现的短视频剪辑方案。技能会扫描尺寸和时长，按素材占比自动选择 16:9、3:4 或 9:16，生成镜头清单、配音文案和可供 FFmpeg 或剪映适配器消费的 `edit-manifest.json`。

```bash
python3 scripts/analyze_media.py ./旅行素材 --output ./output
```

支持用户从抖音、TikTok 或剪映的可用音乐库选择热门歌曲片段，也支持本地音频文件。项目只记录用户选择的歌曲、片段时间和目标平台，不抓取榜单页面或绕过平台访问控制。平台内可用范围应以当前账号、地区和发布入口显示的规则为准。建议使用 MIT License，并分别说明 FFmpeg、剪映/CapCut 适配器、TTS 和第三方音乐许可。
