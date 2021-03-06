import requests, json, os

def getQuestionList():
    '''
    获取问题邀请列表
    '''
    url = 'https://www.zhihu.com/api/v4/questions/{}/recommendation_invitees?include=%5B%2A%5D.member.answer_count%2Carticles_count%2Cfollower_count%2Cgender%2Cis_followed%2Cis_following%2Cbadge&limit=20&keyword=&offset=0'.format(QuestionID)
    header = {
        "cookie": COOKIE,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }
    return requests.get(url=url,headers=header).json()['data']

def postQuestionInvitees(memberID):
    '''
    邀请问题回答
    '''
    global COUNT
    url = 'https://www.zhihu.com/api/v4/questions/{}/invitees'.format(QuestionID)
    header = {
        "cookie": COOKIE,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }
    data = {
        "member_hash": memberID,
        "src": "normal",
    }
    response = requests.post(url=url,headers=header,data=json.dumps(data))
    if response.status_code == 200:
        COUNT += 1

if __name__=="__main__":
    COOKIE = os.environ.get('COOKIE')
    QuestionID = os.environ.get('QuestionID')
    COUNT = 0
    for i in range(20):
        members = getQuestionList()
        for _member in members:
            postQuestionInvitees(_member['member']['id'])
    print("本次操作一共邀请了{}人".format(COUNT))
