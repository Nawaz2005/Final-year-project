def get_recommendation(days, smoker, hba1c):
    advice = []

    if days > 20:
        advice.append("Delayed healing: frequent dressing and monitoring advised.")

    if smoker == 1:
        advice.append("Smoking cessation recommended to improve healing.")

    if hba1c > 0.7:
        advice.append("Poor glucose control: consult physician for diabetes management.")

    advice.append("Maintain wound hygiene and sterile dressing.")

    return advice
