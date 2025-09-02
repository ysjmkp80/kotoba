import pandas as pd
# import matplotlib.pyplot as plt
 import nlplot
# from plotly.offline import iplot
from janome.tokenizer import Tokenizer
tknzr = Tokenizer()

# データファイルを読み込んでデータフレームを作成
df = pd.read_csv('sample.csv', encoding='utf8', header=0, usecols=['アンケート内容'])

# ストップワードの設定
stop_words = {"こと","もの"}

# 単語の抽出とリスト化
def extract_words(text):
    # 単語を格納するリスト
    word_list = []
    # 単語の抽出
    word_list = [token.surface for token in tknzr.tokenize(text) if token.part_of_speech.startswith('名詞')]
    # word_list = [token.surface for token in tknzr.tokenize(text) if token.part_of_speech.startswith('名詞,一般') or token.part_of_speech.startswith('名詞,固有名詞')]
    # ストップワードの適用
    word_list = [x for x in word_list if x not in stop_words]
    # 単語リストを返す
    return word_list

# 単語リストの列をデータフレームに追加
df['words'] = df['アンケート内容'].apply(extract_words)

# データフレームを表示
print(df)

# target_colを指定する
npt = nlplot.NLPlot(df, target_col='words')

# top_nで頻出上位単語, min_freqで頻出下位単語を指定できる
stopwords = npt.get_stopword(top_n=0, min_freq=0)

#単語頻出ランキングを作成
fig_unigram = npt.bar_ngram(
    title='uni-gram',
    xaxis_label='word_count',
    yaxis_label='word',
    ngram=1,
    top_n=50,
    stopwords=stopwords,
)
#単語頻出ランキングを表示
#fig_unigram.show()
# # うまく表示されない場合はファイルに保存する
 fig_unigram.write_html("unigram.html")

