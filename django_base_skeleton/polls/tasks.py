from celery.task import Task
from celery.registry import tasks

class MyTask(Task):
  def run(self, some_arg, **kwargs):
    logger = self.get_logger(**kwargs)
    logger.info("Did something: %s" % some_arg)

tasks.register(MyTask)
