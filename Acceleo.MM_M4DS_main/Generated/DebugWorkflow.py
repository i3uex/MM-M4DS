print(impute_mostFrequent(sex, IRISCHOOL, ETHNICITY))	#DataProcessing name
print('NO SOURCE')         					#SOURCE
print('impute_fix_value(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)')         #TARGET
	print('parameter_derivedValue_impute_mostFrequent')			#DerivedValue
	print('Missing')
	print('MostFrequent')
	print('def_parameter_impute_categorical_columns_der_value')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_sex_columns')
print('PRECONDITION_impute_IRSCHOOL_columns')
print('PRECONDITION_impute_ETHNICITY_columns')
print('POSTCONDITION_impute_sex_columns')
print('POSTCONDITION_impute_IRSCHOOL_columns')
print('POSTCONDITION_impute_ETHNICITY_columns')
print('INVARIANT_impute_sex_columns')
print('INVARIANT_impute_IRSCHOOL_columns')
print('INVARIANT_impute_ETHNICITY_columns')
############################################################
print(deprecated_impute(sex))	#DataProcessing name
print('NO SOURCE')         					#SOURCE
print('NO TARGET')         					#TARGET
	print('parameter_impute_sex')			#DerivedValue
	print('Missing')
	print('MostFrequent')
	print('def_parameter_impute_categorical_col_der_value')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_sex')
print('POSTCONDITION_impute_sex')
print('INVARIANT_impute_sex')
############################################################
print(deprecated_impute(IRSCHOOL))	#DataProcessing name
print('NO SOURCE')         					#SOURCE
print('NO TARGET')         					#TARGET
	print('parameter_impute_IRSCHOOL')			#DerivedValue
	print('Missing')
	print('MostFrequent')
	print('def_parameter_impute_categorical_col_der_value')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_IRSCHOOL')
print('POSTCONDITION_impute_IRSCHOOL')
print('INVARIANT_impute_IRSCHOOL')
############################################################
print(deprecated_impute(ETHNICITY))	#DataProcessing name
print('NO SOURCE')         					#SOURCE
print('NO TARGET')         					#TARGET
	print('parameter_impute_ETHNICITY')			#DerivedValue
	print('Missing')
	print('MostFrequent')
	print('def_parameter_impute_categorical_col_der_value')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_ETHNICITY')
print('POSTCONDITION_impute_ETHNICITY')
print('INVARIANT_impute_ETHNICITY')
############################################################
print(impute_fix_value(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1))	#DataProcessing name
print('impute_mostFrequent(sex, IRISCHOOL, ETHNICITY)')         #SOURCE
print('impute_mean(avg_income, distance)')         #TARGET
	print('parameter_fixValue_impute_fixValue')			#FixValue
	print('Missing')
	print('Unknown')			#Es unknown porque el valor concreto no se ha definido, se define en la llamada
	print('def_parameter_impute_categorical_col_fix_value')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_ACADEMIC_INTEREST_2')
print('POSTCONDITION_impute_ACADEMIC_INTEREST_2')
print('INVARIANT_impute_ACADEMIC_INTEREST_2')
print('PRECONDITION_impute_ACADEMIC_INTEREST_1')
print('POSTCONDITION_impute_ACADEMIC_INTEREST_1')
print('INVARIANT_impute_ACADEMIC_INTEREST_1')
############################################################
print(impute_mean(avg_income, distance))	#DataProcessing name
print('impute_fix_value(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)')         #SOURCE
print('impute_linear_interpolation(satscore)')         #TARGET
	print('parameter_num_op_impute_mean')			#NumOp
	print('Missing')
	print('Mean')
	print('def_impute_cont_columns_param_numOp')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_mean_avg_income')
print('PRECONDITION_impute_mean_distance')
print('POSTCONDITION_impute_mean_avg_income')
print('POSTCONDITION_impute_mean_distance')
print('INVARIANT_impute_mean_avg_income')
print('INVARIANT_impute_mean_distance')
############################################################
print(impute_linear_interpolation(satscore))	#DataProcessing name
print('impute_mean(avg_income, distance)')         #SOURCE
print('row_filter(init_span)')         #TARGET
	print('parameter_num_op_impute_mean')			#NumOp
	print('Missing')
	print('Mean')
	print('def_impute_cont_columns_param_numOp')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_linear_interpolation_satscore')
print('POSTCONDITION_impute_linear_interpolation_satscore')
print('INVARIANT_impute_linear_interpolation_satscore')
############################################################
print(row_filter(init_span))	#DataProcessing name
print('impute_linear_interpolation(satscore)')         #SOURCE
print('column_cont_filter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail)')         #TARGET
	print('parameter_filter_row_filter')			#FilterValue
	print('def_parameter_filter_row_filter')
		print('parameter_primitive_row_filter')			#Primitive
		print('0')
		print('def_parameter_primitive_row_filter')
	print('parameter_primitive_row_filter')			#Primitive
	print('0')
	print('def_parameter_primitive_row_filter')
