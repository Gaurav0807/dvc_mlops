import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def create_dataframe():
    data = {
        "id": [1,2,3,4,5,6,7,8],
        "review": [
            "Great food and ambiance",
            "Terrible Service",
            "Amazing Experience",
            "Food was cold",
            "Loved the deserts",
            "Not worth the money",
            "Excellent customer service",
            "Place was too much crowded but its good"
        ]
    }

    df = pd.DataFrame(data=data)
    return df

def save_dataframe(df):
    if not os.path.exists("data"):
        os.makedirs("data")
    df.to_csv("data/data.csv", index=False)
    print("Data Saved to Folder")


def process_data(k):

    df = pd.read_csv("data/data.csv")

    #Apply Vectorization
    vectorizer = CountVectorizer(max_features=k)
    vectorized_data = vectorizer.fit_transform(df["review"])
    feature_name = vectorizer.get_feature_names_out()

    #Create a new dataframe with K new Columns
    vectorized_df = pd.DataFrame(vectorized_data.toarray(), columns=feature_name)
    processed_df = pd.concat([df,vectorized_df],axis=1)

    processed_df.to_csv("data/processed_data.csv",index=False)
    print(f"processed data csv saced on data folder with {k} new columns")
    return processed_df


if __name__ == "__main__":
    df = create_dataframe()
    
    save_dataframe(df)

    k = 3
    processed_df = process_data(k)

    print(f"Data Shape : {df.shape}")
    print(f"Processed Data Shape : {processed_df.shape}")



