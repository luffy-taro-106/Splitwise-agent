import requests
from requests_oauthlib import OAuth1
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

class SplitwiseAPI:
    def __init__(self):
        self.auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        self.base_url = 'https://secure.splitwise.com/api/v3.0/'

    def get_categories(self):
        """Get a list of all expense categories."""
        response = requests.get(self.base_url + 'get_categories', auth=self.auth)
        return response.json().get('categories', [])

    def get_currencies(self):
        """Get a list of all supported currencies."""
        response = requests.get(self.base_url + 'get_currencies', auth=self.auth)
        return response.json().get('currencies', [])

    def get_notifications(self, limit=10):
        """Get recent notifications for the current user."""
        params = {'limit': limit}
        response = requests.get(self.base_url + 'get_notifications', params=params, auth=self.auth)
        return response.json().get('notifications', [])

    def delete_comment(self, comment_id):
        """Delete a comment by its ID."""
        response = requests.post(self.base_url + f'delete_comment/{comment_id}', auth=self.auth)
        return response.json()

    def create_comment(self, expense_id, content):
        """Add a comment to an expense."""
        payload = {
            'expense_id': expense_id,
            'content': content
        }
        response = requests.post(self.base_url + 'create_comment', data=payload, auth=self.auth)
        return response.json()

    def get_comments(self, expense_id):
        """Get all comments for a specific expense."""
        params = {'expense_id': expense_id}
        response = requests.get(self.base_url + 'get_comments', params=params, auth=self.auth)
        return response.json().get('comments', [])

    def undelete_expense(self, expense_id):
        """Restore a deleted expense by its ID."""
        response = requests.post(self.base_url + f'undelete_expense/{expense_id}', auth=self.auth)
        return response.json()

    def delete_expense(self, expense_id):
        """Delete an expense by its ID."""
        response = requests.post(self.base_url + f'delete_expense/{expense_id}', auth=self.auth)
        return response.json()

    def update_expense(self, expense_id, group_id=None, description=None, cost=None):
        """Update an existing expense."""
        payload = {}
        if group_id is not None:
            payload['group_id'] = group_id
        if description is not None:
            payload['description'] = description
        if cost is not None:
            payload['cost'] = cost

        if not payload:
            return {"error": "No fields provided to update."}

        response = requests.post(self.base_url + f'update_expense/{expense_id}', data=payload, auth=self.auth)
        return response.json()

    def get_expense(self, expense_id):
        """Get details for a single expense by its ID."""
        response = requests.get(self.base_url + f'get_expense/{expense_id}', auth=self.auth)
        return response.json().get('expense', {})

    def get_expenses(self, group_id=None, friend_id=None, dated_after=None, dated_before=None, limit=20):
        """Get a list of expenses with optional filters."""
        params = {
            'group_id': group_id,
            'friend_id': friend_id,
            'dated_after': dated_after,
            'dated_before': dated_before,
            'limit': limit
        }
        # Remove None values so they are not sent as empty params
        params = {k: v for k, v in params.items() if v is not None}

        response = requests.get(self.base_url + 'get_expenses', params=params, auth=self.auth)
        return response.json().get('expenses', [])

    def create_expense(self, description, cost, group_id, payer_id, participants, currency_code='INR'):
        """Create a new expense in Splitwise"""
        payload = {
            'cost': str(cost),
            'description': description,
            'group_id': str(group_id),
        'currency_code': currency_code,
        }

        # Ensure all IDs are strings for consistent comparison
        s_payer_id = str(payer_id)
        s_participants = {str(p) for p in participants}

        num_participants = len(s_participants)
        if num_participants == 0:
            return {'errors': {'base': ['No participants specified for the expense.']}}

        split_amount = round(float(cost) / num_participants, 2)

        # Ensure total owed equals the cost to avoid rounding errors
        total_owed = split_amount * num_participants
        remainder = round(float(cost) - total_owed, 2)

        user_index = 0
        # Add payer to the expense. Payer is always user 0.
        payload[f'users__{user_index}__user_id'] = s_payer_id
        payload[f'users__{user_index}__paid_share'] = str(cost)

        # Determine payer's owed share
        if s_payer_id in s_participants:
            payload[f'users__{user_index}__owed_share'] = str(split_amount + remainder)
        else:
            payload[f'users__{user_index}__owed_share'] = "0.00"
        user_index += 1

        # Add other participants
        for user_id in s_participants:
            if user_id == s_payer_id:
                continue  # Skip payer, already handled
            payload[f'users__{user_index}__user_id'] = user_id
            payload[f'users__{user_index}__paid_share'] = "0.00"
            payload[f'users__{user_index}__owed_share'] = str(split_amount)
            user_index += 1

        response = requests.post(self.base_url + 'create_expense', data=payload, auth=self.auth)
        return response.json()    

    def undelete_group(self, group_id):
        """Restore a deleted group by its ID."""
        response = requests.post(self.base_url + f'undelete_group/{group_id}', auth=self.auth)
        return response.json()

    def delete_group(self, group_id):
        """Delete a group by its ID."""
        response = requests.post(self.base_url + f'delete_group/{group_id}', auth=self.auth)
        return response.json()

    def remove_user_from_group(self, group_id, user_id):
        """Remove a user from a group."""
        payload = {
            'group_id': group_id,
            'user_id': user_id,
        }
        response = requests.post(self.base_url + 'remove_user_from_group', data=payload, auth=self.auth)
        return response.json()

    def add_user_to_group(self, group_id, user_id=None, first_name=None, last_name=None, email=None):
        """Add a user to a group."""
        payload = {
            'group_id': group_id,
        }
        if user_id:
            payload['user_id'] = user_id
        elif email:
            payload['email'] = email
            if first_name:
                payload['first_name'] = first_name
            if last_name:
                payload['last_name'] = last_name
        else:
            return {"error": "Either user_id or email is required."}

        response = requests.post(self.base_url + 'add_user_to_group', data=payload, auth=self.auth)
        return response.json()

    def create_group(self, name, users, group_type="other", simplify_by_default=True):
        """Create a new group with a list of users."""
        payload = {
            'name': name,
            'group_type': group_type,
            'simplify_by_default': simplify_by_default
        }

        for i, user in enumerate(users):
            if user.get('id'):
                payload[f'users__{i}__user_id'] = user['id']
            elif user.get('email'):
                payload[f'users__{i}__email'] = user['email']
            if user.get('first_name'):
                payload[f'users__{i}__first_name'] = user['first_name']
            if user.get('last_name'):
                payload[f'users__{i}__last_name'] = user['last_name']

        response = requests.post(self.base_url + 'create_group', data=payload, auth=self.auth)
        return response.json()

    def get_group(self, group_id):
        """Get details for a specific group by ID"""
        res = requests.get(self.base_url + f'get_group/{group_id}', auth=self.auth)
        return res.json().get('group', {})

    def get_groups(self):
        """Get all groups with detailed member information"""
        res = requests.get(self.base_url + 'get_groups', auth=self.auth)
        groups = res.json().get('groups', [])
        
        # Format groups data consistently
        formatted_groups = []
        for group in groups:
            formatted_group = {
                'id': group['id'],
                'name': group['name'],
                'members': self._format_members(group.get('members', []))
            }
            formatted_groups.append(formatted_group)
        return formatted_groups
    
    def update_user(self, user_id, first_name=None, last_name=None, email=None, password=None, locale=None, default_currency=None):
        """Update details for a specific user by ID"""
        payload = {}
        if first_name is not None:
            payload['first_name'] = first_name
        if last_name is not None:
            payload['last_name'] = last_name
        if email is not None:
            payload['email'] = email
        if password is not None:
            payload['password'] = password
        if locale is not None:
            payload['locale'] = locale
        if default_currency is not None:
            payload['default_currency'] = default_currency

        if not payload:
            return {"error": "No update information provided."}

        response = requests.post(self.base_url + f'update_user/{user_id}', data=payload, auth=self.auth)
        return response.json()

    def get_user(self, user_id):
        """Get details for a specific user by ID"""
        res = requests.get(self.base_url + f'get_user/{user_id}', auth=self.auth)
        return res.json().get('user', {})

    def get_current_user(self):
        """Get the current authenticated user's details"""
        res = requests.get(self.base_url + 'get_current_user', auth=self.auth)
        return res.json().get('user', {})

    def create_friends(self, friends):
        """Create multiple friends at once."""
        payload = {}
        for i, friend in enumerate(friends):
            if 'email' in friend:
                payload[f'friends__{i}__email'] = friend['email']
            if 'first_name' in friend:
                payload[f'friends__{i}__first_name'] = friend['first_name']
            if 'last_name' in friend:
                payload[f'friends__{i}__last_name'] = friend['last_name']

        if not payload:
            return {"error": "No friends information provided."}

        response = requests.post(self.base_url + 'create_friends', data=payload, auth=self.auth)
        return response.json()

    def create_friend(self, user_email, user_first_name=None, user_last_name=None):
        """Create a new friend"""
        payload = {
            'user_email': user_email
        }
        if user_first_name:
            payload['user_first_name'] = user_first_name
        if user_last_name:
            payload['user_last_name'] = user_last_name

        response = requests.post(self.base_url + 'create_friend', data=payload, auth=self.auth)
        return response.json()

    def delete_friend(self, friend_id):
        """Delete a friend by their ID"""
        response = requests.post(self.base_url + f'delete_friend/{friend_id}', auth=self.auth)
        return response.json()

    def get_friend(self, friend_id):
        """Get details for a specific friend by ID"""
        res = requests.get(self.base_url + f'get_friend/{friend_id}', auth=self.auth)
        return res.json().get('friend', {})

    def get_friends(self):
        """Get all friends with their details"""
        res = requests.get(self.base_url + 'get_friends', auth=self.auth)
        friends = res.json().get('friends', [])
        
        formatted_friends = []
        for friend in friends:
            formatted_friends.append({
                'id': friend['id'],
                'name': self._format_name(friend),
                'email': friend.get('email', ''),
                'balance': self._format_balances(friend.get('balance', []))
            })
        return formatted_friends

    def _format_balances(self, balances):
        """Format balance information"""
        formatted = []
        for bal in balances:
            formatted.append({
                'amount': float(bal.get('amount', 0)),
                'currency': bal.get('currency_code', 'USD')
            })
        return formatted




    def get_group_members(self, group_id):
        """Get members of a specific group"""
        groups = self.get_groups()
        for group in groups:
            if str(group['id']) == str(group_id):
                return group['members']
        return []

    def _format_members(self, members):
        """Format member data consistently"""
        formatted_members = []
        for member in members:
            formatted_members.append({
                'id': member['id'],
                'name': self._format_name(member)
            })
        return formatted_members

    def _format_name(self, user_data):
        """Format user name consistently"""
        first = user_data.get('first_name', '')
        last = user_data.get('last_name', '')
        return f"{first} {last}".strip()