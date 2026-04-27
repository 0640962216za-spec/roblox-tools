class RobloxAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = None

    def login(self):
        self.session = self._create_session()
        # Perform login and handle errors
        print('Logged in successfully')

    def logout(self):
        if self.session:
            self.session.close()
            self.session = None
            print('Logged out successfully')

    def _create_session(self):
        import requests
        session = requests.Session()
        # Perform session setup
        return session

    def fetch_user_data(self, user_id):
        if not self.session:
            print('User not logged in')
            return
        # Simulated API request
        response = self.session.get(f'https://api.roblox.com/users/{user_id}')
        return response.json() if response.ok else None

    def update_user_status(self, user_id, status):
        if not self.session:
            print('User not logged in')
            return
        # Simulated API request to update status
        data = {'status': status}
        response = self.session.post(f'https://api.roblox.com/users/{user_id}/status', json=data)
        return response.ok