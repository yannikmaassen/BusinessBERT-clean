import pandas as pd

df = pd.read_csv("../../../fiqa-2018/train.csv")

if "format" in df.columns:
    df["format"] = df["format"].astype(str).str.lower().str.strip()
    df = df[df["format"].isin({"post", "headline"})]

col_map_candidates = [
    {"sentence": "sentence", "snippets": "snippets", "target": "target", "sentiment_score": "sentiment_score"},
]

for cmap in col_map_candidates:
    if all(c in df.columns for c in cmap.values()):
        df = df.rename(columns={v: k for k, v in cmap.items() if v != k})
        break
else:
    missing = {"sentence", "snippets", "target", "sentiment_score"} - set(df.columns)
    raise ValueError(
        f"Could not find required columns. Missing: {missing}. "
        f"Available columns: {list(df.columns)}"
    )

df["sentiment_score"] = pd.to_numeric(df["sentiment_score"], errors="coerce")
df = df.dropna(subset=["sentence", "snippets", "target", "sentiment_score"])
df = df[["sentence", "snippets", "target", "sentiment_score"]].sample(frac=1).reset_index(drop=True)

df.to_json("fiqa_train.json", orient="records")