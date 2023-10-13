## 事前準備

```
$ cp .env.example .env
$ pip install -r requirements.txt
```

headless-chromium
```
$ curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
$ unzip headless-chromium.zip
$ rm headless-chromium.zip
```

chromedriver
```
$ curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip
$ unzip chromedriver.zip
$ rm chromedriver.zip
```

デプロイ
```
$ gcloud functions deploy [FUNCTION_NAME] --gen2 --region=[FUNCTION_REGION] --runtime=[RUNTIME] --trigger-http --entry-point=[YOUR_CODE_ENTRYPOINT] --source=.
$ gcloud functions deploy my-function --gen2 --region asia-northeast1 --runtime python311 --trigger-topic=test --memory 512MiB --entry-point=handler
```

Cloud Functions
https://console.cloud.google.com/functions/list