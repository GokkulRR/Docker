class AppConstant:
    get_welcome = "/"
    post_create_application_id = "/course"
    get_display_all = "/get_all"
    get_particular_detail = "/particular_detail"
    put_update_application = "/update_course/{application_id}"
    del_delete_application = "/delete_course/{application_id}"
    post_send_email = "/send_email"
    get_total_price = "/total_price"


class Mongo:
    mongo_db = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
