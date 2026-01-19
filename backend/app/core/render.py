import os
import tempfile
from .legacy.resize_img import shrink_and_pad_image
from .legacy.dimension_manu import detect_product_and_draw_bounds_manual

def render_manual(
    image_bytes: bytes,
    input_filename: str,
    selected_points: dict,
    text_positions: dict,
    text_values=None,        # {"height":"..", "width":"..", "depth":".."}
    excel_df=None,
    shrink_percent: int = 30,
    line_color=(96, 96, 96),
    text_color=(0, 0, 0),
    font_scale: float = 1.2,
    thickness: int = 5,
):
    with tempfile.TemporaryDirectory() as td:
        in_path = os.path.join(td, "in.jpg")
        temp_path = os.path.join(td, "temp.jpg")
        out_path = os.path.join(td, "out.jpg")

        with open(in_path, "wb") as f:
            f.write(image_bytes)

        shrink_and_pad_image(in_path, temp_path, shrink_percent=shrink_percent)

        # convert JSON -> list tuple giống legacy đang dùng :contentReference[oaicite:11]{index=11}
        pts = []
        for key in ["height", "width", "depth"]:
            p = selected_points[key]
            pts.append((p[0]["x"], p[0]["y"]))
            pts.append((p[1]["x"], p[1]["y"]))

        txt_pts = [
            (text_positions["height"]["x"], text_positions["height"]["y"]),
            (text_positions["width"]["x"], text_positions["width"]["y"]),
            (text_positions["depth"]["x"], text_positions["depth"]["y"]),
        ]

        if text_values is None:
            text_values = {"height": "(choose) cm", "width": "(choose) cm", "depth": "(choose) cm"}

        detect_product_and_draw_bounds_manual(
            temp_path,
            out_path,
            input_filename,
            excel_df,
            pts,
            text_positions=txt_pts,
            line_color=line_color,
            text_color=text_color,
            text1=text_values["height"],
            text2=text_values["width"],
            text3=text_values["depth"],
            font_scale=font_scale,
            thickness=thickness,
        )

        with open(out_path, "rb") as f:
            return f.read()
