# A printed 3D-cinema clip-on for non-magnetic frames

This guide is for making a removable holder that puts flat polarised 3D-cinema film in front of prescription glasses. The film is about 0.2 mm thick and can be cut from cheap passive 3D glasses. Plastic, acetate, titanium and rimless frames need a mechanical attachment when magnets cannot grip them.

The starting design was made for a steel frame with an AI agent writing Python scripts in Blender. It used six 4 × 1 mm neodymium disc magnets epoxied into rear pockets. Film loaded from the back into a 0.4 mm slot and stayed behind retaining lips. The holder was printed upright in PLA at 0.1 mm layers with tree supports. Photos with a coin and 6 mm grid paper supplied scale; hand-drawn outlines supplied the intended shape.

Keep the useful parts of that approach: measured geometry, removable film and small fit tests. Replace the magnet pockets with grips shaped for your own glasses. The old print settings are a starting point for the holder, not proof that a new hook will be strong enough.

## Prerequisites

Gather these before modelling:

- **Your prescription glasses:** inspect them for loose parts, cracks or repairs. Identify sturdy frame surfaces that can take light contact. Rimless lenses and thin metal parts need particular care.
- **Calipers:** measure rim thickness and depth at each proposed grip, bridge width, overall width and the space around the nose pads and hinges. Use light contact; do not squeeze the lenses.
- **Scale photographs:** take front, side, top and close-up views. Include a coin of known diameter and 6 mm grid paper in the same plane as the feature being measured. Record the actual coin diameter. Keep the camera square to that plane and avoid wide-angle close-ups.
- **Hand-drawn outlines:** trace or draw the desired film openings and outside shape. Label left, right, top and dimensions. These outlines define the intended shape; photographs help place it around the glasses.
- **Film:** salvage a left and right film piece from cheap passive 3D-cinema glasses compatible with the cinema system you intend to use. Mark each piece's eye, top edge and front side before removal. Preserve its orientation throughout cutting and loading.
- **Printing materials:** PLA is convenient for rigid shape coupons and the original holder style. PETG is a useful candidate for hooks that must flex, but still needs testing. TPU can make compliant pads or a separate flexible part. None makes an untested clamp safe by itself.
- **Small tools and padding:** sharp scissors suitable for the film, a cutting mat, fine files, deburring tools, tweezers, and thin TPU or soft felt pads. Keep sharp tools away from the prescription lenses.
- **An AI agent and Blender:** ask the agent to generate editable Python scripts with named dimensions. You should be able to change gaps, hook reach and pad thickness without rebuilding everything manually.
- **Printer access:** use a printer or printing service that can reproduce small slots and hooks. Know its nozzle size, material and practical dimensional accuracy. Allow time for several coupons.

Measure the film if possible. The original 0.4 mm film slot provides space around roughly 0.2 mm film, but your printer may narrow that slot. It is a separate dimension from the gap that fits around the prescription frame.

## Choose a grip

Choose contact locations before choosing the outline. A hook that looks tidy but lands on a nose pad, hinge or bare lens face is the wrong hook.

| Mechanism | When to use | Pros | Cons |
| --- | --- | --- | --- |
| Top-rim hooks | A full rim has an accessible, sturdy upper edge. | Simple; easy to install; useful for an early fit trial. | Can swing or lift off; concentrates load at the top; may clash with thick rims. |
| Bottom lips + top hooks, forming an all-sides perimeter clamp | A full rim offers suitable contact around both lens openings. | Distributed grip; self-centring; resists lifting, sliding and rocking. | Needs accurate rim measurements and a planned release motion; too-tight gaps can load the glasses. |
| Bridge saddle | A strong bridge has enough clear space around the nose. | Compact; helps locate the holder centrally; leaves much of the rim clear. | A single support can rock or create a pressure point; may obstruct nose pads or slide on a sloping bridge. |
| Snap-fit over the lens edge with a printed living-hinge | A suitable edge can be captured with very low force and a tested flexible latch. | Can provide a positive latch and an easy release. | Thin printed hinges can split or fatigue; bare rimless lens edges are vulnerable. Prefer capturing a supporting rim; seek an optician's advice before loading a bare lens edge. |
| TPU-lined clamp pads | Sturdy frame areas can accept broad, padded contact. | Cushions contact; accommodates small shape differences; replaceable pads. | Pads add bulk, can creep or collect grit, and change the effective gap. Tightening harder is not a fix for slipping. |
| Flip-up spring hinge | A stable carrier already fits and you want to lift the film out of view. | Convenient switching between viewing positions. | Adds weight, parts and leverage on the glasses; needs stops and a guarded spring. It still needs a reliable frame attachment. |

