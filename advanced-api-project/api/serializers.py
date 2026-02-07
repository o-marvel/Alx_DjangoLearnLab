from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

# ---------------------------------------------------
# BookSerializer
# ---------------------------------------------------
# This serializer converts Book model objects into JSON
# and also converts JSON into Book model objects.
#
# It handles:
# - Validation
# - Serialization
# - Deserialization
# - Data conversion for APIs
# ---------------------------------------------------
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # "__all__" means all fields in the Book model are serialized
        # Fields included:
        # id, title, publication_year, author
        fields = "__all__"

    # ---------------------------------------------------
    # Custom Field Validation
    # ---------------------------------------------------
    # This method validates the publication_year field.
    # It prevents saving a book with a future year.
    #
    # Example:
    # 2035 → ❌ Invalid
    # 2020 → ✅ Valid
    # ---------------------------------------------------
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# ---------------------------------------------------
# AuthorSerializer
# ---------------------------------------------------
# This serializer represents the Author model.
#
# It includes:
# - Author name
# - All books written by the author (nested serialization)
# ---------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer:
    # This field dynamically loads all books related to the author
    #
    # many=True → because one author has many books
    # read_only=True → books cannot be created via AuthorSerializer
    #
    # Uses related_name="books" from the Book model:
    # author.books.all()
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
