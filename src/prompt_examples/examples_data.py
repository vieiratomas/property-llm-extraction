from src.models.schemas import Property

examples = [
    (
        "Beautiful two-bedroom, two-bathroom apartment located in downtown Chicago on the 15th floor, with elevator access and a secure parking spot.",
        Property(
            location="downtown Chicago",
            number_of_bedrooms=2,
            number_of_bathrooms=2,
            floor_number=15,
            elevator_access=True,
            parking=True
        ),
    ),
    (
        "Cozy cabin in the woods with one bedroom and a bathroom but no garage. Located near Lake Tahoe.",
        Property(
            location="near Lake Tahoe",
            number_of_bedrooms=1,
            number_of_bathrooms=1,
            floor_number=None,
            elevator_access=None,
            parking=False
        ),
    ),
    (
        "Luxury villa with multiple balconies, located in Beverly Hills. Comes with private parking and exclusive amenities.",
        Property(
            location="Beverly Hills",
            number_of_bedrooms=None,
            number_of_bathrooms=None,
            floor_number=None,
            elevator_access=None,
            parking=True
        ),
    ),
    (
        "The weather is sunny and the beach is crowded today.",
        Property(
            location=None,
            number_of_bedrooms=None,
            number_of_bathrooms=None,
            floor_number=None,
            elevator_access=None,
            parking=None
        ),
    ),
    (
        "The latest model of this car features an innovative parking assistant.",
        Property(
            location=None,
            number_of_bedrooms=None,
            number_of_bathrooms=None,
            floor_number=None,
            elevator_access=None,
            parking=None
        ),
    ),
]
