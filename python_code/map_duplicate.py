from collections import Counter

data = [{"name" : "xyz", "email": "xyz@gmail.com"},
        {"name" : "xye", "email": "xyz@gmail.com"},
        {"name" : "ram", "email": "ram@gmail.com"},
        {"name" : "shyam", "email": "xyz@gmail.com"},
        {"name" : "ghansyam", "email": "ram@gmail.com"}]

email_list = [i["email"] for i in data]
print(email_list)
counter = Counter()
counter = Counter(email_list)
print(counter)
res_list =[]
for k,v in counter.items():
    if v >=2 :
        res_list = []
        for i in data:
            if i["email"] == k:
                res_list.append(i["name"])

        print(k,res_list)