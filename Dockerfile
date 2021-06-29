FROM mcr.microsoft.com/playwright:latest
COPY . .
RUN apt install -y python3-pip && pip3 install -r requirements.txt
ENV CHAT_ID $CHAT_ID
ENV BOT_TOKEN $BOT_TOKEN
CMD [ "python3", "main.py"]