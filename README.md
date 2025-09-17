# Investment News Agents

Functional GenAI multi-agent prototype for the financial domain.

## How it works

- The system asks the user to input their name and, one by one, the assets they want to analyze.
- For each asset, you can enter the ticker (e.g. PETR4.SA) or the company name (e.g. Petrobras).
- The News Agent fetches the latest Google News for each asset.
- The Planner Agent analyzes the news with a real LLM (GPT, in Portuguese) and provides a recommendation (COMPRAR, VENDER, MANTER), with an explanation for each case.
- The user can add as many assets as desired.  
  To finish and get the final report, just type **fim** (any capitalization) when prompted for a new asset.
- At the end, a summary report with all recommendations is shown.

## How to run

1. Clone the repository or copy the files to a local folder.
2. Make sure you have Python 3.8+ installed.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root of the project with your OpenAI key:
   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```
5. Run:
   ```bash
   python main.py
   ```

## Project Structure

```
main.py
agents/
    news_agent.py
    planner.py
    prompt.py
.env
requirements.txt
```

## Example interaction

```
Bem-vindo ao seu assistente de investimentos multiagente.

Digite seu nome: "Nome"

Digite o ticker ou nome da empresa (ex: PETR4.SA ou Petrobras), ou "FIM" para encerrar: PETR4.SA
Nome (opcional) para o ativo PETR4.SA (aperte Enter para deixar igual ao ticker):

--- PETR4.SA (PETR4.SA) ---
* Petrobras may redirect oil to Asia due to US tariff...
* Petrobras to invest $4.8 billion in integration...
...

Recomendação: VENDER
- VENDER. Justificativa: [explicação da LLM em português]

Digite o ticker ou nome da empresa (ex: PETR4.SA ou Petrobras), ou "FIM" para encerrar: fim

===== RELATÓRIO FINAL =====

Usuário: Pedro
- PETR4.SA (PETR4.SA): VENDER
  Justificativa: [explicação da LLM em português]

Obrigado por utilizar o assistente de investimentos multiagente!
```

## Author

Eduardo Sardenberg Tavares