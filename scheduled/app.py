from chalice import Chalice

app = Chalice(app_name='scheduled')


@app.schedule("cron()")
def first_function(event, context):
    return {'hello': 'world'}


