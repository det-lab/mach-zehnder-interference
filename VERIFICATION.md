# Verification

Verified on November 12, 2026.

- Recovered all source-archive files. All eight SVGs are included. Seven SVGs and the archived PNG remain byte-identical to the recovered originals. The superposition SVG has only the requested heading change and added unequal-amplitude explanation.
- Worksheet content from Part B through the end of the document is byte-identical to the recovered LaTeX. The first-page changes are the requested introduction, with compact figure spacing to preserve the original eight-page layout. The redundant snapshot label was removed after review. Author and license links appear in every page footer. Header-height and PDF transparency-group compatibility adjustments do not change the worksheet content or figure geometry.
- Regenerated the triptych SVG from the recovered Python drawing instructions; its SVG output is byte-identical to the archived SVG.
- Converted all eight SVGs to single-page PDFs and compiled the worksheet using `make`.
- The final build produced eight pages with no LaTeX warnings, overfull boxes, or underfull boxes.
- Visually reviewed all eight worksheet pages and the unused alternate figure. The alternate figure retains its original crowded labels because it is archival material, is not included in the worksheet, and was requested to remain unchanged.
- Parsed the final worksheet with pypdf in strict mode and verified clickable ORCID and CC BY 4.0 links on all eight pages.
- Copied the sources into a separate folder excluding all generated PDFs and TeX build files. `make` regenerated every figure PDF and the worksheet. All eight rebuilt pages have identical extracted text and rendered pixels compared with the delivered PDF.

Build environment: TeX Live 2026 (pdfTeX 1.40.29), latexmk 4.88, Python 3, librsvg 2.62.3, Cairo 1.18.4, Pango 1.58.0. Visual checks used rendered page images; structural checks used pypdf, and page-image comparisons used PDFium. Verification packages are not needed to build the worksheet.

The TeX source includes a small compatibility patch for the 2026 graphics driver: Cairo/librsvg figure PDFs already contain transparency groups, so the driver must not add duplicate `/Group` keys. The resulting PDF passes strict parsing and renders identically to the unpatched output.

## Footer and triptych revision

Removed the redundant “Snapshot in time.” label while retaining the introduction's snapshot explanation. The fancyhdr footer now places the page number on the left and the copyright, linked ORCID, and “All materials herein CC BY 4.0” statement on the right. Recompiled successfully to eight pages without warnings. Verified footer alignment, separation, page numbers, and working ORCID/license link annotations on all eight pages; visually checked the revised first and final pages. Figure sources are unchanged by this revision.
