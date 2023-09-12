

CREATE TABLE "Component" (
	id TEXT, 
	measured_compound TEXT, 
	measured_compound_value FLOAT, 
	measured_compound_unit TEXT, 
	measured_compound_denominator_value FLOAT, 
	measured_compound_denominator_unit TEXT, 
	measured_compound_data_points_number INTEGER, 
	measured_compound_record_date TEXT, 
	measured_compound_comment TEXT, 
	measured_compound_derivation_type TEXT, 
	laboratory_sample_aggregation_minimum_measured_compound_value FLOAT, 
	laboratory_sample_aggregation_maximum_measured_compound_value FLOAT, 
	laboratory_sample_aggregation_median_measured_compound_value FLOAT, 
	laboratory_sample_aggregation_measured_compound_standard_deviation FLOAT, 
	analytical_analysis_measurement_protocol_doi TEXT, 
	analytical_analysis_measurement_method VARCHAR(12), 
	PRIMARY KEY (id, measured_compound, measured_compound_value, measured_compound_unit, measured_compound_denominator_value, measured_compound_denominator_unit, measured_compound_data_points_number, measured_compound_record_date, measured_compound_comment, measured_compound_derivation_type, laboratory_sample_aggregation_minimum_measured_compound_value, laboratory_sample_aggregation_maximum_measured_compound_value, laboratory_sample_aggregation_median_measured_compound_value, laboratory_sample_aggregation_measured_compound_standard_deviation, analytical_analysis_measurement_protocol_doi, analytical_analysis_measurement_method)
);

CREATE TABLE "Container" (
	foods TEXT, 
	components TEXT, 
	PRIMARY KEY (foods, components)
);

CREATE TABLE "Food" (
	id TEXT, 
	primary_food_type TEXT, 
	primary_food_type_label TEXT, 
	primary_food_type_upc_code INTEGER, 
	food_preparation_state VARCHAR(18), 
	food_acquisition_city TEXT, 
	food_acquisition_country TEXT, 
	food_acquisition_country_subdivision TEXT, 
	food_acquisition_date TEXT, 
	food_distributor_city TEXT, 
	food_distributor_country TEXT, 
	food_distributor_country_subdivision TEXT, 
	food_expiration_date TEXT, 
	PRIMARY KEY (id, primary_food_type, primary_food_type_label, primary_food_type_upc_code, food_preparation_state, food_acquisition_city, food_acquisition_country, food_acquisition_country_subdivision, food_acquisition_date, food_distributor_city, food_distributor_country, food_distributor_country_subdivision, food_expiration_date)
);
