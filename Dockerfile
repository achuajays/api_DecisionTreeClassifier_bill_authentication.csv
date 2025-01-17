FROM python:3.9
WORKDIR /app
ADD . .
EXPOSE 8000
RUN pip install -r requirments.txt
CMD ["uvicorn","main:app","--host", "0.0.0.0", "--port", "8000"]
