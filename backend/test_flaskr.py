import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import cleanup_db, setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = f"postgresql://postgres:postgres@localhost:5432/{self.database_name}"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        # Drop the database after each test to use the specific test data passed in during setup
        cleanup_db(self.app, self.database_path)

    # TODO: Write at least one test for each test for successful operation and for expected errors.

    # TODO: Write 2 tests for the GET /questions endpoint
    # TODO: Write 2 tests for the GET /categories endpoint
    # TODO: Write 2 tests for the DELETE /questions/<int:question_id> endpoint
    # TODO: Write 2 tests for the POST /questions endpoint
    # TODO: Write 2 tests for the POST /categories/<int:category_id>/questions endpoint
    # TODO: Write 2 tests for the POST /questions endpoint search
    # TODO: Write 2 tests for the POST /quizzes endpoint


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
