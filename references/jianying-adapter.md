# Jianying / CapCut adapter

Jianying and CapCut project formats vary by release and are not a stable public interchange API. Keep the manifest as the source of truth. An adapter resolves selected paths, creates the measured canvas, applies crop without stretching, places stills for their requested duration, adds voiceover first, then ducks music by 8–12 dB. It must record the target version and accept a user-selected platform track or local excerpt; never scrape chart pages. If a schema is unavailable, return the manifest and an FFmpeg draft instead of fabricating a native project.
