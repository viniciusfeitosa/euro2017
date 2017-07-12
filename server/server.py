import datetime
import time
from japronto import Application


def main(request):
    time.sleep(1)
    return request.Response(json={
        "Name": "Vinicius Pacheco",
        "ConsultedAt": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    })


app = Application()
app.router.add_route('/', main)
app.run(worker_num=20, port=5001)
