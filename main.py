import modules as m
from transformers import BertTokenizerFast, BertForQuestionAnswering, AdamW
from tqdm import tqdm
import torch

train_passage, train_questions, train_answers = m.read_file(r'D:\ML-Projects\Fine-Tuned-Question-Answering\Data\train-v2.0.json')
valid_passage, valid_questions, valid_answers = m.read_file(r'D:\ML-Projects\Fine-Tuned-Question-Answering\Data\dev-v2.0.json')

train_answers = m.add_end_idx(train_answers, train_passage)
valid_answers = m.add_end_idx(valid_answers, valid_passage)

tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

train_encodings = tokenizer(train_passage, train_questions, padding = True, truncation = True)
valid_encodings = tokenizer(valid_passage, valid_questions, padding = True, truncation = True)

m.add_token_position(train_encodings, train_answers, tokenizer)
m.add_token_position(valid_encodings, valid_answers, tokenizer)

train_dataset = m.squad_dataset(train_encodings)
valid_dataset = m.squad_dataset(valid_encodings)

train_loader = m.make_dataloader(train_dataset)
valid_loader = m.make_dataloader(valid_dataset)


device = torch.device('cuda')

model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')
model.to(device)

epochs = 5
lr = 1e-5
optim = AdamW(model.parameters(), lr)
model.train()

for epoch in range(epochs):

    with tqdm(train_loader) as loop:
        for batch in loop:

            optim.zero_grad()

            input_ids = batch['input_ids'].to(device)
            masks = batch['attention_mask'].to(device)
            start_pos = batch['start_positions'].to(device)
            end_pos = batch['end_positions'].to(device)

            outputs = model(input_ids = input_ids, attention_mask = masks, start_positions = start_pos, end_positions = end_pos)
            loss = outputs[0]
            loss.backward()
            optim.step()
model_path = r'D:\ML-Projects\Fine-Tuned-Question-Answering\modules\Model'
model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)
breakpoint()