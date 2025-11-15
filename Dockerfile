# Imagen base
FROM python:3.10-slim

# Carpeta de la app
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install fastapi uvicorn

# Exponer puerto
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "laboratoriofinal:app", "--host", "0.0.0.0", "--port", "8000"]
