#Imagen Base
From python:3.10-slim

#Crear el directorio de trabajo
WORKDIR /app

#Copiar los archivos del proyecto
COPY requirements.txt requirements.txt

#Instalar dependencias
RUN pip install  --no-cache-dir -r requirements.txt

COPY . .

#Exponer el puerto
EXPOSE 5000

#Comando para iniciar el servidor
CMD ["python","app.py"]
