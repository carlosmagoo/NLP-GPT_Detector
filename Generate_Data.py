import pandas as pd
import os
import openai
import time
import random

openai.api_key = "#################################"

df_big = pd.read_csv('...', lines=True, nrows=10000)
split_size = len(df_big) // 10

# Split the dataset into 10 smaller DataFrames
df1 = df_big.iloc[:split_size]
df2 = df_big.iloc[split_size:split_size*2]
df3 = df_big.iloc[split_size*2:split_size*3]
df4 = df_big.iloc[split_size*3:split_size*4]
df5 = df_big.iloc[split_size*4:split_size*5]
df6 = df_big.iloc[split_size*5:split_size*6]
df7 = df_big.iloc[split_size*6:split_size*7]
df8 = df_big.iloc[split_size*7:split_size*8]
df9 = df_big.iloc[split_size*8:split_size*9]
df10 = df_big.iloc[split_size*9:]

Currect_df = df10
result = []
i = 0

for _, row in Currect_df.iterrows():
    instructions = row['instructions']

    prompts = [
        f"{instructions}",
    ]

    prompt = random.choice(prompts)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": " "},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=2004,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["?"],
    )
    essay = response.choices[0].message.content.strip()
    result.append(essay)
    print(i)
    time.sleep(21)
    i = i + 1

    
Currect_df['essay_result'] = result

Currect_df.to_csv('data_gbt10.csv', index=False)
Currect_df.to_pickle("df_big10.pkl")  


