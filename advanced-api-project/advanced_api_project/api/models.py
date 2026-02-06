from django.db import models

# ---------------------------------------------------
# Author Model
# ---------------------------------------------------
# This model represents a book author.
# Each author can write multiple books.
# This creates a ONE-TO-MANY relationship:
#   One Author → Many Books
# ---------------------------------------------------
class Author(models.Model):
    # Stores the name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        # Human-readable representation in admin panel and shell
        return self.name


# ---------------------------------------------------
# Book Model
# ---------------------------------------------------
# This model represents a book.
# Each book belongs to ONE author.
# This creates a MANY-TO-ONE relationship:
#   Many Books → One Author
# ---------------------------------------------------
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Year the book was published
    publication_year = models.IntegerField()

    # ForeignKey establishes relationship with Author model
    # on_delete=models.CASCADE:
    #   If an Author is deleted, all their books are deleted too
    #
    # related_name="books":
    #   Allows reverse access like:
    #   author.books.all()
    #
    # This means from an Author object, you can get all their books
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self):
        # Human-readable representation
        return self.title
