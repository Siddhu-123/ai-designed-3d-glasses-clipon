# Prompt playbook

These templates are distilled from the prompts I actually used (see `original_prompts.md`). Replace each `<...>`. Send P0 once, at the start, and keep the same session for as long as you can so the agent keeps the context.

They assume an AI coding agent that can run Blender headless and Python (numpy/scipy/matplotlib). Paste the templates as they are. The rules in P0 matter more than the wording of the rest.

---

## P0 · Rules of the game (send first)
```text
I am designing a 3D-printed clip-on that holds flat polarised 3D-cinema film (about 0.2 mm, from passive cinema 3D glasses)
in front of my prescription glasses. Frame: <steel / plastic / titanium / rimless>.
Rules for the whole project:
1. Shape comes ONLY from my hand-drawn outlines <file/object names>. Photos may set size, never shape.
2. Never modify my original objects or files. Build each version in its own folder with a short report
   (what changed, what it achieved, what is lacking, key numbers). Never delete a version.
3. I have one chance to print. Never present a design with a defect your own analysis shows: fix it first.
4. Every claim needs evidence: a number, a plot, a section view or an overlay on my photos.
5. The film can bow in one direction only, never dome.
6. No CA/super glue near the film (fumes fog it). 2-part epoxy only, away from the film.
7. Tell me when you are guessing or struggling, and list what is NOT verified.
```

## P1 · Build the glasses model
```text
Open <file>.blend. It has three reference photos of my glasses (front, top, side) and my outlines.
Build the glasses in 3D from the photos on all three axes (not from any scan).
My photos may be 1-2 degrees off square; you may rotate the images to align them to the model.
Show overlays of the model on each photo and report the alignment error in mm per region.
The front must be exact because I will attach to it. If the frame is symmetric, make a mirror-symmetric version too.
```
Follow-up when it drifts: *"See the shape difference at <place> in this screenshot. Fix the glasses model first, then redo everything that depends on it."*

## P2 · Prove the true scale
```text
Here are photos of my glasses on <6 mm> grid paper with a <coin> (look up its exact diameter), plus the size
printed on the temple <57[]20-145>. Measure the model's scale from each source separately, show the overlays,
and say whether they agree. If one disagrees, show me why before choosing. I want precision like 2.345 mm.
Do not continue to the clip until at least two independent sources agree.
```

## P3 · Film and real parts
```text
Here is a photo of my two film sheets next to a <coin>. Trace each sheet's true outline (do not scale it),
keep left and right separate and mark which face is up. Then show how the film sits over each lens
and what would be cut off. Any line I will cut by hand must be a smooth curve: no photo-trace wiggles.
```

## P4a · Magnets (steel frames)
```text
I have <N> magnets, <4 x 1 mm>, rated pull <172 g> (rated on 10 mm horizontal steel). Account for vertical mounting,
thin steel and the air gap. Show a front view with a colour gradient for steel depth and flatness, and mark where
a magnet keeps full contact. Show where you place each magnet; I will mark where I would put them and you explain why not.
Pockets must be square to the local steel, blind from the front and open only at the back.
```
Then test it for real: put loose magnets on the rims, photograph them and send the photo: *"This is the maximum I can place. Decide which to keep."*

## P4b · Clamp (non-magnetic frames)
```text
My frame is not magnetic. Design a perimeter clamp: hooks over the top rim, lips under the bottom rim and side tabs
on both lenses, so the clip grips from all sides. Start with <0.2> mm clearance per side, hooks <0.8> mm deep with filleted roots,
contact only on the frame (never the lens face), and room for <1> mm TPU/felt pads. Avoid nose pads and hinges.
Show section views at every grip point and tell me the print orientation that keeps layer lines across each hook.
```
More options and checks: `guide/NON_METAL_FRAMES.md`.

## P5 · Clip design
```text
Design the clip on the glasses model: outline flush with the frame, front window that keeps as much lens clear as possible,
film loaded from the back into a slot held by lips, <pockets / clamp> as agreed. Keep it symmetric if the frame is.
Report: mass, % of each lens clear, minimum wall, film loading clearance, and show renders from the front, the back
and from my eye position.
```

## P6 · Checks I can judge
```text
Run every check and show me the plot for each, with the number and the threshold:
fit (gap from clip back to frame), magnet seating or clamp contact, strength (worst removal case),
film loading (every intermediate state), view from the eye, face comfort (nose and cheeks), printability (thin walls, supports).
Then list what is NOT verified.
```
When something looks off: *"Why this <gap/thin line/step>? You kept it even though your analysis shows it."*

## P7 · Independent review by other models
```text
Give the model, my full request history and the rules to <2-3> other models. Each reviews through one lens:
(a) making and using the real part, (b) smoothness and print quality, (c) accuracy against my outlines.
Findings must cite a number, a file line or a render region. Verify each finding yourself and change the design
only if it is real and serves my goal. Other models never edit your files.
```

## P8 · Print setup
```text
What print orientation is best so the film slot has no steps and the hooks/pockets print cleanly? If you choose
upright rather than flat, explain why with the slicer preview. Keep supports out of the magnet pockets (support blockers).
Give me the slicer project and G-code for <printer>, 0.1 mm layers.
```

## P9 · Final audit before printing
```text
Before I print: is every check done (fit, smoothness, design, look, size)? List each with its number and plot.
Do not say "ready" unless every visible issue is fixed. Give me a dry-fit procedure to run before any glue.
```

---

### What made the difference (my habits)
- I asked **"are you sure?"** and expected a number, not reassurance.
- I sent **my own markups** on screenshots instead of describing problems in words.
- I brought **real-world tests**: magnets stuck on the rims, coins, grid paper, the magnet datasheet.
- I made every found defect a **permanent rule**, so it could not come back in a later version.
- I kept **every version**, so a rejected idea stayed on record with the reason it failed.
