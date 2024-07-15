def exercise1(tp, fp, fn):
    if type(tp) is not int:
        print("tp must be int")
        return
    if type(fp) is not int:
        print("fp must be int")
        return
    if type(fn) is not int:
        print("fn must be int")
        return
        
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, fn must be greater than zero")
        return
        
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f'Precision: {precision}\n Recall: {recall}\n F1-Score: {f1_score}')
    
if __name__ == '__main__':
    exercise1(tp=2, fp=3, fn=4)
    exercise1(tp='a',fp=3,fn=4)
    exercise1(tp=2,fp='a',fn=4)
    exercise1(tp=2,fp=3,fn='a')
    exercise1(tp=2,fp=3,fn=0)
    exercise1(tp=2.1,fp=3,fn=0)