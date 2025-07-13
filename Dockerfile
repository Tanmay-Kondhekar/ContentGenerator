# base image
FROM python:latest

# working dir
WORKDIR /app

# copy req 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of app
COPY . .

# expose ports
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]