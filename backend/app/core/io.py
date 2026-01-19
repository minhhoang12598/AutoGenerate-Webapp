import cv2
import numpy as np
# qua https , code chỉ nhận ảnh dưới dạng BYTES
# hiện tại OpenCV trong code legacy(python app) chỉ hỗ trợ đọc ảnh từ file path hoặc từ numpy array
# nên cần hàm chuyển đổi từ bytes sang numpy array để xử lý ảnh


def decode_image_bytes(image_bytes: bytes):
    arr = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Cannot decode image bytes")
    return img

def encode_jpg(img, quality: int = 95) -> bytes:
    ok, buf = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    if not ok:
        raise ValueError("Cannot encode jpg")
    return buf.tobytes()

def encode_png(img) -> bytes:
    ok, buf = cv2.imencode(".png", img)
    if not ok:
        raise ValueError("Cannot encode png")
    return buf.tobytes()
