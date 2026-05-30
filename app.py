from datetime import datetime
import json
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

DATA_FILE = "courses.json"
VALID_STATUSES = ["Not Started", "In Progress", "Completed"]


def initialize_json_file():
    """Create courses.json automatically if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def read_courses():
    """Read all courses from the JSON file."""
    try:
        initialize_json_file()

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        raise Exception("The JSON file is corrupted or incorrectly formatted.")

    except OSError:
        raise Exception("Could not read from the data file.")


def write_courses(courses):
    """Write all courses to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(courses, file, indent=4)

    except OSError:
        raise Exception("Could not write to the data file.")


def get_next_id(courses):
    """Generate the next course ID, starting from 1."""
    if not courses:
        return 1

    return max(course["id"] for course in courses) + 1


def validate_course_data(data):
    """Validate required fields and status value."""
    required_fields = ["name", "description", "target_date", "status"]

    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"

    if data["status"] not in VALID_STATUSES:
        return False, (
            "Invalid status. Must be one of: "
            "Not Started, In Progress, Completed"
        )

    try:
        datetime.strptime(data["target_date"], "%Y-%m-%d")
    except ValueError:
        return False, "Invalid target_date format. Use YYYY-MM-DD."

    return True, None


@app.route("/api/courses", methods=["POST"])
def add_course():
    """Add a new course."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be JSON."}), 400

        is_valid, error_message = validate_course_data(data)

        if not is_valid:
            return jsonify({"error": error_message}), 400

        courses = read_courses()

        new_course = {
            "id": get_next_id(courses),
            "name": data["name"],
            "description": data["description"],
            "target_date": data["target_date"],
            "status": data["status"],
            "created_at": datetime.now().isoformat()
        }

        courses.append(new_course)
        write_courses(courses)

        return jsonify(new_course), 201

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses", methods=["GET"])
def get_courses():
    """Get all courses."""
    try:
        courses = read_courses()
        return jsonify(courses), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500

@app.route("/api/courses/stats", methods=["GET"])
def get_course_statistics():
    """
    Return summary statistics about all courses.
    """
    try:
        courses = read_courses()

        stats = {
            "total_courses": len(courses),
            "status_counts": {
                "Not Started": 0,
                "In Progress": 0,
                "Completed": 0
            }
        }

        for course in courses:
            status = course.get("status")

            if status in stats["status_counts"]:
                stats["status_counts"][status] += 1

        return jsonify(stats), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500
        
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    """Get a specific course by ID."""
    try:
        courses = read_courses()

        for course in courses:
            if course["id"] == course_id:
                return jsonify(course), 200

        return jsonify({"error": "Course not found."}), 404

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    """Update an existing course."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be JSON."}), 400

        courses = read_courses()

        for course in courses:
            if course["id"] == course_id:
                updated_course = {
                    "name": data.get("name", course["name"]),
                    "description": data.get("description", course["description"]),
                    "target_date": data.get(
                        "target_date",
                        course["target_date"]
                    ),
                    "status": data.get("status", course["status"])
                }

                is_valid, error_message = validate_course_data(updated_course)

                if not is_valid:
                    return jsonify({"error": error_message}), 400

                course.update(updated_course)
                write_courses(courses)

                return jsonify(course), 200

        return jsonify({"error": "Course not found."}), 404

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    """Delete a course by ID."""
    try:
        courses = read_courses()

        for course in courses:
            if course["id"] == course_id:
                courses.remove(course)
                write_courses(courses)

                return jsonify({
                    "message": "Course deleted successfully."
                }), 200

        return jsonify({"error": "Course not found."}), 404

    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    initialize_json_file()
    app.run(debug=True)