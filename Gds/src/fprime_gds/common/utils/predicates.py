"""
predicates.py:

This file contains basic predicates as well as event and telemetry predicates used by the gds_test_api.py

:author: koran
"""

# Basic predicates
class less_than:
    """
    A predicate that evaluates a less-than comparison
    :param value: To return true, the predicate must be called on an object that is less than this value
    """
    def __init__(self, value):
        pass

class greater_than_pred:
    """
    A predicate that evaluates a greater-than comparison
    :param value: To return true, the predicate must be called on an object that is less than this value
    """
    def __init__(self, value):
        pass

class equal_to_pred:
    """
    A predicate that evaluates an equivalent comparison
    :param value: To return true, the predicate must be called on an object that is equal to this value
    """
    def __init__(self, value):
        pass

class not_equal_to_pred:
    """
    A predicate that evaluates a not-equivalent comparison
    :param value: To return true, the predicate must be called on an object that is not equal to this value
    """
    def __init__(self, value):
        pass

class greater_than_or_equals_pred:
    """
    A predicate that evaluates greater-than-or-equals comparison
    :param value: To return true, the predicate must be called on an object that is greater than or equal to this value
    """
    def __init__(self, value):
        pass

class less_than_or_equals_pred:
    """
    A predicate that evaluates a less-than-or-equals comparison
    :param value: To return true, the predicate must be called on an object that is less than or equal to this value
    """
    def __init__(self, value):
        pass
        
class within_range_pred:
    """
    A predicate that evaluates if the argument is between the two values
    :param lower: To return true, the predicate must be called on an object that is greater than this value
    :param upper: To return true, the predicate must be called on an object that is less than this value
    """
    def __init__(self, lower, upper):
        pass


# Set Predicates
class is_a_member_of_pred:
    """
    A predicate that evaluates if the argument is equivalent to any member in the set
    :param collection: To return true, the predicate must be called on an object that is equivalent to any object in this collection
    """
    def __init__(self, collection):
        pass

class is_not_a_member_of:
    """
    A predicate that evaluates if the argument is not equivalent to all members in the set
    :param collection: To return true, the predicate must be called on an object that is not equivalent to any object in this collection
    """
    def __init__(self, collection):
        pass


# Predicates that modify and combine other basic predicates
class invert:
    """
    A predicate that negates a given predicate. This predicate can be used like a NOT gate when combining predicates. 
    :param pred: The predicate to be negated.
    """
    def __init__(self, pred):
        pass
        

class satisfies_all:
    """
    A predicate that evaluates if the argument satisfies all predicates in the given list.
    This predicate can be used like an AND gate of N elements when combining predicates. 
    :param pred_list: a list of predicates
    """
    def __init__(self, pred_list):
        pass

class satisfies_any:
    """
    A predicate that evaluates if the argument satisfies any predicate in the given list.
    This predicate can be used like an OR gate of N elements when combining predicates. 
    :param pred_list: a list of predicates
    """
    def __init__(self, pred_list):
        pass


# Predicates that support the test api
class true_predicate:
    """
    used by event predicate and telemetry predicate as a placeholder when some predicates may not be specified. 
    """
    __init__(self):
        pass

class event_predicate:
    """
    A predicate for specifying a EventData object from data_types.event_data
    This predicate can be used to search a history
    :param id_pred: If specified, the object's id field must satisfy the given predicate for the telemetry predicate to evaluate to true.
    :param id_value: If specified, the object's value_obj field must satisfy the given predicate for the telemetry predicate to evaluate to true.
    :param time_pred: If specified, the object's time field must satisfy the given predicate for the telemetry predicate to evaluate to true.
    """
    def __init__(self, id_pred=None, args_pred=None, time_pred=None):
        pass
    """
    The telemetry_predicate checks that the telemetry object is an instance of EventData and will raise an error if the check fails. 
    """
    def __call__(self, event):
        pass

class telemetry_predicate:
    """
    A predicate for specifying a ChData object from data_types.ch_data
    This predicate can be used to search a history
    :param id_pred: If specified, the object's id field must satisfy the given predicate for the telemetry predicate to evaluate to true.
    :param id_value: If specified, the object's value_obj field must satisfy the given predicate for the telemetry predicate to evaluate to true.
    :param time_pred: If specified, the object's time field must satisfy the given predicate for the telemetry predicate to evaluate to true.
    """
    def __init__(self, id_pred=None, value_pred=None, time_pred=None):
        pass
    """
    The telemetry_predicate checks that the telemetry object is an instance of ChData and will raise an error if the check fails. 
    """
    def __call__(self, telemetry):
        pass


