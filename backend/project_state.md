
# PROJECT_STATE.md

## Project: AutoGenerate Web App (Python → Web App)
Mục tiêu: Chuyển ứng dụng Python desktop (Tkinter) sang mô hình **Web App + Server**  
Mục đích học tập: GitHub, backend, frontend, web architecture cho người mới.

---

## 1. Tổng quan kiến trúc (hiện tại)

- Backend: Python + FastAPI (đang chuẩn bị triển khai)
- Core xử lý ảnh: OpenCV (cv2), numpy
- Frontend: Chưa triển khai
- Lưu trữ: Local disk (server)
- GUI desktop (Tkinter): **Đã loại bỏ khỏi flow chính**

---

## 2. Trạng thái các bước theo kế hoạch

### ✅ Bước 0 — Chốt mục tiêu
- Chỉ giữ TAB 1 (Auto) và TAB 2 (Manual)
- TAB 3 / TAB 4: bỏ
- Flow:
  Upload ảnh → Auto generate → Thumbnail grid → Manual chỉnh → Render lại → Export

**Trạng thái:** HOÀN THÀNH

---

### ✅ Bước 1 — Tách core xử lý ảnh khỏi GUI
Đã tách toàn bộ logic xử lý ảnh ra khỏi Tkinter.

#### Core modules hiện có:
```

backend/app/core/
├── auto.py        # Auto generate (TAB 1)
├── suggest.py     # Gợi ý điểm (TAB 2)
├── render.py      # Render manual theo điểm user
├── io.py          # Encode / decode ảnh bytes ↔ cv2
├── types.py       # Chuẩn hoá dữ liệu points/text
└── legacy/        # Code cũ giữ nguyên để tái sử dụng
├── resize_img.py
├── dimension_gen.py
└── dimension_manu.py

````

**Nguyên tắc đã đạt được:**
- Core KHÔNG import Tkinter
- Core không dùng file dialog, không cv2.imshow
- Input/Output: bytes + JSON

**Trạng thái:** HOÀN THÀNH

---

### ✅ Bước 2 — Thiết kế format dữ liệu points/text (JSON)
Đã chuẩn hoá format dữ liệu cho frontend ↔ backend:

```json
selected_points: {
  "height": [{"x":..,"y":..},{"x":..,"y":..}],
  "width":  [{"x":..,"y":..},{"x":..,"y":..}],
  "depth":  [{"x":..,"y":..},{"x":..,"y":..}]
}

text_positions: {
  "height": {"x":..,"y":..},
  "width":  {"x":..,"y":..},
  "depth":  {"x":..,"y":..}
}
````

* Được định nghĩa trong `types.py`
* Được sử dụng trong `suggest.py` và `render.py`

**Trạng thái:** HOÀN THÀNH

---

### ⏳ Bước 3 — Backend API (FastAPI) theo mô hình Job

* Chưa triển khai endpoint `/jobs`
* Chưa có BackgroundTasks / worker
* Chưa có storage job structure

**Trạng thái:** CHƯA BẮT ĐẦU

---

### ⏳ Bước 4 — Manual endpoints (TAB 2 web)

* Core đã sẵn sàng (`suggest.py`, `render.py`)
* Chưa expose qua FastAPI endpoint

**Trạng thái:** CHƯA BẮT ĐẦU (core đã xong)

---

### ⏳ Bước 5 — Export kết quả

* Chưa triển khai zip export

**Trạng thái:** CHƯA BẮT ĐẦU

---

### ⏳ Bước 6 — Frontend Web (Grid + Editor)

* Chưa triển khai
* Chưa chọn framework (React/Canvas)

**Trạng thái:** CHƯA BẮT ĐẦU

---

### ⏳ Bước 7 — Thứ tự triển khai MVP

* Đang follow đúng roadmap
* Đã hoàn thành phần core trước backend

**Trạng thái:** ĐANG THEO ĐÚNG HƯỚNG

---

### ✅ Bước 8 — Git commit (local)

* Đã init git repository
* Đã commit toàn bộ core + structure
* Đã chuẩn hoá `.gitignore`

**Trạng thái:** HOÀN THÀNH

---

### ✅ Bước 9 — Push lên GitHub

* Repo: `minhhoang12598/AutoGenerate-Webapp`
* Đã xử lý xong vấn đề account / credential
* Đã push thành công

**Trạng thái:** HOÀN THÀNH

---

## 3. Tình trạng môi trường

* Python venv: `.venv` (backend/)
* OpenCV: `opencv-python` (đã cài đúng)
* VS Code interpreter: trỏ đúng `.venv`
* Git user: `minhhoang12598`

---

## 4. Những quyết định kiến trúc đã chốt

* Truyền ảnh qua HTTP bằng **bytes**
* Truyền dữ liệu chỉnh sửa bằng **JSON**
* Core xử lý ảnh độc lập với web framework
* Lưu file local disk (chưa dùng cloud / DB)
* MVP ưu tiên chạy được, tối ưu sau

---

## 5. Điểm bắt đầu tiếp theo (CHAT MỚI)

👉 **Bước kế tiếp nên làm:**

### 🔜 Bước 3.1

* Dựng FastAPI app tối thiểu
* Endpoint test: `/health`, `/auto-generate` (1 ảnh)

---

## 6. Ghi chú quan trọng

* Không cần quay lại Bước 1–2
* Core hiện tại đủ dùng cho backend + frontend
* Mọi thay đổi tiếp theo chỉ nên nằm ở API / UI

---

**Last updated:** *(điền ngày khi commit)*
**Status:** Core ready → Backend API pending

````

---

### ✅ Việc bạn nên làm ngay
1. Tạo file `PROJECT_STATE.md` ở root repo  
2. Paste nội dung trên  
3. Commit:

```bash
git add PROJECT_STATE.md
git commit -m "Add project state documentation (up to step 9)"
git push
````

---

Khi bạn mở **chat mới**, chỉ cần nói:

> *“Dựa trên PROJECT_STATE.md, tiếp tục Bước 3: FastAPI backend.”*

Mình sẽ tiếp đúng **tại điểm đó**, không lặp lại.
