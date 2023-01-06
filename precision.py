from true_false_pos_neg import true_positive, false_positive

def precision(y_true, y_pred) -> float:
    pr = 0
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    return (tp/(tp+fp))