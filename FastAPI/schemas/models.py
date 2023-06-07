from pydantic import BaseModel


class Name(BaseModel):
    application_id: int
    Student_Name: str
    Course_Name: str
    Enroll_Month: str
    Duration: str
    Price: int


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str
