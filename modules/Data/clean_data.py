


def add_end_idx(answers, passages):
    for answer, passage in zip(answers, passages):
        
        answer_req = answer['text']
        answer_start = answer['answer_start']
        answer_end = answer_start + len(answer_req)
        
        if passage[answer_start:answer_end] == answer_req:
            answer['answer_end'] = answer_end
        elif passage[answer_start-1:answer_end-1] == answer_req:
            answer['answer_start'] = answer['answer_start'] - 1
            answer['answer_end'] = answer_end - 1
        if passage[answer_start-2:answer_end-2] == answer_req:
            answer['answer_start'] = answer['answer_start'] - 2
            answer['answer_end'] = answer_end-2
    return answers