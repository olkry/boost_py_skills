class Student:
    def __init__(self, student_id, full_name, course=1, gpa=0.0):
        self.student_id = student_id
        self.full_name = full_name
        self.course = course
        self.gpa = gpa

    def promote(self):
        self.course += 1
        return f'Студент {self.full_name} переведен на {self.course} курс'

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        return f'Средний балл обновлен: {self.gpa}'

    def get_info(self):
        return (f'Студент: {self.full_name}, Курс: {self.course}, '
                f'Средний балл: {self.gpa}')

    def is_excellent(self):
        return True if self.gpa >= 4.5 else False


# Тестирование
student1 = Student("2024001",
                   "Петров Алексей Иванович",
                   2,
                   4.3)
student2 = Student("2024002",
                   "Сидорова Мария Петровна",
                   1,
                   4.7)

print(student1.get_info())
print(student2.get_info())

print(student1.promote())
print(student1.update_gpa(4.6))

print(f"Является отличником: {student1.is_excellent()}")
print(f"Является отличником: {student2.is_excellent()}")