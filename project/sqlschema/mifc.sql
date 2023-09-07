

CREATE TABLE "Component" (
	id TEXT NOT NULL, 
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
	PRIMARY KEY (id)
);

CREATE TABLE "Container" (
	foods TEXT, 
	components TEXT, 
	PRIMARY KEY (foods, components)
);

CREATE TABLE "Food" (
	id TEXT NOT NULL, 
	primary_food_type TEXT, 
	primary_food_type_label TEXT, 
	food_preparation_state VARCHAR(18), 
	PRIMARY KEY (id)
);
