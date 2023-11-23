from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase, Client


from kitchen_restaurant.admin import CookAdmin, DishAdmin
from kitchen_restaurant.models import Cook, Dish, DishType


class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )

        self.client.force_login(self.admin_user)

        self.site = AdminSite()
        self.cook = Cook.objects.create(
            username="test_user",
            password="test123456",
            first_name="Test",
            last_name="User",
            email="test@example.com",
            years_of_experience=2,
        )
        self.dish_type = DishType.objects.create(name="TestType")
        self.dish = Dish.objects.create(
            name="TestDish",
            description="Test description",
            price=10.99,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_dish_admin_customization(self):
        dish_admin = DishAdmin(Dish, self.site)
        self.assertEqual(
            dish_admin.list_display,
            ("name", "price", "description")
        )
        self.assertEqual(dish_admin.search_fields, ("name",))
