class Assertions:
    @staticmethod
    def assert_value(value_type, expected_value, actual_value):
        assert actual_value == expected_value, \
            value_type + "\n" \
            + "Actual " + " = " \
            + actual_value + " <> " \
            + "Expected Type" + value_type + " = " + expected_value

    @staticmethod
    def assert_boolean_value(value_type, expected_value, actual_value):
        assert actual_value == expected_value, \
            value_type + "\n" \
            + "Actual " + " = " \
            + str(actual_value) + " <> " \
            + "Expected Type" + value_type + " = " + str(expected_value)

    @staticmethod
    def assert_value_with_err_message(value_type, expected_value, actual_value, error_message):
        assert actual_value == expected_value, \
            value_type + "\n" + error_message + "\n"

    @staticmethod
    def assert_value_in_string(value_type, expected_sub_string_value, actual_string_value):
        assert expected_sub_string_value in actual_string_value, \
            "Actual " + value_type + " = " \
            + actual_string_value + " <> " \
            + "Expected Type" + value_type + " = " + expected_sub_string_value
