class Tag(BaseModel):
    name = CharField()

class Product(BaseModel):
    name = CharField()
    tags = ManyToManyField(Student, backref='products')

TagProduct = Product.tags.get_through_model()


class Student(BaseModel):
    name = CharField()

class Course(BaseModel):
    name = CharField()
    students = ManyToManyField(Student, backref='courses')

StudentCourse = Course.students.get_through_model()