"""LinkWin brand-mark components for post templates (default logo treatment from 13 Nov 2026).

Treatment "Seal signature + echo" (Ali, 13 Nov 2026: the logo must feel integrated, not pasted on):
  * signature: the official seal traced to a single-colour vector (brand/mark/linkwin-seal.svg) in seal red #AC3E33,
    a hairline rule, then the official 链赢贸易 / LinkWin Trading wordmarks (cropped from the same trace) in the
    design's text tint. No box, tab or background behind it. Sits on the layout's typographic grid (usually the footer).
  * echo (optional): the same seal, very large and very faint (4–7 % opacity, tone-on-tone), cropped by a panel or
    canvas edge, like an emboss in the material.
All shapes come from the official transparent files on linkwinco.com via tools/trace_logo.py; never redraw them.
RTL: dir="rtl" mirrors the signature order automatically (seal on the right); place the echo with `side`.

usage in a day script:
    from linkwin_mark import MARK_CSS, signature, echo
    css += MARK_CSS
    html = f'... {signature()} ...'          # inside a flex/grid cell
    html = f'<div class="panel">{echo("right")} ...</div>'   # panel needs position:relative; overflow:hidden
CSS custom properties to tune per design: --lw-seal (seal colour), --lw-ink (wordmark colour),
--lw-sig-h (seal height, default 58px), --lw-echo (echo colour), --lw-echo-op (echo opacity).
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def svg(name, cls=""):
    s = open(os.path.join(ROOT, "brand", "mark", name), encoding="utf-8").read().strip()
    s = re.sub(r' width="[\d.]+" height="[\d.]+"', "", s, count=1)
    return s.replace("<svg ", f'<svg class="{cls}" aria-hidden="true" preserveAspectRatio="xMidYMid meet" ', 1)

MARK_CSS = """
.lw-sig{--lw-sig-h:66px;display:flex;align-items:center;gap:18px;flex:none;color:var(--lw-ink,rgba(246,244,239,.86))}
.lw-sig .lw-seal{height:var(--lw-sig-h);width:auto;color:var(--lw-seal,#AC3E33);display:block}
.lw-sig .lw-rule{width:1px;align-self:stretch;margin:4px 0;background:currentColor;opacity:.35}
.lw-sig .lw-words{display:flex;flex-direction:column;gap:8px;align-items:flex-start}
.lw-sig .lw-cn{height:calc(var(--lw-sig-h) * .42);width:auto;display:block}
.lw-sig .lw-en{height:calc(var(--lw-sig-h) * .25);width:auto;display:block;opacity:.78}
[dir=rtl] .lw-sig .lw-words{align-items:flex-end}
.lw-echo{position:absolute;pointer-events:none;width:var(--lw-echo-size,520px);height:var(--lw-echo-size,520px);
  color:var(--lw-echo,#F6F4EF);opacity:var(--lw-echo-op,.055);z-index:0}
.lw-echo svg{width:100%;height:100%;display:block}
"""

def signature():
    return (f'<div class="lw-sig">{svg("linkwin-seal.svg", "lw-seal")}<i class="lw-rule"></i>'
            f'<span class="lw-words">{svg("linkwin-wordmark-cn.svg", "lw-cn")}{svg("linkwin-wordmark-en.svg", "lw-en")}</span></div>')

def echo(side="right", bottom="-120px", inset="-90px", rotate="0deg"):
    return (f'<div class="lw-echo" style="bottom:{bottom};{side}:{inset};transform:rotate({rotate})">'
            f'{svg("linkwin-seal.svg")}</div>')