#-----------------------------------------------------------------------------
print('PRECONDITION_row_filter')
print('POSTCONDITION_row_filter')
############################################################
print(column_cont_filter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail))	#DataProcessing name
print('row_filter(init_span)')         #SOURCE
print('column_cat_filter(CONTACT_CODE1)')         #TARGET
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	print('parameter_column_cont_filter')			#Field
	print('BELONG')
	print('def_field_parameter_column_cont_filter')
		print('TRAVEL_INIT_CNTCTS_column_filter')		#DataField
		print('false')
		print('Integer')
		print('false')
		print('TRAVEL_INIT_CNTCTS')
			print('def_input_column_cont_filter')			#Continuous
				print('0.0')			#Interval
				print('5.0')
				print('closedClosed')
			#-----------------------------------
		print('REFERRAL_CNCTS_column_filter')		#DataField
		print('false')
		print('String')
		print('false')
		print('REFERRAL_CNCTS')
			print('def_input_column_cont_filter')			#Continuous
				print('0.0')			#Interval
				print('5.0')
				print('closedClosed')
			#-----------------------------------
#-----------------------------------------------------------------------------
print('PRECONDITION_column_cont_filter')
print('POSTCONDITION_column_cont_filter')
############################################################
print(column_cat_filter(CONTACT_CODE1))	#DataProcessing name
print('column_cont_filter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail)')         #SOURCE
print('map(TERRITORY)')         #TARGET
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	print('parameter_column_cat_filter')			#Field
	print('BELONG')
	print('def_field_parameter_column_cat_filter')
		print('CONTACT_CODE1')		#DataField
		print('false')
		print('String')
		print('false')
		print('CONTACT_CODE1')
			print('false')			#Categorical
			print('def_column_cat_filter_input_dataField')
			#-----------------------------------
#-----------------------------------------------------------------------------
print('PRECONDITION_column_cat_filter')
print('POSTCONDITION_column_cat_filter')
############################################################
print(map(TERRITORY))	#DataProcessing name
print('column_cat_filter(CONTACT_CODE1)')         #SOURCE
print('map(Instate)')         #TARGET
	print('parameter_map_territory_A')			#Map
	print('0')
	print('def_parameter_map_categorical_col')
	print('parameter_map_territory_N')			#Map
	print('0')
	print('def_parameter_map_categorical_col')
#-----------------------------------------------------------------------------
print('PRECONDITION_map_territory')
print('POSTCONDITION_map_territory')
print('INVARIANT_map_categorical_col')
############################################################
print(map(Instate))	#DataProcessing name
print('map(TERRITORY)')         #SOURCE
print('stringToNumber (TERRITORY, init1rat, init2rat, hscrat, Instate)')         #TARGET
	print('parameter_map_instate_Y')			#Map
	print('1')
	print('def_parameter_map_categorical_col')
	print('parameter_map_Instate_N')			#Map
	print('0')
	print('def_parameter_map_categorical_col')
#-----------------------------------------------------------------------------
print('PRECONDITION_map_Instate')
print('POSTCONDITION_map_Instate')
print('INVARIANT_map_Instate')
############################################################
print(stringToNumber (TERRITORY, init1rat, init2rat, hscrat, Instate))	#DataProcessing name
print('map(Instate)')         #SOURCE
print('impute_outliers_closest(avg_income, distance, premiere, sex, Enroll, Instate)')         #TARGET
#-----------------------------------------------------------------------------
print('INVARIANT_stringToNumber_TERRITORY')
print('INVARIANT_stringToNumber_init1rat')
print('INVARIANT_stringToNumber_init2rat')
print('INVARIANT_stringToNumber_hscrat')
print('INVARIANT_stringToNumber_Instate')
############################################################
print(impute_outliers_closest(avg_income, distance, premiere, sex, Enroll, Instate))	#DataProcessing name
print('stringToNumber (TERRITORY, init1rat, init2rat, hscrat, Instate)')         #SOURCE
print('binner (TOTAL_CONTACTS, SELF_INIT_CNTCTS, SOLICITED_CNTCTS)')         #TARGET
	print('parameter_num_op_impute_mean')			#NumOp
	print('Outlier')
	print('Closest')
	print('def_impute_cont_columns_param_numOp')
