def QuestionsMarks(strParam):
    numbers = '0123456789'
    my_list = []
    for i in strParam:
        if i == '?' or i in numbers:
            my_list.append(i)
    true_check = False
    question_count = 0
    value = 0
    for i in my_list:
        try:
            value += int(i)
        except ValueError:
            pass
        if i == '?':
            question_count += 1
        if question_count >= 3 and value == 10:
            true_check = True
            question_count = 0
            value = int(i)
        elif value >= 10:
            true_check = False
            question_count = 0
            value = 0

  # code goes here
    return 'true' if true_check else 'false'


print(QuestionsMarks("arrb6???4xxbl5???eee5"))
