from decimal import Decimal

from django.test import TestCase

from .models import FloorPlan, MediaFile, Project, media_file_path, plan_file_path


class ProjectModelTest(TestCase):
    def setUp(self):
        self.test_data = {
            "title": "Test House",
            "address": "Test Str. 12",
            "price": "123000",
            "rooms": 5,
            "square": "120",
            "land_area": "300",
            "description": "Modern Test house",
            "details": "Details about house",
            "equipment": "Balkon, Terrass",
        }
        self.project = Project.objects.create(**self.test_data)

    def test_project_instance(self):
        project = Project.objects.get(id=1)

        self.assertEqual(project.title, self.test_data["title"])
        self.assertEqual(project.price, Decimal(self.test_data["price"]))
        self.assertEqual(project.description, self.test_data["description"])

    def test_media_file_path(self):
        test_instance = MediaFile(project=self.project)
        filename = "image.jpeg"
        path = media_file_path(test_instance, filename)

        self.assertEqual(path, "project_1/media/image.jpeg")

    def test_plan_file_path(self):
        test_instance = FloorPlan(project=self.project)
        filename = "plan.png"
        path = plan_file_path(test_instance, filename)

        self.assertEqual(path, "project_1/floor_plan/plan.png")
