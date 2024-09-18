# Usa una imagen base de Python
FROM python:3.9-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que la app corre (5000 en este ejemplo)
EXPOSE 5000

# Comando para ejecutar la aplicación (ajusta según tu aplicación)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
