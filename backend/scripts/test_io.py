from pathlib import Path
from app.core.io import decode_image_bytes, encode_png

p = Path("samples/test1.jpg")
print("inp exists:", p.exists())

b = p.read_bytes() #file ảnh -> bytes (thuộc pathlib.Path)
                   # mô phỏng ảnh upload lên web 
print("read", len(b), "bytes")

img = decode_image_bytes(b) # bytes -> numpy array (OpenCV image) và xử lý ở backend


out = encode_png(img) # numpy array (OpenCV image) -> bytes (PNG) -> trả về cho frontend

Path("out/io_roundtrip.png").write_bytes(out)
print("OK: wrote out/io_roundtrip.png")


# test vòng bytes -> OpenCV -> bytes