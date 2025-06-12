import pandas as pd

df = pd.read_csv('bestsellers.csv')

print(df.head())
print(df.columns)
print(df.shape)
print(df.describe())

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

df["Price"] = df["Price"].astype(float)

author_count = df["Author"].value_counts()
print(author_count)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()

print(avg_rating_by_genre)

author_count.head(10).to_csv("top_authors.csv", index=True)

avg_rating_by_genre.to_csv("avg_rating_by_genre.csv", index=True)