#-----------------------------------------------------------------------------
print('PRECONDITION_impute_outliers_closest_avg_income')
print('PRECONDITION_impute_outliers_closest_distance')
print('PRECONDITION_impute_outliers_closest_premiere')
print('PRECONDITION_impute_outliers_closest_sex')
print('PRECONDITION_impute_outliers_closest_Enroll')
print('PRECONDITION_impute_outliers_closest_Instate')
print('POSTCONDITION_impute_outliers_closest_avg_income')
print('POSTCONDITION_impute_outliers_closest_distance')
print('POSTCONDITION_impute_outliers_closest_premiere')
print('POSTCONDITION_impute_outliers_closest_sex')
print('POSTCONDITION_impute_outliers_closest_Enroll')
print('POSTCONDITION_impute_outliers_closest_Instate')
print('INVARIANT_impute_outliers_closest_avg_income')
print('INVARIANT_impute_outliers_closest_distance')
print('INVARIANT_impute_outliers_closest_premiere')
print('INVARIANT_impute_outliers_closest_sex')
print('INVARIANT_impute_outliers_closest_Enroll')
print('INVARIANT_impute_outliers_closest_Instate')
############################################################
print(binner (TOTAL_CONTACTS, SELF_INIT_CNTCTS, SOLICITED_CNTCTS))	#DataProcessing name
print('impute_outliers_closest(avg_income, distance, premiere, sex, Enroll, Instate)')         #SOURCE
print('binner (TERRITORY)')         #TARGET
	print('binner_parameter_derivedField_TOTAL_CONTACTS')			#DerivedField
	print('TOTAL_CONTACTS_binned')
	print('String')
	print('def_binner_parameter_derived_field')
	print('binner_TOTAL_CONTACTS_out')
	print('false')
	print('String')
	print('false')
	print('TOTAL_CONTACTS_binned')
	print('binner_parameter_derivedField_SELF_INIT_CNTCTS')			#DerivedField
	print('SELF_INIT_CNTCTS_binned')
	print('String')
	print('def_binner_parameter_derived_field')
	print('binner_SELF_INIT_CNTCTS_out')
	print('false')
	print('String')
	print('false')
	print('SELF_INIT_CNTCTS_binned')
	print('binner_parameter_derivedField_SOLICITED_CNTCTS')			#DerivedField
	print('SOLICITED_CNTCTS_binned')
	print('String')
	print('def_binner_parameter_derived_field')
	print('binner_SOLICITED_CNTCTS_out')
	print('false')
	print('String')
	print('false')
	print('SOLICITED_CNTCTS_binned')
	print('binner_parameter_discretize_bin_Low')		#DiscretizeBin
	print('low')
	print('def_binner_parameter_bin')
		print('-1000.0')		#Interval
		print('1.0')
		print('opeOpen')
	print('binner_parameter_discretize_bin_Moderate')		#DiscretizeBin
	print('Moderate')
	print('def_binner_parameter_bin')
		print('1.0')		#Interval
		print('4.0')
		print('closedOpen')
	print('binner_parameter_discretize_bin_High')		#DiscretizeBin
	print('High')
	print('def_binner_parameter_bin')
		print('4.0')		#Interval
		print('1000.0')
		print('closedOpen')
#-----------------------------------------------------------------------------
print('PRECONDITION_binner_TOTAL_CONTACTS')
print('PRECONDITION_binner_SELF_INIT_CNTCTS')
print('PRECONDITION_binner_SOLICITED_CNTCTS')
print('POSTCONDITION_binner_TOTAL_CONTACTS')
print('POSTCONDITION_binner_SELF_INIT_CNTCTS')
print('POSTCONDITION_binner_SOLICITED_CNTCTS')
print('INVARIANT_binner_TOTAL_CONTACTS')
print('INVARIANT_binner_SELF_INIT_CNTCTS')
print('INVARIANT_binner_SOLICITED_CNTCTS')
############################################################
print(binner (TERRITORY))	#DataProcessing name
print('binner (TOTAL_CONTACTS, SELF_INIT_CNTCTS, SOLICITED_CNTCTS)')         #SOURCE
print('NO TARGET')         					#TARGET
	print('binner_parameter_derivedField_TERRITORY_binned')			#DerivedField
	print('TERRITORY_binned')
	print('String')
	print('def_binner_parameter_derived_field')
	print('binner_TERRITORY_out')
	print('false')
	print('String')
	print('false')
	print('TERRITORY_binned')
	print('binner_parameter_discretize_bin_Unknown')		#DiscretizeBin
	print('Unknown')
	print('def_binner_parameter_bin')
		print('-1000.0')		#Interval
		print('1.0')
		print('opeOpen')
	print('binner_parameter_discretize_bin_Zone1')		#DiscretizeBin
	print('Zone 1')
	print('def_binner_parameter_bin')
		print('1.0')		#Interval
		print('3.0')
		print('closedOpen')
	print('binner_parameter_discretize_bin_Zone2')		#DiscretizeBin
	print('Zone 2')
	print('def_binner_parameter_bin')
		print('3.0')		#Interval
		print('5.0')
		print('closedOpen')
	print('binner_parameter_discretize_bin_Zone3')		#DiscretizeBin
	print('Zone 3')
	print('def_binner_parameter_bin')
		print('5.0')		#Interval
		print('7.0')
		print('closedOpen')
	print('binner_parameter_discretize_bin_Zone4')		#DiscretizeBin
	print('Zone 4')
	print('def_binner_parameter_bin')
		print('7.0')		#Interval
		print('1000.0')
		print('closedClosed')
#-----------------------------------------------------------------------------
print('PRECONDITION_binner_TERRITORY')
print('POSTCONDITION_binner_TERRITORY')
print('INVARIANT_binner_TERRITORY')
############################################################








