"""Copy and downscale the figures the report uses from the private design workspace (SRC = blender_ai/frame)."""
import sys, os
from PIL import Image, ImageChops, ImageOps
SRC, OUT = sys.argv[1], "report/figures"
A = "FINAL_v15/analysis/"
PICK = {
 "photo_front.jpg": "overview/img/01_glasses_front.jpg", "photo_side.jpg": "overview/img/01_glasses_side.jpg",
 "photo_top.jpg": "overview/img/01_glasses_top.jpg", "photo_film_coin.jpg": "overview/img/03_film_sheets_coin.jpg",
 "model_vs_bezier.png": "overview/img/02_model_top_vs_bezier.png", "photo_vs_model.png": A+"01_shape_and_size/photo_1_photo_vs_model_v15.png",
 "grid_fit.png": A+"01_shape_and_size/size_grid_fit_2026-10-21.png", "fit_overlay_tele.png": A+"01_shape_and_size/size_fit_overlay_tele.png",
 "symmetry.png": A+"01_shape_and_size/symmetry_check_v15_1.png", "layout.png": A+"01_shape_and_size/v15_1_layout.png",
 "gap.png": A+"02_fit_and_contact/v15_1_gap.png", "steel_depth.png": A+"03_magnets/steel_depth_v15_1.png",
 "steel_flat.png": A+"03_magnets/steel_flatness_v15_1.png", "magnet_spots.png": A+"03_magnets/magnet_spots_v15_1.png",
 "pull.png": A+"03_magnets/pull_per_magnet_v15_1.png", "pockets.png": A+"03_magnets/v15_1_pocket_sections.png",
 "stress.png": A+"04_strength/v15_1_stress.png", "thickness.png": A+"04_strength/v15_1_thickness.png",
 "film_vs_lens.png": A+"05_film/film_vs_lens_v15_1.png", "film_loading.png": A+"05_film/v15_1_film_loading.png",
 "loading_sweep.png": A+"05_film/v15_1_loading_sweep.png", "slot_sections.png": A+"05_film/v15_1_slot_sections.png",
 "face_3q.png": A+"06_view_and_comfort/comfort_v15_1/face_v15_typical_below_3q.png",
 "face_front.png": A+"06_view_and_comfort/comfort_v15_1/face_v15_typical_front.png",
 "comfort_check.png": A+"06_view_and_comfort/comfort_v15_1/comfort_check.png",
 "eye_view.png": A+"06_view_and_comfort/v15_1_render_eye_both.png",
 "render_3q.png": A+"08_renders/v15_1_render_3q.png", "render_back.png": A+"08_renders/v15_1_render_back.png",
 "render_back_bridge.png": A+"08_renders/v15_1_render_back_bridge.png", "render_xray.png": A+"08_renders/v15_1_render_xray.png",
 "render_front.png": A+"08_renders/v15_1_render_front.png", "gcode.png": A+"07_print/gcode_preview_v15_1.png",
 "cura.jpg": "overview/img/06_cura_preview_v14_same_recipe.jpg", "template.png": "overview/img/film_template_page.png",
 "magnet_pockets_back.png": "FINAL_v15/magnet_pockets_back.png", "stl_quality.png": A+"07_print/v15_1_stl_quality.png",
}
EVO = [("v01","archive/clipon_v2_superseded/full/clipon_v2_full_render_front.png"),("v02","archive/clipon_v2_superseded/cut/clipon_v2_cut_render_front.png"),
 ("v03","archive/clipon_v2_superseded/flush/clipon_v2_flush_render_front.png"),("v04","archive/clipon_v2_superseded/flush_4x1/clipon_v2_flush_4x1_render_front.png"),
 ("v05","archive/clipon_v2_superseded/wide_4x1/clipon_v2_wide_4x1_render_front.png"),("v06","archive/clipon_v2_superseded/strong_4x1/clipon_v2_strong_4x1_render_front.png"),
 ("v07","archive/clipon_v2_superseded/strong2_4x1/clipon_v2_strong2_4x1_render_front.png"),("v08","clipon_v2/aligned_4x1/clipon_v2_aligned_4x1_render_front.png"),
 ("v09","clipon_v2/polished_4x1/clipon_v2_polished_4x1_render_front.png"),("v10","clipon_v2/backload_4x1/clipon_v2_backload_4x1_render_front.png"),
 ("v11","clipon_v2/refined_4x1/clipon_v2_refined_4x1_render_front.png"),("v12","clipon_v2/symmetric_4x1/clipon_v2_symmetric_4x1_render_front.png"),
 ("v13","clipon_v2/symmetric_6x1/clipon_v2_symmetric_6x1_render_front.png"),("v14","clipon_v2/faired_6x1/clipon_v2_faired_6x1_render_front.png"),
 ("v15","clipon_v2/v15_scaled/clipon_v2_v15_scaled_render_front.png"),("v15.1","clipon_v2/v15_1_smooth/clipon_v2_v15_1_smooth_render_front.png")]
os.makedirs(OUT, exist_ok=True); os.makedirs(OUT+"/evo", exist_ok=True)
def save(src, dst, w=2000):
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((2, 2)))           # trim the uniform margin plots carry
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 18 else 0).getbbox()
    if box: im = im.crop((max(box[0] - 8, 0), max(box[1] - 8, 0), min(box[2] + 8, im.width), min(box[3] + 8, im.height)))
    if "markup" in dst: im = ImageOps.autocontrast(im, cutoff=1)
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    dst = os.path.splitext(dst)[0] + ".jpg"
    im.save(dst, quality=88, optimize=True)
for k, v in PICK.items(): save(v, f"{OUT}/{k}")

print("ok")
EXTRA = {"markup_hole": "clipon_v2/aligned_4x1/user_markup_2026-10-03_060546.png", "markup_bevel": "clipon_v2/aligned_4x1/user_markup_2026-10-03_061622.png",
         "markup_gap": "clipon_v2/aligned_4x1/user_markup_2026-10-03_042230.png",
         "six_magnet_proposal": "clipon_v2/symmetric_4x1/clipon_v2_symmetric_4x1_magnet_layout_6_PROPOSAL.png",
         "film_measured": "clipon_v2/reference/IMG_7905_measured.jpg", "gap_before_after": "clipon_v2/aligned_4x1/clipon_v2_aligned_4x1_gap_before_after.png"}
for k, v in EXTRA.items(): save(v, f"{OUT}/{k}")
