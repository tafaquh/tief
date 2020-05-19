from tief.association import apriori

data = [
    ["roti", "selai", "mentega"],
    ["roti", "mentega"],
    ["roti", "susu", "mentega"],
    ["coklat", "roti"],
    ["coklat", "susu"]
]
apriori(data, min_support=0.3)