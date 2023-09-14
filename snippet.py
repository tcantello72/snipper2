"""
    created by Toby Cantello
    created on 9/14/23
    last updated on 9/14/23
"""
from flask import abort, make_response

SNIPPET = {
  "1": {
    "id": 1,
    "language": "Python",
    "code": "print('Hello, World!')"
  },

  "2": {
    "id": 2,
    "language": "Python",
    "code": "def add(a, b):\n    return a + b"
  },

  "3": {
    "id": 3,
    "language": "Python",
    "code": "class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n\n    def area(self):\n        return 3.14 * self.radius ** 2"
  },

  "4": {
    "id": 4,
    "language": "JavaScript",
    "code": "console.log('Hello, World!');"
  },

  "5": {
    "id": 5,
    "language": "JavaScript",
    "code": "function multiply(a, b) {\n    return a * b;\n}"
  },

  "6": {
    "id": 6,
    "language": "JavaScript",
    "code": "const square = num => num * num;"
  },

  "7": {
    "id": 7,
    "language": "Java",
    "code": "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"
  },

  "8": {
    "id": 8,
    "language": "Java",
    "code": "public class Rectangle {\n    private int width;\n    private int height;\n\n    public Rectangle(int width, int height) {\n        this.width = width;\n        this.height = height;\n    }\n\n    public int getArea() {\n        return width * height;\n    }\n}"
  }
}

# (GET) Read all Snippets
def read_all():
    return list(SNIPPET.values())

# (GET) Read one snippet by ID
def read_one(id):
    if id in SNIPPET:
        return SNIPPET[id]
    else:
        abort(
            404, f"Snippet with ID {id} not found"
        )

# (POST) Create a new snippet
def create(snippet):
    id = snippet.get("id")
    language = snippet.get("language")
    code = snippet.get("code")

    if id not in SNIPPET:
        SNIPPET[id] = {
            "id": id,
            "language": language,
            "code": code,
        }
        return SNIPPET[id], 201
    else:
        abort(
            406,
            f"Snippet with ID {id} already exists",
        )

# (PUT) Update a snippet
def update(id, snippet):
    if id in SNIPPET:
        SNIPPET[id]["id"] = snippet.get("id")
        SNIPPET[id]["language"] = snippet.get("language")
        SNIPPET[id]["code"] = snippet.get("code")
        return SNIPPET[id]
    else:
        abort(
            404,
            f"Snippet with ID {id} not found"
        )

# (DELETE) Delete a snippet
def delete(id):
    if id in SNIPPET:
        del SNIPPET[id]
        return make_response(
            f"Snippet with ID {id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Snippet with ID {id} not found"
        )