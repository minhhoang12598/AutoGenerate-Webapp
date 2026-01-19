import os
import tempfile
from .legacy.dimension_manu import get_dimension_points

def suggest_points(image_bytes: bytes):
    """
    Trả JSON kiểu:
      selected_points: {height:[p1,p2], width:[p3,p4], depth:[p5,p6]}
      text_positions:  {height:pt, width:pt, depth:pt}
    """
    with tempfile.TemporaryDirectory() as td:
        in_path = os.path.join(td, "in.jpg")
        with open(in_path, "wb") as f:
            f.write(image_bytes)

        # get_dimension_points đang trả:
        # start_v, end_v, start_h, end_h, start_diag, end_diag, text1_pos, text2_pos, text3_pos, temp_path :contentReference[oaicite:10]{index=10}
        start_v, end_v, start_h, end_h, start_diag, end_diag, t1, t2, t3, temp_path = get_dimension_points(in_path)

        # temp_path là ảnh tạm shrink trong code legacy, có thể xóa nếu cần
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass

        selected_points = {
            "height": [{"x": start_v[0], "y": start_v[1]}, {"x": end_v[0], "y": end_v[1]}],
            "width": [{"x": start_h[0], "y": start_h[1]}, {"x": end_h[0], "y": end_h[1]}],
            "depth": [{"x": start_diag[0], "y": start_diag[1]}, {"x": end_diag[0], "y": end_diag[1]}],
        }
        text_positions = {
            "height": {"x": t1[0], "y": t1[1]},
            "width": {"x": t2[0], "y": t2[1]},
            "depth": {"x": t3[0], "y": t3[1]},
        }

        return selected_points, text_positions
