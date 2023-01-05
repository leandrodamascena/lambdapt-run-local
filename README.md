pip install -r requirements.txt

python app.py


## Expected output
```{"level":"ERROR","location":"log_uncaught_exception_hook:760","message":"This will create a structured log","timestamp":"2023-01-05 12:40:15,958+0000","service":"service_undefined","exception":"Traceback (most recent call last):\n  File \"/home/leandro/DEVEL-PYTHON/tmp/lambda-eng/local-project/app.py\", line 7, in <module>\n    raise(Exception(\"This will create a structured log\"))\nException: This will create a structured log","exception_name":"Exception"}```
