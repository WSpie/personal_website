import pandas as pd

def text_generation(prompt, client, model, logger):
    
    try:
        prompt_df = pd.read_parquet(logger.prompt_df_path)
        user_prompt = {'role': 'user', 'content': prompt}
        prompt_df = prompt_df.append(user_prompt)
        prompt_df.to_parquet(logger.prompt_df_path)
        completion = client.chat.completions.create(
            model=model,
            messages=prompt_df.to_dict(orient='records')
        )
        feedback = completion.choices[0].message.content.strip()
        if feedback:
            prompt_df = prompt_df.append({'role': model, 'content': feedback})
            prompt_df.to_parquet(logger.prompt_df_path)
    except Exception as e:
        logger.log_error(e)

    return logger