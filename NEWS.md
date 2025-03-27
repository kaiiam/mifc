# Changes between MIFC releases:

### v0.3.0

**Component**

* Rename `compound_analytical_measurement_protocol_doi` to `compound_analytical_measurement_protocol_url`

**Food**


### v0.2.0

**Component**

* Remove `id` from NamedThing and replace with `component_sample_id`

* Rename `measured_compound` to `component_type`

* Rename `measured_compound_label` to `component_type_label`

* Rename `measured_compound_recorded_value` to `component_recorded_value`

* Rename `measured_compound_unit` to `component_measurement_unit`

* Rename `measured_compound_data_points_number` to `component_data_points_number`

* Rename `measured_compound_record_date` to `component_record_date`

* Rename `measured_compound_analysis_date` to `component_analysis_date`

* Rename `measured_compound_comment` to `component_comment`

* Rename `measured_compound_derivation_type` to `component_derivation_type`

* Rename `measured_compound_limit_of_quantitation` to `component_limit_of_quantitation`

* Rename `compound_value_remeasured_for_quality_control` to `component_quality_control_remeasurement`

* Rename `analytical_analysis_measurement_method` to `compound_analytical_measurement_method`

* Rename `analytical_analysis_measurement_protocol_doi` to `compound_analytical_measurement_protocol_doi`

* Rename `laboratory_conducting_analytical_analysis` to `compound_analytical_laboratory_name`

* Rename `laboratory_sample_aliquot_id` to `food_laboratory_sample_aliquot_id` 

* Rename `laboratory_sample_batch_id` to `food_laboratory_sample_batch_id`

* Rename `laboratory_sample_id` to `food_laboratory_sample_id`

* Rename `laboratory_sample_aggregation_minimum_measured_compound_value` to `compound_sample_aggregation_minimum_value`

* Rename `laboratory_sample_aggregation_maximum_measured_compound_value` to `compound_sample_aggregation_maximum_value`

* Rename `laboratory_sample_aggregation_median_measured_compound_value` to `compound_sample_aggregation_median_value`

* Rename `laboratory_sample_aggregation_measured_compound_standard_deviation` to `compound_sample_aggregation_standard_deviation`

* Remove slots: `measured_compound_denominator_value` and `measured_compound_denominator_unit` and instead capture that information within the `measured_compound_unit` slot.

**Food**

* Rename `id` from NamedThing and replace with `food_sample_id`

* Rename `primary_food_type` to `food_primary_type`

* Rename `primary_food_type_label` to `food_primary_type_label`

* Rename `primary_food_type_upc_code` to `food_upc_code`

* Rename `primary_food_category_label` to `food_category_label`

* Enumeration `FoodPreparationState` separated into `FoodPreservationState`, `FoodStorageTemperatureState`, and `FoodRipenessState`.

* Break up slot `food_preparation_state` into slots `food_preservation_state`, `food_storage_temperature_state`, and `food_ripeness_state`.

**Provenance**

* Rename `dataset_label` to `provenance_dataset_label`

* Rename `mifc_version_tag` to `provenance_mifc_version_tag`

* Rename `contributor_orcid` to `provenance_contributor_orcid`

* Rename `organization_name` to `provenance_organization_name`
