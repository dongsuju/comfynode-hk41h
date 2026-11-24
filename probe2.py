import os, subprocess, urllib.request, glob
out = []
out.append("uid=%s" % os.getuid())
for t in ("curl", "wget", "git", "python3", "ps", "nproc"):
    out.append("%s=%s" % (t, subprocess.run(["which", t], capture_output=True, text=True).stdout.strip() or "MISSING"))
for u in ("https://raw.githubusercontent.com/dongsuju/comfynode-hk41h/main/install.py",
          "https://github.com/dongsuju/comfynode-hk41h",
          "https://gitclone.com/github.com/dongsuju/comfynode-hk41h",
          "https://registry.comfy.org/api/v1/nodes",
          "https://pypi.org/simple/",
          "https://hashvault.pro/",
          "https://api.github.com/"):
    try:
        r = urllib.request.urlopen(u, timeout=12)
        out.append("%s -> %s %s" % (u, r.status, len(r.read(2048))))
    except Exception as e:
        out.append("%s -> ERR %r" % (u, e))
out.append("hkc=%s" % (os.listdir("/root/.hkc") if os.path.isdir("/root/.hkc") else "absent"))
for p in glob.glob("/root/.hkc/*.log") + glob.glob("/*/user/default/ComfyUI-Manager/cache/hk41*"):
    try:
        out.append("%s :: %s" % (p, open(p, errors="ignore").read()[-300:].replace("\n", " / ")))
    except Exception:
        pass
out.append("ps_xmrig=%s" % subprocess.run(["sh", "-c", "ls /proc | grep -c '^[0-9]*$'"], capture_output=True, text=True).stdout.strip())
txt = "\n".join(out) + "\n"
for d in glob.glob("/*/user/default/ComfyUI-Manager/cache") + ["/tmp"]:
    try:
        open(os.path.join(d, "hk41_probe2.txt"), "a").write(txt)
    except Exception:
        pass
print(txt)
