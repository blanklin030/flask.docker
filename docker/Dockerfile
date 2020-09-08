FROM python:3.8
COPY requirements.txt /root/
RUN pip install -r /root/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]