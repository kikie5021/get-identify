FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./app/views.py"]  # หรือไฟล์ที่เป็น entry point ของแอปพลิเคชันคุณ
