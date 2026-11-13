"""Draw the lab's Mach-Zehnder setup as editable SVG and render it to PDF.

Original schematic, copyright 2026 Amy Roberts, CC BY 4.0.
The output lens placement follows the author's experimental configuration.
"""
from pathlib import Path
from render_figures import render_svg


def make_setup():
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="330" viewBox="0 0 1120 330">
<title>Mach-Zehnder interferometer with a converging lens after the second beam splitter</title>
<desc>The laser enters the first beam splitter without a lens. Two paths, each reflected by one mirror, recombine at the second beam splitter. One output passes through a converging lens to a screen. L is measured from the lens to the screen.</desc>
<metadata>Copyright 2026 Amy Roberts. ORCID https://orcid.org/0000-0001-8538-9155. CC BY 4.0 https://creativecommons.org/licenses/by/4.0/</metadata>
<defs>
  <marker id="blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#3474c4"/></marker>
  <marker id="orange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#d17a28"/></marker>
  <marker id="gray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#64748b"/></marker>
</defs>
<rect width="1120" height="330" fill="white"/>
<!-- Incident laser and two arms. -->
<path d="M135 245 H250" fill="none" stroke="#475569" stroke-width="3"/>
<path d="M170 245 H200" stroke="#64748b" stroke-width="2" marker-end="url(#gray)"/>
<path d="M250 245 V90 H500" fill="none" stroke="#3474c4" stroke-width="3"/>
<path d="M250 190 V160 M345 90 H380" fill="none" stroke="#3474c4" stroke-width="2.5" marker-end="url(#blue)"/>
<path d="M250 245 H500 V90" fill="none" stroke="#d17a28" stroke-width="3"/>
<path d="M345 245 H380 M500 190 V160" fill="none" stroke="#d17a28" stroke-width="2.5" marker-end="url(#orange)"/>
<!-- Overlapping output beams. These are schematic paths, not a lens ray construction. -->
<path d="M500 88 H1030" fill="none" stroke="#3474c4" stroke-width="2"/>
<path d="M500 92 H1030" fill="none" stroke="#d17a28" stroke-width="2"/>
<path d="M590 88 H620 M850 88 H880" stroke="#3474c4" stroke-width="2" marker-end="url(#blue)"/>
<path d="M590 92 H620 M850 92 H880" stroke="#d17a28" stroke-width="2" marker-end="url(#orange)"/>
<path d="M500 65 V12" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#gray)"/>
<!-- Splitters are translucent; mirrors are opaque. -->
<g stroke="#475569" stroke-width="4">
  <path d="M228 267 L272 223"/>
  <path d="M478 112 L522 68"/>
</g>
<g stroke="#334155" stroke-width="6">
  <path d="M228 112 L272 68"/>
  <path d="M478 267 L522 223"/>
</g>
<path d="M710 40 Q685 90 710 140 Q735 90 710 40 Z" fill="#e0f2fe" fill-opacity="0.75" stroke="#1479ad" stroke-width="2.5"/>
<path d="M1030 35 V155" stroke="#475569" stroke-width="6"/>
<rect x="25" y="225" width="110" height="40" rx="5" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
<!-- Dimension: lens plane to screen plane. -->
<path d="M710 148 V240 M1030 163 V240" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 4"/>
<path d="M710 227 H1030 M710 220 V234 M1030 220 V234" stroke="#64748b" stroke-width="1.8"/>
<g font-family="DejaVu Sans, sans-serif" font-size="18" fill="#334155" text-anchor="middle">
  <text x="80" y="251">Laser</text>
  <text x="250" y="44">Mirror 1</text>
  <text x="250" y="299">First beam splitter</text>
  <text x="500" y="299">Mirror 2</text>
  <text x="710" y="22">Converging lens</text>
  <text x="710" y="170">f = 75 mm</text>
  <text x="1030" y="22">Screen</text>
  <text x="870" y="209" font-size="21" font-style="italic">L</text>
  <text x="875" y="125" font-size="16">Overlapping beams</text>
  <text x="480" y="45" text-anchor="end">Second beam splitter</text>
</g>
<g font-family="DejaVu Sans, sans-serif" font-size="14" fill="#64748b">
  <text x="524" y="16">Other output</text>
  <text x="1080" y="316" text-anchor="end">Top view; not to scale</text>
</g>
</svg>''']
    path = Path(__file__).resolve().parent / 'figures' / '03_setup.svg'
    path.write_text(''.join(parts))
    render_svg(path)


if __name__ == '__main__':
    make_setup()
