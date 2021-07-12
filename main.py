from flask import Flask
from flask import request, abort
from pyngrok import ngrok
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,TextSendMessage

import os

app = Flask(__name__, static_folder="images")

NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN')
CHANNEL_SECRET = os.environ.get("CHANNEL_SECRET")
CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")

ngrok.set_auth_token(NGROK_AUTH_TOKEN)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
ngrok_url = ngrok.connect(5000, bind_tls=True).public_url
line_bot_api.set_webhook_endpoint(f"{ngrok_url}/callback")


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message))


if __name__ == '__main__':
    app.run()
