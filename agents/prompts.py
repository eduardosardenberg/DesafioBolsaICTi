def planner_prompt_ptbr(asset_name, news_list):
    prompt = (
        f"Você é um consultor financeiro. Com base nas notícias completas a seguir sobre {asset_name}, "
        "o investidor deve COMPRAR, VENDER ou MANTER este ativo? "
        "Dê a recomendação (a primeira palavra deve ser COMPRAR, VENDER ou MANTER), seguida de uma explicação clara e curta, em português, para um usuário leigo.\n\n"
    )
    for news in news_list:
        prompt += f"Título: {news['title']}\n"
        if news.get("content"):
            prompt += f"Notícia: {news['content']}\n"
    prompt += "\nSua recomendação (primeira palavra deve ser COMPRAR, VENDER ou MANTER), seguida da justificativa:\n"
    return prompt
