from sentence_transformers import SentenceTransformer,util

model = SentenceTransformer("stsb-xlm-r-multilingual")

sentences = [
    "私は犬の散歩に行きました。",
    "今日は良い天気ですね。",
    "プログラミングを勉強するのが好きです。",
    "美味しいコーヒーを飲みたいです。", 
    "彼は勉強が大好きです。"
]

query = "Pythonの学習は楽しい。"

sentence_embeddings = model.encode(sentences,convert_to_tensor=True)
query_embedding = model.encode(query,convert_to_tensor=True)

similarities = util.cos_sim(query_embedding,sentence_embeddings)[0]
sorted_indices = similarities.argsort(descending=True)

print("検索ワード:",query)
print("| ------ | ---------------------------------- |")
print("| 類似度 |                 文章               |")
print("| ------ | ---------------------------------- |")
for index in sorted_indices:
    print(f"| {similarities[index]:.4f} | {sentences[index]} |")