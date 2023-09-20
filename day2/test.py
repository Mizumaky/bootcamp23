# write code for chatgpt

import os
import sys
import json
import torch
import argparse
import numpy as np
from tqdm import tqdm
from torch.utils.data import DataLoader
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

from dataset import GPT2Dataset
from utils import get_logger

logger = get_logger()


def parse_args():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--test_data", type=str, default="./data/test.txt")
    parser.add_argument("--model_path", type=str, default="./model")
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--max_len", type=int, default=64)
    parser.add_argument("--top_k", type=int, default=5)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()
    return args


def main(args):
    # load model
    tokenizer = GPT2TokenizerFast.from_pretrained(args.model_path)
    model = GPT2LMHeadModel.from_pretrained(args.model_path)
    model.to(args.device)
    model.eval()

    # load test data
    test_dataset = GPT2Dataset(args.test_data, tokenizer, args.max_len)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False)

    # generate responses
    responses = []
    for batch in tqdm(test_loader):
        batch = batch.to(args.device)
        outputs = model.generate(
            input_ids=batch,
            max_length=args.max_len,
            do_sample=True,
            top_k=args.top_k,
            top_p=args.top_p,
            temperature=1.0,
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=1,
        )
        responses.extend(outputs.tolist())

    # save responses
    with open("responses.json", "w") as f:
        json.dump(responses, f)