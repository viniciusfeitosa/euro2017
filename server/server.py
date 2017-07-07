import datetime
import time
from japronto import Application


def main(request):
    time.sleep(1)
    return request.Response(json={
        "name": "Vinicius Pacheco",
        "consulted_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    })


app = Application()
app.router.add_route('/', main)
app.run(worker_num=10, port=5001)
