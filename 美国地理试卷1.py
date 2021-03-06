import random,os
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
#Generate 35 quiz files
for quizNum in range(35):
#TODO: Create the quiz and answer key files.
    quizfile=open("capitalquz%s.txt"%(quizNum+1), 'w')
    answerfile=open("capitalanswer%s.txt"%(quizNum+1), 'w')
#TODO: Write out the header for the quiz.
    quizfile.write('Name:\nDate:\nPeriod:\n')
    quizfile.write((' '*20)+'States Captical Quiz(Form %s)'%(quizNum+1))
    quizfile.write('\n\n')
#TODO: Shuffle the order of the states
    states=list(capitals.keys())
    random.shuffle(states)
#TODO: Loop through all 50 states,making a question for each.
    for quesNum in range(50):
#TODO: Get right and wrong answers
        correctAnswer=capitals[states[quesNum]]#这个还是词典
        wrongAnswer=list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]#删除value中correct answer的序号
        wrongAnswer=random.sample(wrongAnswer,3)#在wronganswer中随机挑选三个样本作为错误选项
        answerOptions=wrongAnswer+[correctAnswer]#不能用list[correctAnswer],因为correctAnswer在每一次循环中是一个字符串，会变成一个一个字符
        random.shuffle(answerOptions)
#TODO:Write the question and answer options to the quiz file
        quizfile.write("%s.What's the capital of %s?\n"%(quesNum+1,states[quesNum]))
        for i in range(4):
            quizfile.write('%s. %s\n'%('ABCD'[i],answerOptions[i]))
            quizfile.write('\n')
#TODO: Write the answer key to the file
        answerfile.write('%s. %s\n'%(quesNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
quizfile.close()
answerfile.close()