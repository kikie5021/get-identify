FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN ls /app  # ตรวจสอบว่าโฟลเดอร์ app มีไฟล์อะไรบ้าง
RUN ls /app/app  # ตรวจสอบว่าโฟลเดอร์ app มีไฟล์อะไรบ้าง

CMD ["python", "app/views.py"]  # หรือไฟล์ที่เป็น entry point ของแอปพลิเคชันคุณ
