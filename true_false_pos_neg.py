# True Positive : Given a 1 class if the model predicts it as 1 class 
# True Negative : Given a 0 class if the model predicts it as 0 class
# False Positive : Given a 0 class if the model predicts it as 1 class
# False Negative : Given a 1 class if the model predicts it as 0 class

def true_positive(y_true, y_pred) -> int:
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if (yt == 1) & (yp == 1):
            tp += 1
    return tp

def true_negative(y_true, y_pred) -> int:
    tn = 0
    for yt, yp in zip(y_true, y_pred):
        if (yt==0) and (yp==0):
            tn += 1
    return tn

def false_positive(y_true, y_pred) -> int:
    fp = 0
    for yt, yp in zip(y_true, y_pred):
        if (yt==0) and (yp==1):
            fp += 1
    return fp
    
def false_negative(y_true, y_pred) -> int:
    fn = 0
    for yt, yp in zip(y_true, y_pred):
        if (yt==1) and (yp==0):
            fn+=1
    return fn