from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@x.com', team=team)
        self.assertEqual(str(user), 'U')
    def test_activity_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@x.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2025-01-01')
        self.assertIn('Run', str(activity))
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='desc', suggested_for='all')
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T3', description='d3')
        user = User.objects.create(name='U3', email='u3@x.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=42)
        self.assertIn('U3', str(lb))

class ApiRootTest(TestCase):
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
