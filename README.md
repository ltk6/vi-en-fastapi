# Vietnamese → English Translation API (FastAPI)

## 1. Thông tin sinh viên

* Họ tên: Lâm Tuấn Khanh
* MSSV: 24120337
* Trường: Đại học Khoa Học Tự Nhiên TP.HCM
* Khoa: Công Nghệ Thông Tin

## 2. Tên mô hình & liên kết Hugging Face

* Model: Helsinki-NLP/opus-mt-vi-en
* Link: https://huggingface.co/Helsinki-NLP/opus-mt-vi-en

## 3. Mô tả hệ thống

Hệ thống cung cấp API dịch văn bản từ tiếng Việt sang tiếng Anh sử dụng mô hình pretrained từ Hugging Face.

* Framework: FastAPI
* Endpoint chính: `/predict`
* Input: Văn bản tiếng Việt
* Output: Bản dịch tiếng Anh

## 4. Hướng dẫn cài đặt

### 4.1. Clone project

```bash
git clone https://github.com/ltk6/vi-en-fastapi
cd vi-en-fastapi
```

### 4.2. Cài đặt thư viện

```bash
python -m pip install -r requirements.txt
```

## 5. Hướng dẫn chạy chương trình

Chạy server bằng lệnh:

```bash
python -m uvicorn main:app --reload
```
Sau khi chạy:

* API docs: http://127.0.0.1:8000/docs
* Root endpoint: http://127.0.0.1:8000/

## 6. Hướng dẫn gọi API

### 6.1. Endpoint

```
POST /predict
```

### 6.2. Request

```json
{
  "text": "Thế giới, hãy tốt bụng với cô ấy."
}
```

### 6.3. Response

```json
{
  "input": "Thế giới, hãy tốt bụng với cô ấy.",
  "translation": "The world, be kind to her."
}
```


## 7. Video demo

* Link: https://drive.google.com/file/d/1ut0i4PloCtPoNdLEEhsmU9f73m0W26ml/view?usp=drive_link
