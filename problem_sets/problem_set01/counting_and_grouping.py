def item_order(order):
    """Count and group a customer's order

    Create a list of a customer's order sorted by items and their order counts.
    The items that a customer can order are limited to:
                                             'salad', 'hamburger' and 'water'

    Args:
        order: a customer's order

    Returns:
        the string of a sorted customer's order in the following format:
        'salad:[# salad] hamburger:[# hambruger] water:[# water]'

    Raises:
        TypeError: if order is not a string
    """
    salad = 'salad'
    salad_num = 0
    hamburger = 'hamburger'
    hamburger_num = 0
    water = 'water'
    water_num = 0

    for idx, item in enumerate(order):
        if order[idx:idx+len(salad)] == salad:
            salad_num += 1
        elif order[idx:idx+len(hamburger)] == hamburger:
            hamburger_num += 1
        elif order[idx:idx+len(water)] == water:
            water_num += 1

    return '%s:%d %s:%d %s:%d' % (salad, salad_num,
                                  hamburger, hamburger_num,
                                  water, water_num)

    # return '{}:{} {}:{} {}:{}'.format(salad, salad_num,
    #                                   hamburger, hamburger_num,
    #                                   water, water_num)

    # return (salad + ':' + str(salad_num),
    #         hamburger + ':' + str(hamburger_num),
    #         water + ':' + str(water_num))

    # return (salad + ':' + str(salad_num) + ' ' +
    #         hamburger + ':' + str(hamburger_num) + ' ' +
    #         water + ':' + str(water_num))

#  Test function:
item_order('salad water hamburger salad hamburger')
item_order('hamburger water hamburger')

###############################################################################

# NOTES: Test cases

# [Test case 1]
# If order = "salad water hamburger salad hamburger"
# then the function returns "salad:2 hamburger:2 water:1"

# [Test case 2]
# If order = "hamburger water hamburger"
# then the function returns "salad:0 hamburger:2 water:1"


# NOTES: How to return?
# [Example 1: String concatenation with + symbol]

# return (salad + ':' + str(salad_num) + ' ' +
#         hamburger + ':' + str(hamburger_num) + ' ' +
#         water + ':' + str(water_num))

# output: salad:2 hamburger:2 water:1

# [Example 2: String concatenation? with , symbol]

# return (salad + ':' + str(salad_num),
#         hamburger + ':' + str(hamburger_num),
#         water + ':' + str(water_num))

# output: ('salad:2', 'hamburger:2', 'water:1')

# [Example 3]

# return '%s:%d %s:%d %s:%d' % (salad, salad_num,
#                             hamburger, hamburger_num,
#                             water, water_num)

# output: salad:2 hamburger:2 water:1

# [Example 4]

# return '{}:{} {}:{} {}:{}'.format(salad, salad_num,
#                                 hamburger, hamburger_num,
#                                 water, water_num)

# output: salad:2 hamburger:2 water:1
