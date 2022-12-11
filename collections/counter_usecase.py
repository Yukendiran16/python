from collections import Counter

student_list = []


class Student:
    def __init__(self, name="name", t_mark=0, e_mark=0, m_mark=0, s_mark=0):
        self.name = name
        self.t_mark = t_mark
        self.e_mark = e_mark
        self.m_mark = m_mark
        self.s_mark = s_mark
        self.grade = self.calculate_grade()
        student_list.append(self)

    def calculate_grade(self):
        """
        This is the function to calculate grade for the student using whose marks
        :return: grade for the student
        """
        total = self.t_mark + self.e_mark + self.m_mark + self.s_mark
        if 350 < total <= 400:
            return "A"
        elif 300 < total <= 350:
            return "B"
        elif 250< total <= 300:
            return "C"
        elif 200 < total <= 250:
            return "D"
        else:
            return "Fail"

    @staticmethod
    def exam_result():
        """
        This function to prepare exam result using counter
        :return: counter {grade: student count}
        """
        return Counter(i.grade for i in student_list)


Student("yuki", 95, 93, 85, 92)
Student("yuki", 85, 63, 95, 82)
Student("yuki", 75, 73, 75, 72)
Student("yuki", 95, 93, 75, 42)
Student("yuki", 65, 63, 95, 92)
Student("yuki", 85, 73, 65, 52)
Student("yuki", 75, 43, 96, 72)
Student("yuki", 45, 43, 45, 42)
Student("yuki", 35, 33, 35, 32)
Student("yuki", 55, 53, 55, 52)
print(Student.exam_result())
