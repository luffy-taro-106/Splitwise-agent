get_current_user_prompt = """Get the details of the currently authenticated user. Use this when:
        - User asks about themselves (e.g., 'who am I?', 'my details', 'my info')
        - You need the current user's ID for any operation (expenses, groups, etc.)
        - User refers to themselves as 'me' or 'my' in any context
        No input needed as this automatically fetches the logged-in user.
        Returns: Complete user object with id, name, email, and other details.
        Note: Always call this first when user references themselves before proceeding with other operations."""

get_user_prompt = """Get details for a specific user. Use this when:
        - to search for any user first go through get_friends and get_groups and try to get there id from there 
        - You need information about another user (when mentioned by name/email)
        - User asks 'who is [name]?' or 'get details for [email]'
        - You need to verify a user exists before adding to group/expense
        Input: Either:
        1) User's numeric ID (preferred)
        2) User's email address
        3) First name + last name (if unique)
        Automation: If only name/email is provided, first search all friends/groups to find matching user ID.
        Returns: Complete user object or error if not found."""

get_friends_prompt = """Get all friends of the current user. Use this when:
        - User mentions 'friends' without specifying IDs
        - You need to select friends for group/expense creation
        - User asks 'who are my friends?' or 'list my friends'
        No input needed.
        Returns: List of all friend objects with id, name, email.
        Important: Always use this to resolve friend names to IDs automatically."""

get_currencies_prompt = """Get all supported currencies. Use this when:
        - User asks about currencies (e.g., 'what currencies are supported?')
        - You need to validate a currency code
        - An expense is being created without specified currency
        No input needed.
        Returns: List of currency objects with code, name, symbol.
        Note: Default to USD if no currency specified."""

get_notifications_prompt = """Get user notifications. Use this when:
        - User asks 'any updates?' or 'show my notifications'
        - You need to alert user about recent activity
        Input: Optional number to retrieve (default: 10 latest).
        Returns: List of notification objects with type, content, timestamp."""

# Comments Section
get_comments_prompt = """Get all comments for an expense. Use this when:
        - User asks 'show comments for expense [X]'
        - You need to display discussion about an expense
        Input: Expense ID (extract from context if not provided directly).
        Returns: List of comment objects with author, content, timestamps."""

get_create_comment_prompt = """Add comment to an expense. Use this when:
        - User says 'comment on expense [X]: [message]'
        - User asks to add feedback to an expense
        Required Input: 
        - Expense ID (extract from context)
        - Comment content/text
        Returns: New comment object with confirmation."""

get_delete_comment_prompt = """Delete a comment. Use this when:
        - User says 'delete my comment [X]'
        - User wants to remove their own comment
        Required Input: Comment ID (must belong to current user).
        Returns: Success/failure confirmation."""

# Expenses Section
get_expenses_prompt = """Get multiple expenses. Use this when:
        - User asks 'show my recent expenses'
        - You need to display multiple expenses
        Input: Optional filters (date range, amount, group).
        Returns: List of expense objects with full details."""

get_expense_prompt = """Get single expense details. Use this when:
        - User asks 'show expense [X]'
        - You need details of a specific expense
        Required Input: Expense ID (extract from context).
        Returns: Complete expense object."""

add_expense_prompt = """Create new expense. Use this when:
        - User says 'add expense' or 'I paid for [item]'
        - Any expense creation request
        Required Input: Dictionary with:
        - cost (required)
        - description (required)
        - details (date, currency, etc.)
        - participants (auto-resolve names to IDs)
        Automation: 
        1) Resolve participant names to IDs using get_friends/get_groups
        2) Default to current user as payer if unspecified
        3) Default to even split if no ratios specified
        Returns: New expense object."""

get_update_expense_prompt = """Update existing expense. Use this when:
        - User says 'update expense [X] to [new details]'
        Required Input: 
        - Expense ID
        - Changed fields (same structure as creation)
        Returns: Updated expense object."""

get_delete_expense_prompt = """Delete an expense. Use this when:
        - User says 'delete expense [X]'
        Required Input: Expense ID.
        Returns: Confirmation."""

get_undelete_expense_prompt = """Restore deleted expense. Use this when:
        - User says 'undo delete of expense [X]'
        Required Input: Expense ID.
        Returns: Restored expense object."""

# Groups Section
get_groups_prompt = """Get all user's groups. Use this when:
        - User asks 'show my groups' or mentions groups
        No input needed.
        Returns: List of group objects with id, name, members.
        Important: Use this to resolve group names to IDs automatically."""

get_group_prompt = """Get specific group details. Use this when:
        - User asks 'show group [X]'
        Required Input: Group ID or name (auto-resolve name to ID).
        Returns: Complete group object."""

create_group_prompt = """Create new group. Use this when:
        - User says 'create group [name] with [members]'
        Required Input:
        - Group name (required)
        - Members (list of names/emails - auto-resolve to IDs)
        Automation:
        1) Call get_friends to resolve member names to IDs
        2) Include current user automatically
        Returns: New group object."""

get_update_group_prompt = """Update group details. Use this when:
        - User says 'update group [X] name/members'
        Required Input:
        - Group ID
        - Changed fields
        Returns: Updated group object."""

add_user_to_group_prompt = """Add user to group. Use this when:
        - User says 'add [name] to group [X]'
        Required Input:
        - Group ID (or name - auto-resolve)
        - User identifier (name/email - auto-resolve to ID)
        Automation: First call get_friends if needed to resolve user.
        Returns: Updated group object."""

remove_user_from_group_prompt = """Remove user from group. Use this when:
        - User says 'remove [name] from group [X]'
        Required Input:
        - Group ID
        - User ID (auto-resolve from name)
        Returns: Updated group object."""

delete_group_prompt = """Delete group. Use this when:
        - User says 'delete group [X]'
        Required Input: Group ID.
        Returns: Confirmation."""

undelete_group_prompt = """Restore deleted group. Use this when:
        - User says 'undo delete of group [X]'
        Required Input: Group ID.
        Returns: Restored group object."""

# Friends Section
create_friends_prompt = """Add new friends. Use this when:
        - User says 'add friend [email/name]'
        Required Input: List of friend details (email required).
        Automation: Skip already-added friends automatically.
        Returns: List of new friend objects."""

delete_friend_prompt = """Remove friend. Use this when:
        - User says 'remove friend [name]'
        Required Input: Friend ID (auto-resolve from name via get_friends).
        Returns: Confirmation."""

# Balances Section
get_balances_prompt = """Get all balances. Use this when:
        - User asks 'who owes me?'
        - You need to show debt relationships
        No input needed.
        Returns: List of balance objects."""

get_balance_prompt = """Get specific balance. Use this when:
        - User asks 'how much does [X] owe me?'
        Required Input: User ID (auto-resolve from name).
        Returns: Balance details."""

get_update_balance_prompt = """Update balance. Use this when:
        - User wants to manually adjust debts
        Required Input: Balance ID and new amount.
        Returns: Updated balance."""

# Members Section (for group members)
get_members_prompt = """Get group members. Use this when:
        - You need member details for a group
        Required Input: Group ID.
        Returns: List of member objects."""

get_member_prompt = """Get specific member details. Use this when:
        - You need details about one group member
        Required Input: Member ID.
        Returns: Member object."""

get_update_member_prompt = """Update member details. Use this when:
        - User wants to change member settings in group
        Required Input: Member ID and changes.
        Returns: Updated member object."""

# User Management
get_update_user_prompt = """Update user profile. Use this when:
        - User says 'update my profile'
        Required Input: Changed fields.
        Returns: Updated user object."""