FROM python:3.10
# EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["/bin/bash", "docker-entrypoint.sh"]