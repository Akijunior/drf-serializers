
def check_valid_list(list_var, keys):
	dict_fields = {}
	
	for key in keys:
		if list_var.get(key, None) is None:
			dict_fields[key] = '%s eh requerido' % (key)
	return dict_fields


def check_unique(model, data):
	return model.objects.filter(name = data).exists()