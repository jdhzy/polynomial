import re
from statistics import mean

def countPoop(text):
    poop = '💩'
    count = {}

    for line in text.splitlines():
        if poop in line:
            # Use regex to better handle names and messages
            parts = re.split(r'\.\s+', line, 1)  # Handle splitting on ". " correctly
            if len(parts) == 2:
                person_message = parts[1].split(' ', 1)
                if len(person_message) == 2:
                    person, message = person_message
                    person = person.strip()
                    message = message.strip()
                    
                    c = message.count(poop)  # Count the poops in the message
                    
                    if person in count:
                        count[person] += c
                    else:
                        count[person] = c
    return count

def poopStat(text):
    outcome = countPoop(text)
    for name in outcome:
        print(f'{name} 本月进行了{outcome[name]}次💩')

def poopChamp(text):
    counts = countPoop(text)
    if counts:  # Only proceed if the dictionary is not empty
        champ = max(counts, key=counts.get)
        print(f'让我们祝贺 {champ} 以{counts[champ]}次💩夺得本月的冠军🏆！')
    else:
        print("没有找到任何💩！")

def poopContestBegins(data):
    poopStat(data)
    poopChamp(data)

data = '''#接龙

1. yuxii3 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
2. ：） 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
3. yichun🧸 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
4. joanne(; 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩
5. 保温杯里伏特加 💩💩💩💩💩💩💩💩💩💩💩💩💩'''

poopContestBegins(data)

