#!/usr/bin/python3
"""This class tests the FileStorage module"""
from unittest import TestCase, main
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
import models


class TestStorage_Type(TestCase):
    """Test the file storage type"""

    def test_storage_type(self):
        """Test the FileStorage type

        NOTES:
        Normally you can't access FileStorage._FileStorage__objects.
        We are just testing out the types for now so it works
        The code specifically tests for dict type
        """
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_file_path_type(self):
        """Test if the file path is a string type"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_fileStorage_instance(self):
        """Test the instance of FileStorage"""
        self.assertIsInstance(models.storage, FileStorage)

    def test_fileStorage_instance_type(self):
        """Test the type of FileStorage instance"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_Load(TestCase):
    """This class mainly tests the loading of all data"""

    def test_load_single_instance(self):
        """Test the loading of single a instance
        NOTES:
            This also just loads a new FileStorage instance
        """
        user_model = User()
        self.assertIn("User.{}".format(user_model.id),
                      models.storage.all().keys())

    def test_load_multiple_instances(self):
        """Test the loading of multiple instances (literally all of them)"""
        base_model = BaseModel()
        user_model = User()
        state_model = State()
        review_model = Review()
        city_model = City()
        place_model = Place()
        self.assertIn("BaseModel.{}".format(base_model.id),
                      models.storage.all().keys())
        self.assertIn("State.{}".format(state_model.id),
                      models.storage.all().keys())
        self.assertIn("User.{}".format(user_model.id),
                      models.storage.all().keys())
        self.assertIn("Review.{}".format(review_model.id),
                      models.storage.all().keys())
        self.assertIn("City.{}".format(city_model.id),
                      models.storage.all().keys())
        self.assertIn("Place.{}".format(place_model.id),
                      models.storage.all().keys())

    def test_load_instance_with_args(self):
        """Test all method with args"""
        with self.assertRaises(TypeError):
            models.storage.all("fetch")


class TestFileStorage_New(TestCase):
    """Test the new method for FileStorage"""

    def test_new_with_multiple_args(self):
        """Test if (new) method accepts multiple args"""
        with self.assertRaises(TypeError):
            models.storage.new("Roger", "Markus")

    def test_new_with_no_objects(self):
        """Test if (new) method will work with no object"""
        with self.assertRaises(AttributeError):
            models.storage.new("dummy_args")


class TestFileStorage_Save(TestCase):
    """Test the save method of FileStorage"""

    def test_save_instance_with_args(self):
        """Tests the save function with args"""
        with self.assertRaises(TypeError):
            models.storage.save("New Object")

    def test_single_save_instance(self):
        """Test the single instance of save method
        Then load the file to check if contents were written
        """
        base_model = BaseModel()
        base_model.save()
        self.assertIn("BaseModel.{}".format(base_model.id),
                      models.storage.all().keys())

    def test_multiple_save_instances(self):
        """Test the multiple instances of save method
        Then load the file to check if contents were written
        """
        base_model = BaseModel()
        user_model = User()
        state_model = State()
        review_model = Review()
        city_model = City()
        place_model = Place()

        # NOTE: This doesn't write to the actual file, rather in memory
        # Meaning I would need to manually create the file in the test
        base_model.save()
        user_model.save()
        state_model.save()
        review_model.save()
        city_model.save()
        place_model.save()

        self.assertIn("BaseModel.{}".format(base_model.id),
                      models.storage.all().keys())
        self.assertIn("State.{}".format(state_model.id),
                      models.storage.all().keys())
        self.assertIn("User.{}".format(user_model.id),
                      models.storage.all().keys())
        self.assertIn("Review.{}".format(review_model.id),
                      models.storage.all().keys())
        self.assertIn("City.{}".format(city_model.id),
                      models.storage.all().keys())
        self.assertIn("Place.{}".format(place_model.id),
                      models.storage.all().keys())


class TestFileStorage_Reload(TestCase):
    """Test the reload method of FileStorage"""

    def test_reload_instance_with_args(self):
        """Tests the save function with args"""
        with self.assertRaises(TypeError):
            models.storage.reload("New Object")

    def test_reload_save_instance(self):
        """Test the single instance of save & reloading
        Then check if contents were written
        """
        base_model = BaseModel()
        user_model = User()
        base_model.save()
        self.assertIn("BaseModel.{}".format(base_model.id),
                      models.storage.all().keys())
        user_model.save()
        models.storage.reload()
        self.assertIn("BaseModel.{}".format(base_model.id),
                      models.storage.all().keys())
        self.assertIn("User.{}".format(user_model.id),
                      models.storage.all().keys())

    def test_multiple_save_instances(self):
        """Test the multiple instances of save & reload
        Then check if contents were written
        """
        base_model = BaseModel()
        user_model = User()
        state_model = State()
        review_model = Review()
        city_model = City()
        place_model = Place()

        # NOTE: This doesn't write to the actual file, rather in memory
        # Meaning I would need to manually create the file in the test
        base_model.save()
        user_model.save()
        state_model.save()

        self.assertIn("BaseModel.{}".format(base_model.id),
                      models.storage.all().keys())
        self.assertIn("State.{}".format(state_model.id),
                      models.storage.all().keys())
        self.assertIn("User.{}".format(user_model.id),
                      models.storage.all().keys())
        models.storage.reload()

        review_model.save()
        city_model.save()
        place_model.save()

        models.storage.reload()
        self.assertIn("Review.{}".format(review_model.id),
                      models.storage.all().keys())
        self.assertIn("City.{}".format(city_model.id),
                      models.storage.all().keys())
        self.assertIn("Place.{}".format(place_model.id),
                      models.storage.all().keys())


if __name__ == "__main__":
    main()
