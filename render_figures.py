"""Render editable SVGs with librsvg, or CairoSVG if installed."""
from pathlib import Path
import shutil
import subprocess


def render_svg(source):
    source = Path(source)
    target = source.with_suffix('.pdf')
    converter = shutil.which('rsvg-convert')
    if converter:
        subprocess.run([converter, '--format=pdf', '--output', str(target), str(source)], check=True)
    else:
        try:
            import cairosvg
        except ImportError as exc:
            raise SystemExit('Install librsvg (rsvg-convert) or pip install -r requirements.txt') from exc
        cairosvg.svg2pdf(url=str(source), write_to=str(target))
    print(target.name)


if __name__ == '__main__':
    for source in sorted((Path(__file__).resolve().parent / 'figures').glob('*.svg')):
        render_svg(source)
