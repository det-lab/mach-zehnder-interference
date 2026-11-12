import math
from pathlib import Path
from render_figures import render_svg
p=Path(__file__).resolve().parent/'figures';p.mkdir(parents=True,exist_ok=True)
W,H=960,214
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="960" height="214" fill="white"/>']
for j,title in enumerate(['1. Electric-field vectors','2. Sinusoidal field','3. Wavefronts']):
 x=8+j*320
 parts += [f'<rect x="{x}" y="5" width="306" height="202" rx="7" fill="#f8fafc" stroke="#cbd5e1"/>',f'<text x="{x+153}" y="28" text-anchor="middle" font-size="17" font-family="DejaVu Sans" font-weight="bold" fill="#1f2937">{title}</text>']
# Vectors: densely sampled, signed instantaneous transverse E field
x=8
parts += [f'<line x1="{x+24}" y1="111" x2="{x+284}" y2="111" stroke="#94a3b8" stroke-width="1.5"/>']
for t in range(5,255,7):
 xx=x+28+t; amp=41*math.sin(2*math.pi*t/83)
 if abs(amp)<1.5: continue
 y2=111-amp
 parts += [f'<line x1="{xx:.1f}" y1="111" x2="{xx:.1f}" y2="{y2:.1f}" stroke="#2563eb" stroke-width="1.7"/>']
 if amp>0:parts += [f'<path d="M {xx-3:.1f} {y2+5:.1f} L {xx:.1f} {y2:.1f} L {xx+3:.1f} {y2+5:.1f}" stroke="#2563eb" fill="none" stroke-width="1.6"/>']
 else:parts += [f'<path d="M {xx-3:.1f} {y2-5:.1f} L {xx:.1f} {y2:.1f} L {xx+3:.1f} {y2-5:.1f}" stroke="#2563eb" fill="none" stroke-width="1.6"/>']
parts += [f'<text x="{x+153}" y="193" text-anchor="middle" font-size="12" fill="#475569">E oscillates transverse to travel</text>']
# Sinusoidal plot of the same field as vectors
x=328;cy=111
parts += [f'<line x1="{x+22}" y1="{cy}" x2="{x+284}" y2="{cy}" stroke="#94a3b8" stroke-width="1.4"/>',f'<line x1="{x+24}" y1="169" x2="{x+24}" y2="52" stroke="#94a3b8" stroke-width="1.4"/>']
pts=' '.join(f'{x+28+t:.2f},{cy-41*math.sin(2*math.pi*t/83):.2f}' for t in range(0,254,2))
parts += [f'<polyline points="{pts}" fill="none" stroke="#2563eb" stroke-width="3"/>',f'<text x="{x+12}" y="49" font-size="15" fill="#2563eb">E_y</text>',f'<text x="{x+275}" y="129" font-size="14" fill="#475569">x</text>',f'<text x="{x+153}" y="193" font-size="12" text-anchor="middle" fill="#475569">Field component vs. position</text>']
# Crest planes of equal phase
x=648
for k in range(7):
 xx=x+37+k*36
 parts.append(f'<line x1="{xx}" y1="53" x2="{xx}" y2="155" stroke="#2563eb" stroke-width="2.5"/>')
parts += [f'<line x1="{x+44}" y1="168" x2="{x+252}" y2="168" stroke="#64748b" stroke-width="2"/>',f'<path d="M {x+252} 168 l -10 -5 v 10 z" fill="#64748b"/>',f'<text x="{x+153}" y="192" text-anchor="middle" font-size="12" fill="#475569">Crest planes; propagation to the right</text>']
parts += [f'<text x="{x+153}" y="161" text-anchor="middle" font-family="DejaVu Sans" font-style="italic" font-size="17" fill="#334155">k</text>']
parts.append('</svg>')
s=''.join(parts)
(p/'00_representations.svg').write_text(s)
render_svg(p/'00_representations.svg')
