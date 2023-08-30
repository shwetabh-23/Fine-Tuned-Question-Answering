import modules as m
from transformers import BertTokenizerFast

train_passage, train_questions, train_answers = m.read_file(r'D:\ML-Projects\Fine-Tuned-Question-Answering\Data\train-v2.0.json')
valid_passage, valid_questions, valid_answers = m.read_file(r'D:\ML-Projects\Fine-Tuned-Question-Answering\Data\dev-v2.0.json')

train_answers = m.add_end_idx(train_answers, train_passage)
valid_answers = m.add_end_idx(valid_answers, valid_passage)
breakpoint()