


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

def add_token_position(encodings, answers, tokenizer):
    start_positions = []
    end_positions = []
    for i in range(len(answers)):
        start_positions.append(encodings.char_to_token(i, answers[i]['answer_start']))
        end_positions.append(encodings.char_to_token(i, answers[i]['answer_end'] - 1))

        # if start position is None, the answer passage has been truncated
        if start_positions[-1] is None:
            start_positions[-1] = tokenizer.model_max_length
        if end_positions[-1] is None:
            end_positions[-1] = tokenizer.model_max_length

    encodings.update({'start_positions': start_positions, 'end_positions': end_positions})