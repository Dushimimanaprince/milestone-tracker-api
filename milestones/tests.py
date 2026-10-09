import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import Milestone


class MilestoneAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('milestone-collection')

    def test_create_milestone_success(self):
        """US-01: Valid payload returns 201 Created and PENDING status"""
        payload = {
            "title": "Configured CI/CD",
            "description": "Added GitHub Actions workflow",
            "student_id": "AMALI-2026-01"
        }
        response = self.client.post(
            self.url,
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["status"], "PENDING")
        self.assertEqual(data["title"], "Configured CI/CD")
        self.assertTrue(Milestone.objects.filter(id=data["id"]).exists())

    def test_create_milestone_missing_required_fields(self):
        """US-01: Missing required fields returns 400 Bad Request"""
        invalid_payload = {"description": "Missing title and student_id"}
        response = self.client.post(
            self.url,
            data=json.dumps(invalid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_list_milestones_empty(self):
        """US-02: Returns 200 and empty list when no milestones exist"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 0)
        self.assertEqual(response.json()["milestones"], [])

    def test_list_milestones_with_records(self):
        """US-02: Returns 200 and array with stored milestones"""
        Milestone.objects.create(
            title="Setup Repo",
            description="Sprint 0 work",
            student_id="AMALI-2026-01"
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["milestones"][0]["title"], "Setup Repo")