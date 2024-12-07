# 1. Base Image
FROM python:3.8-slim

# 2. Set Working Directory
WORKDIR /app

# 3. Menyalin file aplikasi ke dalam container
COPY . /app

# 4. Install dependensi yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose port untuk aplikasi
EXPOSE 5000

# 6. Instruksi untuk menjalankan aplikasi
CMD ["python", "app.py"]
