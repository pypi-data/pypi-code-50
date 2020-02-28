import json
import boto3
import uuid
import datetime
from boto3.dynamodb.conditions import Key

class DynamoDB:
    def __init__(self, region):
         self._dynamodb = boto3.resource('dynamodb', region_name=region)
    def WriteChallange(self,challange):
        table = self._dynamodb.Table('TMMissionControlChallengeBank')
        response = table.put_item(
            Item= challange )
        print("PutItem succeeded:")
        print(json.dumps(response))
    def GetTeamsFromGame(self, gameID):
        table = self._dynamodb.Table('TMMissionControlTeams')
        resp = table.query(
            # Add the name of the index you want to use in your query.
            IndexName="GameID-index",
            KeyConditionExpression=Key('GameID').eq(gameID),
        )
        return resp
    def GetGameFromGame(self, gameID):
        table = self._dynamodb.Table('TMMissionControlGames')
        resp = table.query(
            KeyConditionExpression=Key('GameID').eq(gameID),
        )
        return resp

#Coginto
def GetEmailOfRequester(event):
    return event['requestContext']['authorizer']['claims']['email']
def GetCogintoIdOfRequester(event):
    return event['requestContext']['authorizer']['claims']['cognito:username']
def GetNameOfRequester(event):
    return event['requestContext']['authorizer']['claims']['name']


def handler(event, context):
    print(event)
    gameID = event['pathParameters']['game']
    db = DynamoDB(region="us-east-1")
    game = db.GetGameFromGame(gameID=gameID)
    if 'Blackout' in game['Items'][0]:
        blackoutTime = game['Items'][0]['Blackout']
        format = '%Y-%m-%dT%H:%M:%S.%fZ'
        utc = datetime.datetime.utcnow()
        d = datetime.datetime.strptime(blackoutTime, format)
        if d < utc:
            print("blackout")
            return {
            'statusCode': 200,
            'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials' : True
            },
            'body': json.dumps( {'blackout': True } )
        }
    print(game)
    try:
        r = db.GetTeamsFromGame(gameID=gameID)
        list = r['Items']
        list.sort(key=sortScore, reverse=True)
        top10 = list[:10]
        teamData = []

        for team in top10:
            teamData.append(ParseData(team=team))
    except:
        teamData = []
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials' : True
        },
        'body': json.dumps(teamData)
    }

def ParseData(team):
    results = []
    for point in team['CompletedChallenges']:
        results.append(
            {
                "x": point[3],
                "y": float((point[2]))
            }
        )
    for hint in team['ResolvedHints']:
        results.append(
            {
                "x": hint['timeStamp'],
                "y": float(hint['penalty'])
            }
        )

    results.sort(key=sortDate)
    total = 0
    for point in results:
        total = total + point['y']
        point['y'] = total

    teamData = {
        "results":results,
        "name": team['Name']
    }

    return teamData

def sortScore(val):
    return float(val['Score'])

def sortDate(val):
    return val['x']

if __name__ == '__main__':
    db = DynamoDB(region="us-east-1")
    gameID="f4d3c078-d9a6-4a67-8f6b-48416e3358be"
    game = db.GetGameFromGame(gameID=gameID)
    if 'blackout' in  game['Items'][0]:
        blackoutTime = game['Items'][0]['Blackout']
        format = '%Y-%m-%dT%H:%M:%S.%fZ'
        utc = datetime.datetime.utcnow()
        d = datetime.datetime.strptime(blackoutTime, format)
        if d < utc:
            print("blackout")
    print(game)
    r = db.GetTeamsFromGame(gameID="f4d3c078-d9a6-4a67-8f6b-48416e3358be")
    list = r['Items']
    list.sort(key = sortScore, reverse=True)
    top10 = list[ :10]
    teamData = []
    for team in top10:
        teamData.append( ParseData(team=team) )

    print(top10)