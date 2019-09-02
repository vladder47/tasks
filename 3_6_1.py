import requests

with open('dataset_3378_3.txt') as nf:
    s = nf.readline().strip()
r = requests.get(s)
while r.text[0:2] != 'We':
    m = 'https://stepic.org/media/attachments/course67/3.6.3/'
    m += r.text
    r = requests.get(m)
    print(r.text)




