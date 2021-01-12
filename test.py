import pandas as pd

thresholds = [('low', 0),('medium',0.5),('high',1)]
thresholds = pd.DataFrame(thresholds)
print(thresholds)

prob = pd.Series([1,2,3,4,5,6])

for p in prob:
        print("prob start")
        for _, row in thresholds.iterrows():
                #print(row[0])
                print(p,"--",row[1])

        print("prob done")



