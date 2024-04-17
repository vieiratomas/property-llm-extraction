from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class Property(BaseModel):
    """Information about a specific property, including its location, features, and amenities."""

    location: Optional[str] = Field(description="The location of the property")

    type: Optional[str] = Field(
        default=None, description="The type of property, such as 'house', 'apartment', 'condo', etc."
    )

    number_of_bedrooms: Optional[int] = Field(
        default=None, description="The total count of bedrooms in the property. This should be a non-negative integer."
    )
    number_of_bathrooms: Optional[int] = Field(
        default=None, description="The total count of bathrooms in the property, including both full and half bathrooms."
    )
    floor_number: Optional[int] = Field(
        default=None, description="The specific floor on which the property is located, if applicable. For single-story properties, this can be omitted."
    )
    
    elevator_access: Optional[bool] = Field(
        default=None, description="Indicates whether the property can be accessed via an elevator."
    )
    parking: Optional[bool] = Field(
        default=None, description="Indicates whether parking facilities are available at the property."
    )
    air_conditioning: Optional[bool] = Field(
        default=None, description="Whether the property has air conditioning"
    )