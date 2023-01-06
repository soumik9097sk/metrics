import recall
if __name__=="__main__":
    y_true = [1,0,0,0,1,1,0,0,1,0]
    y_pred = [1,0,1,0,1,0,1,0,0,1]
    pr = recall.recall(y_true, y_pred)
    print(pr)