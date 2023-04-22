from chalice import Chalice

app = Chalice(app_name='scheduled')


@app.schedule("cron(0 10 ? * * *)")
def scheduled(event):
    print("Executou com sucesso")
    return True
