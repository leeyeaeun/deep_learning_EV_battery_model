import pandas as pd

test_label = pd.read_csv('test_label.csv')
train_label = pd.read_csv('train_label.csv')


test_label['car'] = test_label['car'] - 800
test_label.to_csv('test_label.csv', index=False)

train_label['car'] = train_label['car'] - 800
train_label.to_csv('train_label.csv', index=False)
