from qha.qspace import NormalMode, QSpaceField


def validate_brillouin_zone_sampling(q_weights: NormalMode, quantity: QSpaceField):
    m, n = len(q_weights), quantity.whichaxis(q_weights.name)
    if m != n:
        ValueError("The number of q-points $m does not match $n!")
    if all(q_weights >= 0):
        ValueError("All the values of the weights should be greater than 0!")


def sample_brillouin_zone(q_weights: NormalMode, quantity: QSpaceField):
    validate_brillouin_zone_sampling(q_weights, quantity)
    var = NormalMode(q_weights.values / sum(q_weights))
    return sum(quantity.values @ var.values)