**Use the all-sides perimeter clamp as the default for a suitable full-rim frame.** Place bottom lips and top hooks around both openings, with side guides where needed. Spreading light contact around the perimeter distributes grip instead of creating one pressure point. Opposing locating surfaces also help the holder self-centre when seated.

“All sides” does not mean squeezing every surface or wrapping plastic across the lenses. Use separated contacts on sturdy frame edges, with clear space around the optical openings. Let the geometry locate the holder; use only enough elastic movement to retain it. Add soft pads where appropriate.

For rimless glasses, there may be no safe perimeter to clamp. Do not transfer a full-rim design directly to exposed lens edges. A suitable bridge or other structural attachment may be needed, and some glasses are unsuitable for this project. Do not force a clamp onto a delicate frame just to use the default mechanism.

## Design rules for a clamp

**Start with 0.15–0.3 mm clearance per side** between rigid printed locating surfaces and the measured frame. For a symmetric gap, that means adding 0.3–0.6 mm overall to the measured thickness. Treat this as an initial range, then tune it with a test coupon. A curved or tapered rim needs measurements at the actual contacts, not one average thickness.

Include the pad thickness in the model. A pad occupies space; adding one later can turn a loose fit into an overloaded clamp. Define the rigid gap, pad thickness and intended pad compression separately. Do not remove all clearance to create retention. A small hook overlap should capture the rim while a supported flexible feature allows installation and release.

**Start with a lip depth of 0.6–1.0 mm** where a lip captures a suitable frame edge. Check this overlap in section views. It must retain the frame without reaching onto the lens face. Keep film-retaining lips separate from frame-gripping lips so their dimensions and functions remain clear.

**Never press on the prescription lens face.** Contact sturdy frame surfaces only. Leave enough separation between film, printed parts and lenses for normal movement, slight flex and manufacturing variation. Check the closest point in side and section views, including strongly curved lenses. If you cannot keep contact off the lens, change the attachment.

Keep the field of view open. Place hooks and ribs outside the useful lens openings and check the view from both eye positions. Avoid the nose pads, their arms, the bridge's underside where it meets the nose, and the temple hinges. Confirm that the temples can open and close and that the holder can be removed without levering against them.

Choose print orientation for strong hooks: **layer lines across, not along, the hook**, so the hook is not a long thin feature that can peel apart along a layer boundary. Inspect the actual sliced paths and expected bending direction; a phrase about orientation alone is not enough. Keep bending loads from opening layer interfaces. If the holder's upright orientation makes the hooks weak, print the hooks separately in a stronger orientation and attach them securely.

Add generous fillets at hook roots rather than sharp inside corners. Provide a clear release tab so removal does not require bending the glasses. A printed living-hinge must have its own material and cycle test; do not assume a thin PLA strip will survive repeated flexing.

Use TPU or felt pads to avoid scratching, and keep both pads and glasses clean. Deburr every contact edge. Supports must be removable without gouging a hook or leaving sharp bumps. Keep adhesive and squeeze-out away from contact areas, film slots and optical openings.

## Prompts

Replace every `<placeholder>` before sending a prompt. Supply the photos, outlines and measurements referred to in the text.

### Build the model from photos and outlines

```text
Create an editable Blender model using a Python script for a removable
3D-cinema film holder for my <frame material and construction> glasses.
Use <photo files> for placement and <hand-drawn outline files> as the
shape truth. Use <measurement list in mm> for dimensions. Preserve my
left/right outline differences. Hold <film thickness> film in rear-loaded
slots with retaining lips; start from <film slot width> mm. Replace
magnet pockets with <chosen grip>. Name the adjustable parameters.
Show front, side and top views. Flag missing dimensions before inventing
any contact geometry.
```

### Establish and prove the scale

