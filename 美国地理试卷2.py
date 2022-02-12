import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#TODO：建立35份文件
for quizNum in range(35):
    quizfile=open("test%s.txt"%(quizNum+1),'w')
    answerfile=open("answer%s.txt"%(quizNum+1),'w')
#TODO:写入每份文件的开头
    quizfile.write("Name:\nGrade:\n")
    quizfile.write((' '*20)+"States Test(Form %s)\n"%(quizNum+1))
#TODO:打乱美国各州的顺序
    state=list(capitals.keys())
    random.shuffle(state)
#TODO:组织正确答案
    for quesNum in range(50):
        correctAnswer=capitals[state[quesNum]]
#TODO:组织错误答案
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
#TODO:整合答案
        fullAnswer=wrongAnswer+[correctAnswer]
        random.shuffle(fullAnswer)
#TODO:写入题目
        quizfile.write("%s.What's the capital of %s?\n"%(quesNum+1,state[quesNum]))
#TODO:写入ABCD与选项
        for i in range(4):
            quizfile.write("%s.%s\n"%('ABCD'[i],fullAnswer[i]))
#TODO:组织答案
        answerfile.write("%s.%s\n"%(quesNum+1,'ABCD'[fullAnswer.index(correctAnswer)]))
quizfile.close()
answerfile.close()