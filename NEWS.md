# Changes between MIFC releases:

### v0.2.0

**Component**

* Remove slots: `measured_compound_denominator_value` and `measured_compound_denominator_unit` and instead capture that information within the `measured_compound_unit` slot.

**Food**

* Enumeration `FoodPreparationState` separated into `FoodPreservationState`, `FoodStorageTemperatureState`, and `FoodRipenessState`.

* Break up slot `food_preparation_state` into slots `food_preservation_state`, `food_storage_temperature_state`, and `food_ripeness_state`.