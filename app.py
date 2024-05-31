from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store blog posts
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post.", "author": "John Doe"},
    {"id": 2, "title": "Second Post", "content": "This is the second post.", "author": "Jane Smith"}
]

# Helper function to find a post by id
def find_post(post_id):
    return next((post for post in posts if post['id'] == post_id), None)

# Endpoint to retrieve all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Endpoint to retrieve a single post by id
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = find_post(post_id)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post)

# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

# Endpoint to update a post by id
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = find_post(post_id)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    updated_data = request.get_json()
    post.update(updated_data)
    return jsonify(post)

# Endpoint to delete a post by id
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = find_post(post_id)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    posts.remove(post)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

