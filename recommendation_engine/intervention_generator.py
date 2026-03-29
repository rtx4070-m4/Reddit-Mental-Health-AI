
def recommend(score):

    if score > 0.85:
        return "Immediate crisis hotline recommendation"
    elif score > 0.6:
        return "Encourage professional counseling"
    elif score > 0.4:
        return "Suggest mental health resources"
    else:
        return "No immediate risk detected"
