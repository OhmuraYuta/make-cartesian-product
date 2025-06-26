import csv
import itertools
import pandas as pd

input_path = input('入力元:')
output_path = input('出力先:')

with open(input_path) as f:
    reader = csv.reader(f)
    li = [row for row in reader]  # 二次元のリストにする
    columns_li = [list(x) for x in zip(*li)]  # 列ごとのリストにする
    # 空欄をなくす処理
    clean_columns_li = [[column for column in columns if column != ''] for columns in columns_li]

    # ヘッダーを削除
    args = [clean_columns[1:] for clean_columns in clean_columns_li]

    # 直積作成
    cartesian_product = list(itertools.product(*args))

    df = pd.DataFrame(cartesian_product)
    # ヘッダーを設定
    df.columns = [clean_columns[0] for clean_columns in clean_columns_li]
    df.head()
    # csvに出力
    df.to_csv(output_path)