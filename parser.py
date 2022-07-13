import requests

groupShortcut = input('Введите последние буквы в поисковой строке группы: ') #пример:
                                                        #ссылка: https://vk.com/lovebmstu
                                                        #нужно ввести: lovebmstu
def getGroupID(groupID):
    url = 'https://api.vk.com/method/groups.getById'
    token = '75afa40b75afa40b75afa40b9875d2c6f6775af75afa40b17621c39827a748024ceea70'
    params = {
        'group_id': groupID,
        'access_token': token,
        'v': '5.92'
    }
    response = requests.get(url, params).json()
    return response['response'][0]['id']

def getUsersCount(groupID):
    url = 'https://api.vk.com/method/groups.getMembers'
    token = '75afa40b75afa40b75afa40b9875d2c6f6775af75afa40b17621c39827a748024ceea70'
    params = {
        'group_id': groupID,
        'access_token': token,
        'v': '5.92'
    }
    response = requests.get(url, params).json()
    return response['response']['count']

def getUsersSex(groupID, offset):
    url = 'https://api.vk.com/method/groups.getMembers'
    token = '75afa40b75afa40b75afa40b9875d2c6f6775af75afa40b17621c39827a748024ceea70'
    params = {
        'group_id': groupID,
        'access_token': token,
        'v': '5.92',
        'fields': 'sex',
        'offset': offset
    }
    response = requests.get(url, params).json()
    return response['response']['items']

currGroupID = getGroupID(groupShortcut)
membersCount = int(getUsersCount(currGroupID))
girlsList = []
currLen = 0
offset = 0

while ((membersCount - offset) > currLen):
    arrayOfUsers = getUsersSex(currGroupID, offset)
    currLen = len(arrayOfUsers)
    filtered = list(filter(lambda x: x['sex'] == 1, arrayOfUsers))
    girlsList += [f'https://vk.com/id{user["id"]}' for user in filtered]
    offset += currLen
temp = '\n'.join(girlsList)

with open('list.txt', 'w') as f:
    f.write(temp)