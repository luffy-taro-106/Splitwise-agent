from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class DeleteCommentInput(BaseModel):
    comment_id: int = Field(..., description="The ID of the comment to delete.")

def delete_comment(comment_id: int):
    """Delete a comment from an expense by its ID."""
    api = SplitwiseAPI()
    return api.delete_comment(comment_id)
