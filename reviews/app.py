from __future__ import annotations
from typing import List

import strawberry


def get_reviews(root: strawberry.Parent[Reviewable]) -> List[Review]:
    return [
        Review(id=id_, body=f"A review for {root.id}")
        for id_ in range(root.reviews_count)
    ]


@strawberry.federation.interface_object(keys=["id"])
class Reviewable:
    id: strawberry.ID
    reviews: List[Review] = strawberry.field(resolver=get_reviews)
    reviews_count: int = 10


@strawberry.type
class Review:
    id: int
    body: str


schema = strawberry.federation.Schema(
    types=[Reviewable, Review], enable_federation_2=True
)
