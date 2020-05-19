data = [
    ["bread", "jam", "butter"],
    ["bread", "butter"],
    ["bread", "milk", "butter"],
    ["chocolate", "bread", "milk", "butter"],
    ["chocolate", "milk"]
]
supp_df = apriori(data, min_support=0.3)
print(supp_df)

conf_df = association_rule(supp_df['ItemSet'].tolist(), min_confidence=0.8)
print(conf_df)