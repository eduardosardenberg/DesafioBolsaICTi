from agents.news_agent import NewsAgent
from agents.planner import PlannerAgent
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Bem-vindo ao seu assistente de investimentos multiagente.\n")
    user = input("Digite seu nome: ") or "Usuário"
    news_agent = NewsAgent()
    planner_agent = PlannerAgent()

    analyzed_assets = []

    while True:
        ticker = input('\nDigite o ticker ou nome da empresa (ex: PETR4.SA ou Petrobras), ou "FIM" para encerrar: ').strip()
        if ticker.lower() == "fim":
            break

        name = input(f"Nome (opcional) para o ativo {ticker} (aperte Enter para deixar igual ao ticker): ") or ticker

        print(f"\n--- {name} ({ticker}) ---")
        news = news_agent.get_news(ticker)
        if not news:
            print("Nenhuma notícia encontrada para este ativo.")
        else:
            for n in news:
                print(f"* {n['title']} ({n.get('published', '')})")

        rec, reasons = planner_agent.analyze_news(name, news)
        print(f"\nRecomendação: {rec}")
        for r in reasons:
            print(f"- {r}")

        analyzed_assets.append({
            "name": name,
            "ticker": ticker,
            "recommendation": rec,
            "reason": reasons[0] if reasons else ""
        })

 
    # Gera relatório final resumido
    print("\n===== RELATÓRIO FINAL =====\n")
    print(f"Usuário: {user}")
    for asset in analyzed_assets:
        print(f"- {asset['name']} ({asset['ticker']}): {asset['recommendation']}")
        print(f"  Justificativa: {asset['reason']}\n")
    print("Obrigado por utilizar o assistente de investimentos multiagente!")
    
if __name__ == "__main__":
    main()
