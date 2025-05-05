from transformers import AutoTokenizer, AutoModel
import torch
import typing

'''
Use a pre-trained model to turn text into vectors
'''

class TextEmbedder:

    def __init__(self, model_name = "sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModel.from_pretrained("bert-base-uncased")
        self.model.eval()

    def embed(self, text: str) -> torch.Tensor:

        token = self.tokenizer(text, return_tensors="pt", truncation=True)
        

    

class VectorDB():

    def add(self, text: str):
        pass

    def search():
        pass

    def load():

        pass

def main():

    # add dummy documents

    # run the search query

    # print the top matches

    pass