```text
Determine true scale from <photo files>. The coin diameter is
<diameter> mm and the grid spacing is 6 mm. Use references in the same
plane as each measured feature. Show the pixel measurements, mm-per-pixel
calculation, and a labelled overlay. Cross-check several grid intervals
against the coin and compare <caliper measurements>. Report disagreement
and perspective error. Do not average incompatible views or call the
scale proven if references disagree. Tell me which photo to retake.
```

### Design and section the clamp

```text
Design an all-sides perimeter clamp for <measured rim sections> using
bottom lips, top hooks and side guides as needed. Start with
<0.15 to 0.3> mm clearance per side and <0.6 to 1.0> mm lip depth.
Include <pad material and thickness>. Spread contact around sturdy frame
edges; never press on lens faces. Keep <nose-pad and hinge keep-outs>
clear and preserve <viewing openings>. Add fillets at hook roots and a
release feature. Show dimensioned sections through every distinct grip,
including contact, clearance, overlap and installation movement.
Explain how it self-centres without squeezing the glasses.
```

### Check fit, stress and the view

```text
Check <model version> against <frame measurements and geometry>.
Show evidence of interference checks, minimum lens clearance, nose-pad
and hinge clearance, installation and release movement, and views from
<left and right eye positions>. Assess hook bending for <material>,
<print orientation> and <estimated installation deflection>. Show the
loads and assumptions behind any stress result; label estimates clearly.
Show the sliced layer direction at hook roots. List failures and revise
them before export. Separate model checks from physical tests still needed.
```

### Make the coupon before the full print

```text
Create a small fit-test coupon for <specific rim contact location> before
exporting the full holder. Include the actual hook root, fillet, lip,
release tab and <pad thickness>. Make labelled variants with
<clearance values> mm clearance per side. Include a short film-slot
sample using <film thickness> and <slot width>. Use <material and printer
settings> and the intended hook orientation. Supply dimensions and an
easy-to-follow test sequence. Success means gentle seating, secure
retention, easy release and no lens contact, marks or frame distortion.
```

## Checks before printing

- [ ] Frame condition is sound, and all contact locations are identified.
- [ ] Coin and grid scale agree with caliper measurements at the relevant locations.
- [ ] Left/right outlines, film pieces and viewing orientation are labelled.
- [ ] The film matches the intended cinema system and covers the useful openings.
- [ ] Clamp clearances include pads and have passed a physical coupon trial.
- [ ] Lip depths and hook overlap capture frame edges without touching lens faces.
- [ ] Sections show space between lenses, film and printed parts throughout installation.
- [ ] Nose pads, hinges, temples and the useful field of view remain clear.
- [ ] Hook roots have fillets; installation and release require only gentle movement.
- [ ] Print orientation and sliced paths support hook bending without layer peeling.
- [ ] Film slots, retaining lips and support removal are practical at the chosen printer settings.
- [ ] Exported parts are solid, use millimetres and have the expected overall dimensions.
- [ ] A retention test and inspection are planned before wearing the finished holder.

## Test coupon first

Print the labelled gap variants in the intended material and orientation. Remove supports and smooth the contact surfaces before testing. First compare each gap with caliper measurements; reject obviously tight variants before bringing them near the glasses.

Seat the best candidate gently at its intended location over a soft surface. Stop if the frame bends, the lens moves, or installation needs force. Check retention and release repeatedly, then inspect for marks, pad movement and hook whitening or cracks. Test the film-slot sample separately. Transfer the successful dimensions to the full model, then check the complete holder again: several grips acting together can fit differently from one coupon.

## Safety

Never use CA glue near the film: its fumes can fog it. Keep film out of the assembly during adhesive work, and follow the adhesive's curing instructions before loading it. A mechanical film retainer avoids putting glue beside the optical surface.

Protect your eyes while cutting, deburring or removing supports. Keep blades and loose fragments away from prescription lenses. This holder and salvaged cinema film are not safety eyewear, impact protection, sunglasses or solar-viewing filters.

Do not apply pressure to lens faces or force a latch around a bare lens edge. Pressure can damage lenses, coatings or frame parts. Stop using the holder if it scratches, shifts, cracks, causes discomfort or changes how your glasses sit. Ask an optician before attaching anything to delicate or rimless glasses.

Driving or walking with 3D film in front of your eyes is unsafe. It darkens and changes the view and can interfere with seeing obstacles. Use it seated for compatible 3D viewing, and remove it before standing, walking or driving.
