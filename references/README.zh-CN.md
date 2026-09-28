# Travel Video Auto Editor 中文文档

Travel Video Auto Editor 是一个面向旅行内容创作者的自动化视频剪辑 Skill：输入一个包含照片和视频的文件夹，系统读取真实媒体元数据，判断素材主导画幅，生成旅行故事结构、镜头清单、配音计划、平台音乐配置和可复现的 `edit-manifest.json`。

## 核心能力

- 扫描嵌套文件夹中的 JPG、PNG、WebP、HEIC、MP4、MOV、M4V、WebM 和 MKV
- 使用 `ffprobe` 读取尺寸、时长、方向和编码信息
- 按素材占比自动选择 16:9、3:4 或 9:16
- 支持通过 `--aspect` 手动覆盖平台画幅
- 规划“开场 → 到达 → 细节 → 移动 → 收尾”的旅行故事节奏
- 预留字幕、配音、转场、AI TTS 和 FFmpeg 渲染接口
- 支持抖音、TikTok、剪映平台内音乐库的热门歌曲片段
- 支持本地音频和独立授权音乐
- 通过 manifest 对接 FFmpeg、剪映和 CapCut 适配器

## 快速开始

```bash
cd travel-video-auto-editor
python3 scripts/analyze_media.py ./旅行素材 --output ./output
```

强制输出竖屏短视频：

```bash
python3 scripts/analyze_media.py ./旅行素材 \
  --output ./output \
  --aspect 9:16 \
  --language zh-CN
```

输出文件：

```text
output/edit-manifest.json
```

## 画幅选择规则

- 16:9 素材占比大于等于 55%：使用 16:9
- 3:4 素材占比大于等于 55%：使用 3:4
- 其他情况：默认使用 9:16，适合短视频平台
- 用户指定 `--aspect` 后，手动设置优先于自动判断

图片不会被强行拉伸，适配器应根据 manifest 的 `crop` 字段选择 `cover`、`contain` 或 `blur-fill`。

## 音乐使用

项目支持用户从抖音、TikTok 或剪映当前可用的音乐库中选择热门歌曲片段，也支持用户提供本地音频。manifest 会记录：

- 平台
- 歌曲或音频 ID
- 片段起止时间
- 目标发布场景
- 地区或账号相关信息
- 配音时的背景音乐压低参数

项目不会抓取榜单页面，也不会绕过平台访问控制。平台内可用范围取决于当前账号、地区和发布入口。

## 相关文档

- [英文文档](README.en.md)
- [Manifest 结构](../travel-video-auto-editor/references/manifest-schema.md)
- [剪映 / CapCut 适配器](../travel-video-auto-editor/references/jianying-adapter.md)
- [Skill 说明](../travel-video-auto-editor/SKILL.md)
