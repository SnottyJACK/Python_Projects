# Нужно рассмотреть больше случаев в if-elif-else
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder == 0 or remainder >= 5 or messages_count == 11:
        print("У вас " + str(messages_count) + " новых сообщений")
    elif remainder == 1:
        print("У вас " + str(messages_count) + " новое сообщение")
    else:
        print("У вас " + str(messages_count) + " новых сообщения")
