FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# ตรวจสอบไฟล์ใน /app
RUN ls -la /app

# ตรวจสอบไฟล์ใน /app/app
RUN ls -la /app/app

# ตั้งค่า PYTHONPATH
ENV PYTHONPATH=/app

CMD ["python", "app/views.py"]
