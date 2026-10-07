from datetime import datetime
year = datetime.now().year

def get_age(naissance):
    age = year - naissance
    return(age)
