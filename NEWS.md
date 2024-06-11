# Changes between MIFC releases:

### v0.2.0

**Component**

* Rename `measured_compound` to `measured_compound_type`

* Rename `measured_compound_value` to `measured_compound_recorded_value`

* Remove slots: `measured_compound_denominator_value` and `measured_compound_denominator_unit` and instead capture that information within the `measured_compound_unit` slot.

**Food**

* Rename `primary_food_type` to `food_primary_type`

* Rename `primary_food_type_label` to `food_primary_type_label`

* Rename `primary_food_type_upc_code` to `food_upc_code`

* Rename `primary_food_category_label` to `food_category_label`

* Enumeration `FoodPreparationState` separated into `FoodPreservationState`, `FoodStorageTemperatureState`, and `FoodRipenessState`.

* Break up slot `food_preparation_state` into slots `food_preservation_state`, `food_storage_temperature_state`, and `food_ripeness_state`.

