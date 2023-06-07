from fastapi import APIRouter
from schemas.models import Name, Email
from scripts.core.handlers.access import get_input, select_course, get_all, get_particular_detail, update_course, delete_course, pipeline_agg
from scripts.core.handlers.email_handler import send_email
from scripts.constants.app_constants import AppConstant

app = APIRouter()


@app.get(AppConstant.get_welcome)
def fun():
    return get_input()


@app.post(AppConstant.post_create_application_id)
def fun(request: Name):
    return select_course(request)


@app.get(AppConstant.get_display_all)
def fun():
    return get_all()

@app.get(AppConstant.get_particular_detail)
def fun(application_id: int):
    return get_particular_detail(application_id)



@app.put(AppConstant.put_update_application)
def fun(application_id: int, up_course: Name):
    return update_course(application_id, up_course)


@app.delete(AppConstant.del_delete_application)
def fun(application_id: int):
    return delete_course(application_id)


@app.post(AppConstant.post_send_email)
def fun(email: Email):
    total_value = pipeline_agg()
    return send_email(str(total_value), email)


@app.get(AppConstant.get_total_price)
def fun():
    return pipeline_agg()
