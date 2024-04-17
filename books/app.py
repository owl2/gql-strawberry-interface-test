from typing import List
 
import strawberry
from strawberry.federation.schema_directives import Requires, External
 
 
# @strawberry.federation.type(keys=["id"])
# @strawberry.federation.interface(keys=["id"], directives=[External()])
@strawberry.federation.interface(keys=["id"],)
class Book:
    id: strawberry.ID
    title: str


    @classmethod
    def resolve_reference(cls, id: strawberry.ID, title: str) -> 'Book':
        # here we could fetch the book from the database
        # or even from an API
        return Book(id=id, title=title)
 
 
def get_all_books() -> List[Book]:
    return Book(id=strawberry.ID("1"), title="The Dark Tower")


 
@strawberry.type
class Query:
    all_books: List[Book] = strawberry.field(resolver=get_all_books)

    @strawberry.field
    def book(self) -> Book:
        return Book(id=strawberry.ID("1"), title='A title')
 
 
schema = strawberry.federation.Schema(
    query=Query,
    types=[Book], 
    enable_federation_2=True)

