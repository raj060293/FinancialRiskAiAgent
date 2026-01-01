import config.env
from agents.risk_detector import detect_risk
from agents.risk_reasoner import reason_risk


def main():
    print("Hello from financial-risk-agent!")

def process_transaction(transaction: dict):
    print("Processing transaction:", transaction)

    try:
        result = detect_risk(transaction)
        print("Risk Detection Result:", result)

        if result["risk_level"] == "LOW":
            return {
                "final_action" : "ALLOW",
                "reason" : "Low risk transaction"
            }

        reasoning = reason_risk(transaction, result)
        print("Reasoning: ", reasoning)
        return {
            "risk_score": reasoning["risk_score"],
            "explanation": reasoning["explanation"],
            "final_action": reasoning["recommended_action"]
        }

    except Exception as e:
        print("Risk Detection failed completely:", e)
        return {
            "final_action": "ESCALATE",
            "reason" : "Risk detection failure"
        }


if __name__ == "__main__":
    main()
