from true_false_pos_neg import true_positive, false_negative

def recall(y_true, y_pred) -> float:
    re = 0
    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    return tp/(tp+fn)
