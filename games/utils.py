
def check_valid_list(list_var):
	pass

def check_unique(model, key, data):
	return model.objetcs.filter(key == data).exist()