def accuracy(y_true, y_pred):
    correct_counter = 0
    for act, pred in zip(y_true, y_pred):
        if act == pred:
            correct_counter += 1
    return (correct_counter/len(y_true))