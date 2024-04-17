from typing import List

import strawberry


@strawberry.federation.interface(keys=["id"])
class Reviewable:
    id: strawberry.ID


@strawberry.federation.type(
    keys=["id"],
)
class Book(Reviewable):
    title: str


def get_all_books() -> List[Book]:
    return Book(id=strawberry.ID("1"), title="The Dark Tower")


@strawberry.type
class Query:
    all_books: List[Book] = strawberry.field(resolver=get_all_books)

    @strawberry.field
    def book(self) -> Book:
        return Book(id=strawberry.ID("1"), title="A title")

    @strawberry.field
    def reviewable(self) -> Reviewable:
        return Book(id=strawberry.ID("1"), title="A title")


schema = strawberry.federation.Schema(
    query=Query, types=[Book], enable_federation_2=True
)
