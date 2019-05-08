import hyperparameters

def get_ip(third_level, fourth_level):
    return "%s.%d.%d" % (str(hyperparameters.ip_base), third_level, fourth_level)
