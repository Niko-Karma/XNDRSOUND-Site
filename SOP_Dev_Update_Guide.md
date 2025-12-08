# Developer Guide: Updating the Gallery

**Goal:** Update `gallery.json` with new images provided by the client.

## File Location
`static/data/gallery.json`

## Process
1.  **Open the JSON file** in your editor.
2.  **Add a new object** to the array for each new image.
3.  **Required Fields**:
    *   `id`: unique integer (increment from the last one)
    *   `url`: The Cloudinary link provided by the client.
    *   `title`: Display title for the image.
    *   `tags`: Array of strings.
        *   Use `"featured"` to make it appear in the featured filter/highlight.
        *   Common tags: `studio`, `urban`, `concert`, `promo`.

## Example Snippet

```json
  {
    "id": 7,
    "url": "https://res.cloudinary.com/your-cloud/image/upload/v12345/sample.jpg",
    "title": "New Album Cover",
    "tags": ["promo", "featured"],
    "width": 1000,
    "height": 1000
  }
```

## Deployment
1.  Commit and push the changes to `gallery.json`.
2.  The site will automatically update (if CI/CD is set up) or pull changes on the server.
