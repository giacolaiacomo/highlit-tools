"""Builds index.html from tools.json (newest first). usage: python build.py"""
import html, json
tools = json.load(open("tools.json", encoding="utf-8"))
cards = "\n".join(
    f'<article id="{html.escape(t["keyword"].lower())}"><div><h2>{html.escape(t["name"])}</h2><p>{html.escape(t["about"])}</p></div>'
    f'<a class="go" href="{html.escape(t["url"], quote=True)}" rel="noopener">Open the tool</a></article>' for t in tools)
page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>highlit: free tools worth your time</title>
<meta name="description" content="One free, open-source tool a day. Every tool featured by highlit, with its link.">
<link rel="icon" href="img/icon.png">
<style>
@font-face{{font-family:RH;font-weight:800;src:url(fonts/red-hat-display-latin-800-normal.woff2) format("woff2");font-display:swap}}
@font-face{{font-family:RH;font-weight:500;src:url(fonts/red-hat-display-latin-500-normal.woff2) format("woff2");font-display:swap}}
*{{box-sizing:border-box;margin:0}}
body{{background:#101012;color:#fff;font:500 18px/1.5 RH,system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
main{{max-width:760px;margin:0 auto;padding:48px 22px 72px}}
.logo{{height:52px;display:block}}
h1{{font:800 clamp(38px,8vw,60px)/1.05 RH,system-ui,sans-serif;letter-spacing:-.03em;margin:44px 0 16px}}
mark{{background:linear-gradient(transparent 12%,#FFC91F 12%,#FFC91F 92%,transparent 92%);color:#101012;padding:0 .12em;border-radius:.08em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.lead{{color:#b9b9c0;font-size:20px;max-width:34em}}
section{{margin-top:44px;display:grid;gap:14px}}
article{{background:#1a1a1e;border:1px solid #2a2a30;border-radius:18px;padding:22px 24px;display:flex;gap:20px;align-items:center;justify-content:space-between}}
h2{{font:800 24px/1.2 RH,system-ui,sans-serif;letter-spacing:-.01em}}
article p{{color:#b9b9c0;margin-top:6px;font-size:17px}}
.go{{flex:none;background:#FFC91F;color:#101012;font:800 16px RH,system-ui,sans-serif;text-decoration:none;padding:12px 18px;border-radius:999px;white-space:nowrap}}
.go:hover,.go:focus-visible{{background:#fff;outline:none}}
footer{{margin-top:56px;color:#8b8b93;font-size:15px}}
footer a{{color:#fff}}
@media (max-width:560px){{article{{flex-direction:column;align-items:flex-start}}}}
</style></head><body><main>
<img class="logo" src="img/logo.png" alt="highlit">
<h1>One <mark>free tool</mark> a day.</h1>
<p class="lead">Open-source apps you can use without writing code. Every tool from our videos is here, with its link.</p>
<section>
{cards}
</section>
<footer><p>New tool every day on Instagram: <a href="https://www.instagram.com/highlit.ai/">@highlit.ai</a></p>
<p>We only say what each tool's own page states. The voice in our videos is AI-generated. Links go to the tool's own project page; highlit is not affiliated with these projects.</p></footer>
</main></body></html>
"""
open("index.html", "w", encoding="utf-8").write(page)
print("index.html:", len(tools), "tools")
