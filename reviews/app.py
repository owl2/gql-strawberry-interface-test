from typing import List
 
import strawberry
from strawberry.federation.schema_directives import Requires, External
 
 
@strawberry.type
class Review:
    id: int
    body: str
    book: 'Book'
 
 
def get_reviews(root: "Book") -> List[Review]:
    return [
        Review(id=id_, body=f"A review for {root.id}")
        for id_ in range(root.reviews_count)
    ]
 
 
# @strawberry.federation.type(keys=["id"])
# @strawberry.federation.interface_object(keys=["id"], directives=[External()])
@strawberry.federation.interface_object(keys=["id"])
class Book:
    id: strawberry.ID
    reviews_count: int
    reviews: List[Review] = strawberry.field(resolver=get_reviews)
 
    @classmethod
    def resolve_reference(cls, id: strawberry.ID, reviews_count: int) -> 'Book':
        # here we could fetch the book from the database
        # or even from an API
        return Book(id=strawberry.ID("1"), reviews_count=3)


def get_all_reviews() -> List[Review]:
    return [Review(
                    id=strawberry.ID("1"), 
                    body="Blablabla", 
                    book=Book(id=strawberry.ID("1"), reviews_count=3),
                    )]

 
@strawberry.type
class Query:
    _hi: str = strawberry.field(resolver=lambda: "Hello World!")
    all_reviews: List[Review] = strawberry.field(resolver=get_all_reviews)
 
 
schema = strawberry.federation.Schema(
    query=Query, types=[Book, Review], enable_federation_2=True
)

