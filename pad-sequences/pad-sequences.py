import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return [[]]
    if max_len:
        for i in range(len(seqs)):
            if len(seqs[i]) > max_len:
                seqs[i] = seqs[i][:max_len]
            else:
                difference = max_len - len(seqs[i])
                for _ in range(difference):
                    seqs[i].append(pad_value)
    if not max_len:
        temp_max = max(len(seq) for seq in seqs)
        for i in range(len(seqs)):
            if len(seqs[i]) > temp_max:
                seqs[i] = seqs[i][:temp_max]
            else:
                difference = temp_max - len(seqs[i])
                for _ in range(difference):
                    seqs[i].append(pad_value)
    return seqs