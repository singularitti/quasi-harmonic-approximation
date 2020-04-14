import numpy as np

HBAR = 6.62607004e-34
BOLTZMANN = 1.380648e-23


def validate_frequency(frequency):
    if frequency < 0: ValueError("Negative frequency is not proper for QHA calculation!")


def bose_einstein_distribution(temperature, frequency):
    return 1 / (np.exp(HBAR * frequency / (BOLTZMANN * temperature)) - 1)


def subsystem_partition_function(temperature, frequency):
    if frequency == 0:
        return 1

    x = HBAR * frequency / (BOLTZMANN * temperature)
    return np.exp(x / 2) / (np.exp(x) - 1)


def subsystem_free_energy(temperature, frequency):
    validate_frequency(frequency)
    if frequency == 0:
        return 0

    hw = HBAR * frequency
    kt = BOLTZMANN * temperature
    return hw / 2 + kt * np.log(1 - np.exp(-hw / kt))


def subsystem_internal_energy(temperature, frequency):
    validate_frequency(frequency)
    if frequency == 0:
        return BOLTZMANN * temperature

    hw = HBAR * frequency
    return hw / 2 / np.tanh(hw / (2 * BOLTZMANN * temperature))


def subsystem_entropy(temperature, frequency):
    validate_frequency(frequency)

    n = bose_einstein_distribution(temperature, frequency)
    return BOLTZMANN * ((1 + n) * np.log(1 + n) - n * np.log(n))


def subsystem_volumetric_specific_heat(temperature, frequency):
    validate_frequency(frequency)
    if frequency == 0:
        return BOLTZMANN

    hw = HBAR * frequency
    kt = 2 * BOLTZMANN * temperature
    return BOLTZMANN * (hw / np.sinh(hw / kt) / kt) ** 2
