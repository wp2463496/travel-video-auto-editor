#!/usr/bin/env python3
import argparse,json,subprocess
from pathlib import Path
I={".jpg",".jpeg",".png",".webp",".heic"}; V={".mp4",".mov",".m4v",".webm",".mkv"}
def probe(p):
 try:
  d=json.loads(subprocess.check_output(["ffprobe","-v","error","-print_format","json","-show_streams","-show_format",str(p)],text=True)); s=next((x for x in d.get("streams",[]) if x.get("codec_type")=="video"),{}); return int(s.get("width") or 0),int(s.get("height") or 0),float(s.get("duration") or d.get("format",{}).get("duration") or 0),s.get("codec_name")
 except Exception:return 0,0,0.0,None
def b(w,h):
 if not w or not h:return "unknown"
 r=w/h
 return "16:9" if abs(r-16/9)<=.12 else "3:4" if abs(r-3/4)<=.12 else "portrait" if r<1 else "landscape"
def main():
 a=argparse.ArgumentParser();a.add_argument("folder");a.add_argument("--output",default="output");a.add_argument("--aspect",choices=["auto","16:9","3:4","9:16"],default="auto");a.add_argument("--language",default="zh-CN");x=a.parse_args();root=Path(x.folder).expanduser().resolve()
 if not root.is_dir():a.error(f"folder does not exist: {root}")
 items=[]
 for p in sorted(root.rglob("*"),key=lambda z:str(z).lower()):
  if p.is_file() and p.suffix.lower() in I|V:
   w,h,d,c=probe(p);items.append({"id":f"shot-{len(items)+1:03d}","path":str(p.relative_to(root)),"kind":"image" if p.suffix.lower() in I else "video","width":w,"height":h,"duration_s":round(d,3),"orientation":b(w,h),"codec":c})
 n=len(items) or 1;counts={k:sum(i["orientation"]==k for i in items) for k in ["16:9","3:4","portrait","landscape","unknown"]};shares={k:round(v/n,4) for k,v in counts.items()};chosen=x.aspect if x.aspect!="auto" else ("16:9" if shares["16:9"]>=.55 else "3:4" if shares["3:4"]>=.55 else "9:16"); wh={"16:9":[1920,1080],"3:4":[1080,1440],"9:16":[1080,1920]}[chosen];m={"schema_version":"1.0","source":{"folder":str(root),"file_count":len(items)},"canvas":{"aspect":chosen,"width":wh[0],"height":wh[1]},"analysis":{"counts":counts,"shares":shares},"language":x.language,"items":items,"selection":{"selected":[],"rejected":[]},"audio":{"music":None,"license":{"status":"pending","usage_context":"in_platform_publish","platform":None,"track_id":None,"excerpt_start_s":0,"excerpt_end_s":None}},"voiceover":{"status":"pending","script_path":"voiceover/script.txt"}};out=Path(x.output);out.mkdir(parents=True,exist_ok=True);(out/"edit-manifest.json").write_text(json.dumps(m,ensure_ascii=False,indent=2));print(json.dumps({"manifest":str(out/"edit-manifest.json"),"files":len(items),"recommended_aspect":chosen,"shares":shares},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
