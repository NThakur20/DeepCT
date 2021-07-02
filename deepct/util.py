import numpy as np

def subword_weight_to_word_weight(subword_weight_str, m, smoothing, keep_all_terms):
    fulltokens = []
    weights = []
    for item in subword_weight_str.split('\t'):
        token, weight = item.split(' ')
        weight = float(weight)
        token = token.strip()
        if token.startswith('##'):
            fulltokens[-1] += token[2:]
        else:
            fulltokens.append(token)
            weights.append(weight)
    assert len(fulltokens) == len(weights)
    fulltokens_filtered, weights_filtered = [], []
    selected_tokens = {}
    for token, w in zip(fulltokens, weights):
        if token == '[CLS]' or token == '[SEP]' or token == '[PAD]':
            continue

        if w < 0: w = 0
        if smoothing == "sqrt":
            tf = int(np.round(m * np.sqrt(w)))
        else:
            tf = int(np.round(m * w))
        
        if tf < 1: 
            if not keep_all_terms: continue
            else: tf = 1

        selected_tokens[token] = max(tf, selected_tokens.get(token, 0))

    return selected_tokens