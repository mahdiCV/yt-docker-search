FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install sentence-transformers

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]   