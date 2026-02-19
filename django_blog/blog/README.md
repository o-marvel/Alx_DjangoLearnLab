## Blog CRUD Features

- Users can view all posts.
- Users can view individual post details.
- Authenticated users can create posts.
- Authors can edit and delete their own posts.
- Unauthorized users cannot modify posts they do not own.
- All views use Django Class-Based Views.
- Permissions handled via LoginRequiredMixin and UserPassesTestMixin.

## Comment System

- Users can view comments on each blog post.
- Only authenticated users can add comments.
- Comment authors can edit or delete their comments.
- Permissions are enforced using Django mixins.
- Comments are displayed under each post detail page.

## Tagging System

- Posts can have multiple tags.
- Tags are selectable when creating or editing posts.
- Clicking a tag displays all posts associated with that tag.

## Search System

- Users can search posts by title, content, or tag.
- Search uses Django Q objects for advanced filtering.
- Results are displayed on a dedicated search page.
