from main import *

async def work_with_table(mas, parametr):
    text = 'Список победителей'
    # await bot.send_message(chat_id=ADMIN, text=text)
    if parametr == 'ALL':
        indx = 0
        for x in range(len(mas)):
            indx += 1
            text = f"{text}\n{indx}. {mas[x][1]}"
        return text
    elif parametr == 'YES':
        indx = 0
        for x in range(len(mas)):
            if mas[x][2] == 'YES':
                indx +=1
                text = f"{text}\n{indx}. {mas[x][1]} (proof {mas[x][4]})"
        return text
    # print(*mas)


