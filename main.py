from flask import Flask, request
from data import GetcourseData
import requests
import datetime

token = TOKEN
app = Flask(__name__)


@app.route('/')
def getcourse():

    data = GetcourseData(request.args.get('payment'), request.args.get('order_id'))
    payment = data.order_payment
    order = 'Заказ с Геткурс # '+ data.order_id

    p = ''.join(x for x in payment if x.isdigit())
    d = datetime.date.today()

    url = 'https://api.planfact.io/api/v1/operations/income'
    payload = {'operationDate': d, 'accountId': '93386', 'value': float(p), 'comment': order}
    headers = {'X-ApiKey': token}
    if p > str(0):
        r = requests.post(url, headers=headers, data=payload)
    return 'OK'

if __name__ == '__main__':
    app.run(host='localhost')
