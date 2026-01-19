import os
import tempfile
from .io import encode_jpg
from .legacy.resize_img import shrink_and_pad_image
from .legacy.dimension_gen import detect_product_and_draw_bounds

def auto_generate(
    image_bytes: bytes,
    input_filename: str,
    excel_df=None,
    shrink_percent: int = 30,
    line_color=(96, 96, 96),
    text_color=(0, 0, 0),
    font_scale: float = 1.2,
    thickness: int = 5,
):
    """
    - Nhận ảnh (bytes)
    - Ghi ra file tạm
    - Chạy shrink_and_pad_image + detect_product_and_draw_bounds
    - Đọc kết quả và trả về bytes
    """

    with tempfile.TemporaryDirectory() as td:
        in_path = os.path.join(td, "in.jpg")
        temp_path = os.path.join(td, "temp.jpg")
        out_path = os.path.join(td, "out.jpg")

        with open(in_path, "wb") as f:
            f.write(image_bytes)

        # Logic đang dùng trong app cũ:
        # - shrink_and_pad_image :contentReference[oaicite:6]{index=6}
        # - detect_product_and_draw_bounds :contentReference[oaicite:7]{index=7}
        shrink_and_pad_image(in_path, temp_path, shrink_percent=shrink_percent)
        detect_product_and_draw_bounds(
            temp_path,
            out_path,
            excel_df,
            input_filename,
            line_color,
            text_color,
            font_scale=font_scale,
            thickness=thickness,
        )

        with open(out_path, "rb") as f:
            return f.read()
