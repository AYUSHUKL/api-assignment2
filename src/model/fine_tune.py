from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification

def fine_tune_model(data):
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
    trainer = Trainer(model=model, args=TrainingArguments("test_trainer"), train_dataset=data)
    trainer.train()
