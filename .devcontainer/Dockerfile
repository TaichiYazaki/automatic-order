FROM python:latest

WORKDIR /usr/src/automatic-order

# pipの更新
RUN pip install --upgrade pip          
# python libraryのリストをホストから取得      
COPY ./requirements.txt /tmp/requirements.txt
# requirements.txt内のライブラリーを一括インストール
RUN pip install -r /tmp/requirements.txt