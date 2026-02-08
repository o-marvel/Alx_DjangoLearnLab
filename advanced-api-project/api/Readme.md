## API View Configuration

### Public Endpoints
- GET /api/books/  
  Retrieves all books.
- GET /api/books/<id>/  
  Retrieves a single book.

### Protected Endpoints (Authentication Required)
- POST /api/books/create/  
  Creates a new book.
- PUT /api/books/<id>/update/  
  Updates an existing book.
- DELETE /api/books/<id>/delete/  
  Deletes a book.

### Permissions
- Read operations: Public access
- Write operations: Authenticated users only

### Custom Behaviors
- perform_create(): Handles validation and object creation
- perform_update(): Handles update logic
- Built-in filtering and search enabled

### Filtering
- Search by title and author name
- Order by publication year and title

### Security
- DRF permission system
- Authentication enforcement
- API-ready for JWT integration
