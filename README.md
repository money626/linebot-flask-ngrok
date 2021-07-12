# Line Chatbot Easy Development Setup

A basic line chatbot that echoes what users say. Uses Flask as backend and ngrok to quickly setup linebot.

## Setup

1. Clone this repository.

      ```shell
      git clone https://github.com/money626/linebot-flask-ngrok
      ```

2. Rename(or copy) .env.example to .env and fill your own value

2. Setup environment
    * Using Docker

        1. Build image run 
           ```shell
           docker build . -t <image-tag>
           ```
        2. Run container
           ```shell
           docker run --rm -it -d --env-file ./.env <image-tag>
           ```

    * Using docker-compose

        1. Run service
           ```shell
           docker-compose up -d
           ```

    * Using local environment

        1. Create virtualenv and activate it
           ```shell
           python -m venv <venv-name>
           . <venv-name>/Scripts/activate
           # .\<venv-name>\Scripts\activate for Windows users
           # or using conda 
           conda create -n <venv-name>
           conda activate <venv-name>
           ```
        2. Install dependencies
           ```shell
           pip install -r requirements.txt
           ```
        3. Run the server
           ```shell
           python main.py
           ```
    