from pathlib import Path
from app.core.legacy.resize_img import shrink_and_pad_image
from app.core.legacy.dimension_gen import detect_product_and_draw_bounds

inp = "samples/test1.jpg"
tmp = "out/tmp_shrink.jpg"
outp = "out/legacy_auto.jpg"

print("inp exists:", Path(inp).exists())


shrink_and_pad_image(inp, tmp, shrink_percent=30)
print("tmp exists:", Path(tmp).exists()) 

detect_product_and_draw_bounds(
    tmp,
    outp,
    data_excel=None,
    input_filename="ABCDEF_test.jpg",  # 6 ký tự đầu là product_code
)
print("outp exists:", Path(outp).exists())


print("OK: wrote", outp)
