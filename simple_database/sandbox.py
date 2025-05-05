from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
tokens = tokenizer("The quick brown fox", return_tensors="pt")
print(tokens)