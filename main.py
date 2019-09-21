from flask import Flask, request
from data import GetcourseData
import requests
import datetime

token = 'CPZ0mPm9K6bGKS_7o8URxf5I5Cj5kstRvyILLfl9WROVFI9m-bjV1DMOpI7YV1h3ecoOGVj2qk56jAKRz2i1PI1SP46IY5XhDqIml171tgOWH4O-gsRvgRXKd6-bfIBFPU1wq-y33RdeLOwTL6HaRsjQimPCplQpkPfMwtmXbEz3r6Sfb08dOeTdVgwraWheFPrFRMAYQBQpPaQOUhvzSv1HSC09srFRd6VvRCVSjyug86qlhVoRPCYI4g25WzcmUwoiZPqPRolm38BkLsY-_pEJ65dUXcn6XmrjVVOTp9Cv5qA2yV8kGLqnk96hw9ObWHTp5GwXsjIkQRaXuqoFxSNXkbDWBTTUQNYy8LksX5M8-3rmcvI56PCFErOgrGuQYRiBQKNF0BWlc5sPYQv-hrbRst-kMzbh_tnxaqbXVu5ZFqOMxY0db1cLru_CxvLUbQxq6bVyKRP1NBMQT5NVfD4K6yuaIgsRtpjattc56IxsYqLewDE7HvpnAxxk8q4WlCkYUpJJj2ER5bbkzAcExNbqKxBY4Ha5ZJXCOEi5S6hiBQje'

app = Flask(__name__)


@app.route('/')
def getcourse():

    data = GetcourseData(request.args.get('payment'), request.args.get('order_id'))
    payment = data.order_payment
    order = 'Заказ с Геткурс # '+ data.order_id

    print(payment)
    p = ''.join(x for x in payment if x.isdigit())
    print(p)
    print(order)
    d = datetime.date.today()
    print(d)

    url = 'https://api.planfact.io/api/v1/operations/income'
    payload = {'operationDate': d, 'accountId': '93386', 'value': float(p), 'comment': order}
    headers = {'X-ApiKey': token}
    if p > str(0):
        r = requests.post(url, headers=headers, data=payload)


    return 'hi'

if __name__ == '__main__':
    app.run(host='localhost')
