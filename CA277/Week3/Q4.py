class Test(object):
    def __init__(self, subject_name, correct_answers, passing_mark):
        self.subject_name = subject_name
        self.correct_answers = correct_answers
        self.passing_mark = passing_mark


class Student(object):
    def __init__(self, name):
        self.name = name

    def take_test(self, paper, answers):
        correct = 0
        a = len(answers)
        for i in range(a):
            if answers[i] == paper.correct_answers[i]:
                correct += 1
        score = correct / a

        b = paper.passing_mark[:-1]
        pass_score = int(b) / 100
        s = (str(score * 100) + '%')
        subject = paper.subject_name
        if score >= pass_score:
            return f'{self.name} passed the {subject} test with the score with the score {s}'
        else:
            return f'{self.name} failed the {subject} test!'


paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')


stu1 = Student('Tom')
stu1.take_test(paper2, ['1C', '2C', '3D', '4A'])  # Tom passed the Chemistry test with the score 100.0%
print(stu1.take_test(paper2, ['1C', '2C', '3D', '4A']))

stu2 = Student('John')
stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B'])  # John failed the Maths test!
print(stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B']))



