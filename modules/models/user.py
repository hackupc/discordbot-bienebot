class User:

    def __init__(self, name, userid, roles):
        role_names = [e.name for e in roles]
        team = [item for item in role_names if item.startswith('team')]
        self.name = name
        self.id = userid
        self.roles = roles
        self.is_in_team = any(team)
        if not self.is_in_team:
            self.team = None
        else:
            self.team = team[0].split('-')[1]

    def save(self):
        print(self.name)
        print('Saved')

    def connect(self):
        print(self)
        print('Get info')
