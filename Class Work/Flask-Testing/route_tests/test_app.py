from unittest import TestCase

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################


class IndexTests(TestCase):
    """Tests for the index route."""

    def test_index(self):
        """Test that the index page shows "Hello, World!" """
        res = app.test_client().get('/')
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        expected_page_text = "Hello, World!"
        self.assertEqual(expected_page_text, result_page_text)


#######################
# Favorite Color Tests
#######################

class ColorTests(TestCase):
    """Tests for the Color route."""

    def test_color_results_blue(self):
        result = app.test_client().get('/color_results?color=blue')

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = 'Wow, blue is my favorite color, too!'
        self.assertEqual(expected_page_text, result_page_text)

    def test_color_results_light_green(self):
        # 'light green'.
        result = app.test_client().get("/color_results?color=light-green")

        self.assertEqual(result.status_code, 200)

        page_text = result.get_data(as_text=True)
        expected_text = "Wow, light-green is my favorite color, too!"
        self.assertEqual(expected_text, page_text)

    def test_color_results_empty(self):
        # no color
        result = app.test_client().get("/color_results")

        self.assertEqual(result.status_code, 200)

        page_text = result.get_data(as_text=True)
        expected_text = "Wow, None is my favorite color, too!"
        self.assertEqual(expected_text, page_text)


#######################
# Froyo Tests
#######################

class FroyoTests(TestCase):
    def test_froyo_results_scenario1(self):
        res = app.test_client().get("/froyo_results?flavor=1&toppings=2")

        self.assertEqual(res.status_code, 200)

        page_text = res.get_data(as_text=True)
        expected_text = "You ordered 1 flavored Fro-Yo with toppings 2!"
        self.assertEqual(page_text, expected_text)

    def test_froyo_results_scenario2(self):
        # TODO: Fill in this function to test the show_froyo_results route under a
        # specific scenario.
        pass

    def test_froyo_results_edgecase1(self):
        res = app.test_client().get("/froyo_results")

        self.assertEqual(res.status_code, 200)

        page_text = res.get_data(as_text=True)
        expected_text = "You ordered None flavored Fro-Yo with toppings None!"
        self.assertEqual(page_text, expected_text)

    def test_froyo_results_edgecase2(self):
        # TODO: Fill in this function to test the show_froyo_results route under a
        # specific EDGE CASE scenario.
        pass


#######################
# Reverse Message Tests
#######################

class MessageTests(TestCase):
    def test_message_results_helloworld(self):
        form_data = {
            'message': 'Hello World'
        }
        res = app.test_client().post('/message_results', data=form_data)
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        self.assertIn('dlroW olleH', result_page_text)

    def test_message_results_scenario2(self):
        form_data = {
            "message": "Alex"
        }

        res = app.test_client().post("/message_results", data=form_data)
        self.assertEqual(res.status_code, 200)

        page_text = res.get_data(as_text=True)
        expected_text = "xelA"
        self.assertIn(expected_text, page_text)

    def test_message_results_edgecase1(self):
        # TODO: Fill in this function to test the message_results route under
        # an edge case scenario.
        pass


#######################
# Calculator Tests
#######################

class CalculatorTests(TestCase):
    def test_calculator_results_scenario1(self):
        res = app.test_client().get("/calculator_results?operand1=2&operation=add&operand2=5")

        self.assertEqual(res.status_code, 200)

        page_text = res.get_data(as_text=True)
        expected_text = "You chose to add 2 and 5. Your result is: 7"
        self.assertEqual(page_text, expected_text)

    def test_calculator_results_scenario2(self):
        # TODO: Fill in this function to test the calculator_results route under a
        # specific scenario.
        pass

    def test_calculator_results_scenario3(self):
        # TODO: Fill in this function to test the calculator_results route under a
        # specific scenario.
        pass

    def test_calculator_results_scenario4(self):
        # TODO: Fill in this function to test the calculator_results route under a
        # specific scenario.
        pass

    def test_calculator_results_edgecase1(self):
        # TODO: Fill in this function to test the calculator_results route under a
        # specific EDGE CASE scenario.
        pass

    def test_calculator_results_edgecase2(self):
        # TODO: Fill in this function to test the calculator_results route under a
        # specific EDGE CASE scenario.
        pass
