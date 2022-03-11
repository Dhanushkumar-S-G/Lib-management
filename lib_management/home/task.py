from celery import shared_task


@shared_task(bind=True)