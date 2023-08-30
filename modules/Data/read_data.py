import json

def read_file(file_path):
        
    contexts = []
    questions = []
    answers = []

    with open(file_path, 'r') as f:
        data = json.load(f)
    for group in data['data']:
        for passage in group['paragraphs']:
          context = passage['context']
          for qa in passage['qas']:
            question = qa['question']
            for answer in qa['answers']:
              contexts.append(context)
              questions.append(question)
              answers.append(answer)
                    
    return contexts, questions, answers