# from celery_tasks import add

# def main():
#     r = add.delay(4, 4)
#     print(r.get())

from celery import Celery

def main():
    app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="rpc://")
    r = app.send_task('celery_tasks.add',args=(3,2))
    print(r.get())
if __name__ == '__main__':
    main()
