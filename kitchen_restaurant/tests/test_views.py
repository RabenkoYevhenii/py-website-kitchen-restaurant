from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen_restaurant.models import DishType, Cook, Dish


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get("kitchen_restaurant:dish-type-list")
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test321"
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="Test Dish Type")

    def test_dish_type_list_view(self):
        url = reverse("kitchen_restaurant:dish-type-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_type_list.html")

    def test_dish_type_detail_view(self):
        url = reverse("kitchen_restaurant:dish-type-detail", kwargs={"pk": self.dish_type.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_type_detail.html")

    def test_dish_type_create_view(self):
        url = reverse("kitchen_restaurant:dish-type-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_type_form.html")

    def test_dish_type_update_view(self):
        url = reverse("kitchen_restaurant:dish-type-update", kwargs={"pk": self.dish_type.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_type_form.html")

    def test_dish_type_delete_view(self):
        url = reverse("kitchen_restaurant:dish-type-delete", kwargs={"pk": self.dish_type.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_type_confirm_delete.html")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get("kitchen_restaurant:cook-list")
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test321"
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="Test Dish Type")
        self.cook = Cook.objects.create(
            username="test_user",
            password="test123456"
        )
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test description",
            price=10.99,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_cook_list_view(self):
        url = reverse("kitchen_restaurant:cook-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/cook_list.html")

    def test_cook_detail_view(self):
        url = reverse("kitchen_restaurant:cook-detail", kwargs={"pk": self.cook.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/cook_detail.html")

    def test_cook_create_view(self):
        url = reverse("kitchen_restaurant:cook-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/cook_form.html")

    def test_cook_update_view(self):
        url = reverse("kitchen_restaurant:cook-update", kwargs={"pk": self.cook.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/cook_form.html")

    def test_cook_delete_view(self):
        url = reverse("kitchen_restaurant:cook-delete", kwargs={"pk": self.cook.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/cook_confirm_delete.html")


class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get("kitchen_restaurant:dish-list")
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test321"
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="TestType")
        self.cook = self.user
        self.dish = Dish.objects.create(
            name="TestDish",
            description="Test description",
            price=10.99,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_dish_list_view(self):
        url = reverse("kitchen_restaurant:dish-list")
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_list.html")

    def test_dish_detail_view(self):
        url = reverse("kitchen_restaurant:dish-detail", kwargs={"pk": self.dish.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_detail.html")

    def test_dish_create_view(self):
        url = reverse("kitchen_restaurant:dish-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_form.html")

    def test_dish_update_view(self):
        url = reverse("kitchen_restaurant:dish-update", kwargs={"pk": self.dish.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_form.html")

    def test_dish_delete_view(self):
        url = reverse("kitchen_restaurant:dish-delete", kwargs={"pk": self.dish.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen_restaurant/dish_confirm_delete.html")
