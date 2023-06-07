from schemas.models import Name
from scripts.utility.mongodb_client import course_list


def get_input():
    return {"Welcome message": "Welcome to Course Registering Platform!"}


def select_course(request: Name):
    try:
        if list(course_list.find({"application_id": request.application_id})) != []:
            return {'message': "Application Number Already Registered"}
        else:
            course_list.insert_one(request.dict())
            return {"message": "Application is created Successfully"}
    except Exception as err:
        return "error", str(err)


def get_all():
    course = course_list.find({})
    new_course = []
    for student in course:
        detail = {'application_id': student['application_id'], 'Student_Name': student['Student_Name'],
                  'Course_Name': student['Course_Name'], 'Enroll_Month': student['Enroll_Month'],
                  'Duration': student['Duration'], 'Price': student['Price']}
        new_course.append(detail)
    return {"details": new_course}


def get_particular_detail(application_id: int):
    course = course_list.find({})
    new_course = []
    for student in course:
        if student['application_id'] == application_id:
            detail = {'application_id': student['application_id'], 'Student_Name': student['Student_Name'],
                      'Course_Name': student['Course_Name'], 'Enroll_Month': student['Enroll_Month'],
                      'Duration': student['Duration'], 'Price': student['Price']}
            new_course.append(detail)
        return new_course


def update_course(application_id: int, up_course: Name):
    try:
        course_list.update_one({"application_id": application_id}, {"$set": up_course.dict()})
        return {"message": "Application is Updated Successfully"}

    except Exception as err:
        return "error", str(err)


def delete_course(application_id: int):
    try:
        course_list.delete_one({"application_id": application_id})
        return {"message": "Application is Deleted Successfully"}
    except Exception as err:
        return "error", str(err)


def pipeline_agg():
    pipeline = [
        {
            '$group': {
                '_id': 0,
                'Total': {
                    '$sum': '$Price'
                }
            }
        },
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = course_list.aggregate(pipeline)
    data = list(data)
    print(data)
    return {"total prices": (data)[0]['Total']}
