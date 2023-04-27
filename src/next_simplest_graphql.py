'''
The next simplest possible Python script that shows GraphQL in action.
This one shows what GraphQL was invented for, namely, you can ask
for specific data and GraphQL will send back specifically what you ask for.

Author: KEN
Date:   2023.04.26
'''

# graphql_api.py
from flask import Flask
from flask_graphql import GraphQLView
import graphene

# This class has a lot of data (id, name, age, email) 
# OK, fair enough, that is not really a lot. But anyway
# we will see with GraphQL that you can request
# just the data you want instead of everything. 
# NOTE: You have to be careful about your variable
# names. Using "snakecase" winratio will work, but if
# you try to use "camelcase" win_ratio it will not work!
# It's the year 2023, who can believe this nonsense?!
class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Int()
    email = graphene.String()
    winratio = graphene.Float()

class Query(graphene.ObjectType):
    user = graphene.Field(User)

    def resolve_user(self, info):
        return User(id=1, name="Roger Federer", 
                    age=37, email="roger@example.com", winratio=99.56)

schema = graphene.Schema(query=Query)

app = Flask(__name__)

# This is the part that defines localhost:500/graphql
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
