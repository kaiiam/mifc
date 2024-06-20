## Container-Food-001
### Input
```yaml
foods:
- food_id: FDC:167512
  food_preservation_state: raw
  food_primary_type: FOOD:11954
  food_primary_type_label: Tomatillos, raw
- food_id: FDC:167513
  food_preservation_state: raw
  food_primary_type: FOOD:10100
  food_primary_type_label: Pork, fresh, variety meats and by-products, ears, frozen,
    raw
  food_storage_temperature_state: frozen

```
## Container-Component-001
### Input
```yaml
components:
- component_data_points_number: 1
  component_derivation_type: Analytical
  component_id: FDC:167512
  component_measurement_unit: g/(100.g)
  component_recorded_value: 5.88
  component_type: COMPONENT:1003
- component_data_points_number: 1
  component_derivation_type: Analytical
  component_id: FDC:167512
  component_measurement_unit: kcal/(100.g)
  component_recorded_value: 3.5
  component_type: COMPONENT:1007
- component_data_points_number: 2
  component_derivation_type: Analytical
  component_id: FDC:167512
  component_measurement_unit: kJ/(100.g)
  component_recorded_value: 1286.0
  component_type: COMPONENT:1062
- component_data_points_number: 0
  component_derivation_type: Calculated
  component_id: FDC:167512
  component_measurement_unit: mg/(100.g)
  component_recorded_value: 1.2
  component_type: COMPONENT:1079
- component_data_points_number: 1
  component_derivation_type: Estimated
  component_id: FDC:167512
  component_measurement_unit: ug/(100.g)
  component_recorded_value: 2.12
  component_type: COMPONENT:1089
- component_data_points_number: 2
  component_derivation_type: Analytical
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 4.34
  component_type: COMPONENT:1003
- component_data_points_number: 1
  component_derivation_type: Analytical
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 3.08
  component_type: COMPONENT:1007
- component_data_points_number: 0
  component_derivation_type: Sourced from literature
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1381.0
  component_type: COMPONENT:1062
- component_comment: Samples were obtained from 12 retail stores using a probability-based
    sampling plan.  Some fish had been treated during processing to retain moisture
    on thawing.  Untreated fish = 265 mg sodium/100g.
  component_data_points_number: 6
  component_derivation_type: Analytical
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1.4
  component_type: COMPONENT:1079
  laboratory_sample_aggregation_maximum_measured_compound_value: 2.2
  laboratory_sample_aggregation_median_measured_compound_value: 1.5
  laboratory_sample_aggregation_minimum_measured_compound_value: 0.8
- component_data_points_number: 3
  component_derivation_type: Analytical
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1.93
  component_type: COMPONENT:1089

```
## Container-Provenance-001
### Input
```yaml
provenances:
- contributor_orcid: https://orcid.org/0000-0002-3410-4655
  dataset_label: Standard Reference (SR) Legacy
  mifc_version_tag: v1.0.1
  organization_name: USDA

```
## Container-Component-003
### Input
```yaml
components:
- analytical_analysis_measurement_protocol_doi: SUGR-GALAC-CHG
  component_analysis_date: March 8, 2023
  component_data_points_number: 1
  component_id: '167512'
  component_measurement_unit: g/(100.g)
  component_quality_control_remeasurement: false
  component_recorded_value: 0.52
  component_type: COMPONENT:1075
  component_type_label: galactose
  laboratory_conducting_analytical_analysis: Silliker
  laboratory_sample_aliquot_id: NFY122JPN
  laboratory_sample_batch_id: o
  laboratory_sample_id: CY124QU
- analytical_analysis_measurement_protocol_doi: SUGR-DP1-2-CHG
  component_analysis_date: March 9, 2023
  component_data_points_number: 1
  component_id: '167513'
  component_limit_of_quantitation: <0.25
  component_measurement_unit: g/(100.g)
  component_recorded_value: 0.0
  component_type: COMPONENT:1014
  component_type_label: maltose
  laboratory_conducting_analytical_analysis: Silliker
  laboratory_sample_aliquot_id: NFY122JRQ
  laboratory_sample_batch_id: o
  laboratory_sample_id: CY124QX
- analytical_analysis_measurement_protocol_doi: SUGR-DP1-2-CHG
  component_analysis_date: March 17, 2023
  component_data_points_number: 1
  component_id: '167514'
  component_limit_of_quantitation: <0.25
  component_measurement_unit: g/(100.g)
  component_quality_control_remeasurement: true
  component_recorded_value: 0.0
  component_type: COMPONENT:1011
  component_type_label: glucose
  laboratory_conducting_analytical_analysis: Silliker
  laboratory_sample_aliquot_id: NFY122JV9
  laboratory_sample_batch_id: q
  laboratory_sample_id: CY124R2

```
## Container-Component-002
### Input
```yaml
components:
- analytical_analysis_measurement_method: HPLC
  component_data_points_number: 1
  component_id: FDC:167512
  component_measurement_unit: g/(100.g)
  component_recorded_value: 5.88
  component_type: COMPONENT:1003
- analytical_analysis_measurement_method: GC
  component_data_points_number: 1
  component_id: FDC:167512
  component_measurement_unit: kcal/(100.g)
  component_recorded_value: 3.5
  component_type: COMPONENT:1007
- analytical_analysis_measurement_method: GLC
  component_data_points_number: 2
  component_id: FDC:167512
  component_measurement_unit: kJ/(100.g)
  component_recorded_value: 1286.0
  component_type: COMPONENT:1062
- analytical_analysis_measurement_method: Nephelometry
  component_data_points_number: 0
  component_id: FDC:167512
  component_measurement_unit: mg/(100.g)
  component_recorded_value: 1.2
  component_type: COMPONENT:1079
- analytical_analysis_measurement_method: Gravimetric
  analytical_analysis_measurement_protocol_doi: ' AOAC 934.06 mod'
  component_data_points_number: 1
  component_id: FDC:167512
  component_measurement_unit: ug/(100.g)
  component_recorded_value: 2.12
  component_type: COMPONENT:1089
- analytical_analysis_measurement_method: Fluorometric
  analytical_analysis_measurement_protocol_doi: AOAC 985.01 + 984.27
  component_data_points_number: 2
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 4.34
  component_type: COMPONENT:1003
- analytical_analysis_measurement_method: Kjeldahl
  component_data_points_number: 1
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 3.08
  component_type: COMPONENT:1007
- analytical_analysis_measurement_method: HPLC
  analytical_analysis_measurement_protocol_doi: AOAC 996.06
  component_data_points_number: 0
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1381.0
  component_type: COMPONENT:1062
- analytical_analysis_measurement_method: HPLC
  component_data_points_number: 6
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1.4
  component_type: COMPONENT:1079
- analytical_analysis_measurement_method: HPLC
  component_data_points_number: 3
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1.93
  component_type: COMPONENT:1089

```
## Container-Food-002
### Input
```yaml
components:
- analytical_analysis_measurement_method: HPLC
  component_data_points_number: 1
  component_id: FDC:167512
  component_measurement_unit: g/(100.g)
  component_recorded_value: 5.88
  component_type: COMPONENT:1003
- analytical_analysis_measurement_method: GC
  component_data_points_number: 1
  component_id: FDC:167512
  component_measurement_unit: kcal/(100.g)
  component_recorded_value: 3.5
  component_type: COMPONENT:1007
- analytical_analysis_measurement_method: GLC
  component_data_points_number: 2
  component_id: FDC:167512
  component_measurement_unit: kJ/(100.g)
  component_recorded_value: 1286.0
  component_type: COMPONENT:1062
- analytical_analysis_measurement_method: Nephelometry
  component_data_points_number: 0
  component_id: FDC:167512
  component_measurement_unit: mg/(100.g)
  component_recorded_value: 1.2
  component_type: COMPONENT:1079
- analytical_analysis_measurement_method: Gravimetric
  analytical_analysis_measurement_protocol_doi: ' AOAC 934.06 mod'
  component_data_points_number: 1
  component_id: FDC:167512
  component_measurement_unit: ug/(100.g)
  component_recorded_value: 2.12
  component_type: COMPONENT:1089
- analytical_analysis_measurement_method: Fluorometric
  analytical_analysis_measurement_protocol_doi: AOAC 985.01 + 984.27
  component_data_points_number: 2
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 4.34
  component_type: COMPONENT:1003
- analytical_analysis_measurement_method: Kjeldahl
  component_data_points_number: 1
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 3.08
  component_type: COMPONENT:1007
- analytical_analysis_measurement_method: HPLC
  analytical_analysis_measurement_protocol_doi: AOAC 996.06
  component_data_points_number: 0
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1381.0
  component_type: COMPONENT:1062
- analytical_analysis_measurement_method: HPLC
  component_data_points_number: 6
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1.4
  component_type: COMPONENT:1079
- analytical_analysis_measurement_method: HPLC
  component_data_points_number: 3
  component_id: FDC:167513
  component_measurement_unit: g/(100.g)
  component_recorded_value: 1.93
  component_type: COMPONENT:1089

```
## Container-Food-001-missing-component_id
### Input
```yaml
foods:
- food_preservation_state: raw
  food_primary_type: FOOD:11954
  food_primary_type_label: Tomatillos, raw
- food_preservation_state: 1
  food_primary_type: FOOD:10100
  food_primary_type_label: Pork, fresh, variety meats and by-products, ears, frozen,
    raw
  food_storage_temperature_state: frozen

```
## Container-Food-001-illegal-primary-preservation
### Input
```yaml
foods:
- food_id: FDC:167512
  food_preservation_state: raw
  food_primary_type: FOOD:11954
  food_primary_type_label: Tomatillos, raw
- food_id: FDC:167513
  food_preservation_state: 1
  food_primary_type: FOOD:10100
  food_primary_type_label: Pork, fresh, variety meats and by-products, ears, frozen,
    raw
  food_storage_temperature_state: frozen

```
