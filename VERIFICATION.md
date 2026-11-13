# Verification

Verified on November 12, 2026.

- Recovered all source-archive files. All eight SVGs are included. Seven SVGs and the archived PNG remain byte-identical to the recovered originals. The superposition SVG has only the requested heading change and added unequal-amplitude explanation.
- Worksheet content from Part B through the end of the document is preserved except for the author-requested revisions to Questions 4(c) and 7 and the use of the directly measured lens-to-screen distance in Parts D and E, documented below. The first-page changes are the requested introduction, with compact figure spacing to preserve the original eight-page layout. The redundant snapshot label was removed after review. Author and license links appear in every page footer. Header-height and PDF transparency-group compatibility adjustments do not change the worksheet content or figure geometry.
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

## Screen-marking wording revision

Changed Question 4(c) to “Mark the three locations on the screen where you predict bright fringes.” Recompiled the eight-page worksheet without warnings and visually checked the revised page.

## Small-angle question revision

Question 7 now asks students to “show that in the small-angle limit” before the unchanged equations. Removed “Write the algebra and identify where the small-angle approximation enters.” Corrected the derivation reference to Question 6, which contains the adjacent-fringe construction. Recompiled to eight pages without warnings and visually checked the revised page.

## Direct lens-to-screen measurement

Replaced the separate beam-splitter distances with the directly measured lens-to-screen distance L throughout Parts D and E. The magnification remains M = |1 - L/f|. The far-screen condition is L >> f, with theta approximately lambda L / (f d_screen); the uncertainty prompt now uses sigma_L/L. Updated the measurement table to record wavelength, focal length, L, fringe spacing, M, and theta, and described moving the screen relative to the lens. Figure sources are unchanged.

Recompiled successfully to eight pages without warnings or overfull/underfull boxes. Confirmed the old D and a variables are absent from worksheet math, checked the L approximation and uncertainty notation, and visually reviewed all three revised pages (6–8).

## Guided Taylor approximation

Expanded Question 7 with an introduction to simplifying complicated expressions, the Taylor formula about zero through the cubic term, and prompts to identify the dimensionless small parameter, construct the sine expansion, compare the neglected term, and recover the small-angle fringe-spacing formula. Added optional links to 3Blue1Brown and MIT OCW Session 99 (Clip 3). The generic function is denoted g to distinguish it from the focal length f. The activity begins on a new page to preserve room for student work; earlier eight-page verification records describe previous revisions.

The current worksheet compiles to nine pages without warnings or overfull/underfull boxes. Verified that both resource links are present as PDF annotations and that Questions 7 and 8 fit together on page 6. Visually reviewed that page. All figure sources are unchanged.

## Far-screen approximation derivation

Removed the phrase “sufficiently differentiable” from the Taylor introduction. Question 14 now asks students to derive theta approximately lambda L / (f d_screen) from Question 12 for L >> f, identify the small dimensionless ratio, and explain which term can be neglected before proceeding to uncertainty propagation. Added work space for this derivation. The final worksheet remains nine pages and compiles without warnings or overfull/underfull boxes. Visually checked the updated Taylor activity and measurement/uncertainty pages.

## Far-screen prompt clarification

Question 14 now explicitly asks: “Explain why the term f/L can be neglected in this limit.” The preceding derivation prompt and formula are unchanged. Recompiled to nine pages without warnings and visually checked the revised page.

## Apparatus schematic and experimental check

Added an original setup schematic and its Python generator. It shows the unexpanded laser input, two beam splitters, two mirrors, and a converging lens in one output after the second beam splitter. The lens-to-screen distance L and focal length f = 75 mm are labeled. The caption explains the choice to keep the beams narrow during alignment. The Thorlabs manual was consulted as an apparatus reference; its artwork is not included, and its input-lens placement is not copied.

Question 14 now asks students to calculate f/L from their experimental values and explain why the term can be neglected. Explicit page breaks keep Question 10 with its hint, the measurement section together, and Question 15 with both subparts. The worksheet now contains ten pages. Earlier page-count records describe previous revisions.

Verified all nine figure sources render, confirmed the original eight SVGs and their PDF exports remain unchanged, and visually reviewed the new schematic and all four affected worksheet pages. Strict PDF parsing succeeds, footer links work on every page, and there are no compilation errors or overfull/underfull boxes. pdfTeX reports its standard multiple-transparency-group inclusion warning on pages containing two Cairo figure exports; this does not affect rendering or strict PDF parsing.

A clean build in a separate folder, excluding all generated PDFs and TeX intermediates, regenerated all figures and the ten-page worksheet. Every rebuilt page has pixels identical to the delivered PDF at the comparison resolution.

## Final-page consolidation

Moved Question 15 onto the same page as Question 14 by placing the measurement table on the preceding page and starting Question 14 on a fresh page. All question text and answer-space lengths are unchanged. The current worksheet is nine pages; Questions 14 and 15 are together on page 9. Compiled successfully without overfull boxes and visually reviewed pages 8 and 9.
