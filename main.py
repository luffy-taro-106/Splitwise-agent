from operator import ge
import google.generativeai as genai
from config import GEMINI_API_KEY
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import StructuredTool
from tools import *
from prompts import *

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

# Define tools with proper descriptions
splitwise_tools = [
    StructuredTool.from_function(
        name="GetCurrentUser",
        func=get_current_user,
        description=get_current_user_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetUser",
        func=get_user,
        args_schema=GetUserInput,
        description=get_user_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetCurrencies",
        func=get_currencies,
        description=get_currencies_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetNotifications",
        func=get_notifications,
        args_schema=GetNotificationsInput,
        description=get_notifications_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="DeleteComment",
        func=delete_comment,
        args_schema=DeleteCommentInput,
        description=get_delete_comment_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="CreateComment",
        func=create_comment,
        args_schema=CreateCommentInput,
        description=get_create_comment_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetComments",
        func=get_comments,
        args_schema=GetCommentsInput,
        description=get_comments_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="UndeleteExpense",
        func=undelete_expense,
        args_schema=UndeleteExpenseInput,
        description=get_undelete_expense_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="DeleteExpense",
        func=delete_expense,
        args_schema=DeleteExpenseInput,
        description=get_delete_expense_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="UpdateExpense",
        func=update_expense,
        args_schema=UpdateExpenseInput,
        description=get_update_expense_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetExpense",
        func=get_expense,
        args_schema=GetExpenseInput,
        description=get_expense_prompt,
        return_direct=False,
    ),

    StructuredTool.from_function(
        name="UpdateUser",
        func=update_user,
        args_schema=UpdateUserInput,
        description=get_update_user_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="CreateFriends",
        func=create_friends,
        args_schema=CreateFriendsInput,
        description=create_friends_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="DeleteFriend",
        func=delete_friend,
        args_schema=DeleteFriendInput,
        description=delete_friend_prompt,
        return_direct=False,
    ),
 
    StructuredTool.from_function(
        name="UndeleteGroup",
        func=undelete_group,
        args_schema=UndeleteGroupInput,
        description=undelete_group_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="DeleteGroup",
        func=delete_group,
        args_schema=DeleteGroupInput,
        description=delete_group_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="RemoveUserFromGroup",
        func=remove_user_from_group,
        args_schema=RemoveUserFromGroupInput,
        description=remove_user_from_group_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="AddUserToGroup",
        func=add_user_to_group,
        args_schema=AddUserToGroupInput,
        description=add_user_to_group_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="CreateGroup",
        func=create_group,
        args_schema=CreateGroupInput,
        description=create_group_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetGroup",
        func=get_group,
        args_schema=GetGroupInput,
        description=get_group_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetGroups",
        func=get_groups,
        description=get_groups_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetMembers",
        func=get_members,
        description=get_members_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetBalances",
        func=get_balances,
        description=get_balances_prompt,
        return_direct=False,
    ),
    StructuredTool.from_function(
        func=add_expense,
        name="AddExpense",
        description=add_expense_prompt,
        args_schema=AddExpenseInput,
        return_direct=False,
    ),
    StructuredTool.from_function(
        name="GetFriends",
        func=get_friends,
        description=get_friends_prompt,
        return_direct=False,
    )
]

agent_executor = initialize_agent(
    tools=splitwise_tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,
    agent_kwargs={
        "system_message": system_prompt
    }
)

# Keep the command-line interface when run directly
if __name__ == '__main__':
    print("🤖 Splitwise Assistant Ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"Agent: {response['output']}")
        except Exception as e:
            print(f"Error: {str(e)}")